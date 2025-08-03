#!/usr/bin/env python3
"""
CSV Relationship Discovery Tool
Analyzes all 45 CSV files to identify relational connections and common keys
"""

import pandas as pd
import os
import json
from pathlib import Path
from collections import defaultdict
import re

class CivRelationshipAnalyzer:
    def __init__(self):
        self.logs_path = Path(os.path.expandvars(r"${LOCALAPPDATA}\Firaxis Games\Sid Meier's Civilization VI\Logs"))
        self.relationships = defaultdict(list)
        self.common_keys = defaultdict(set)
        self.file_structures = {}
        
    def load_analysis_results(self):
        """Load the existing CSV analysis results"""
        try:
            with open('csv_analysis_20250803_191142.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print("❌ Analysis results not found. Run analyze_all_csv_files.py first.")
            return None
    
    def identify_common_patterns(self, analysis_results):
        """Identify common column patterns across all CSV files"""
        
        # Track all column patterns
        all_columns = defaultdict(list)
        turn_columns = []
        player_columns = []
        city_columns = []
        
        for filename, info in analysis_results.items():
            if 'error' in info:
                continue
                
            columns = info.get('columns', [])
            
            for col in columns:
                clean_col = col.strip().lower()
                all_columns[clean_col].append(filename)
                
                # Identify key column types
                if 'turn' in clean_col or 'game turn' in clean_col:
                    turn_columns.append((filename, col))
                elif 'player' in clean_col or 'civilization' in clean_col:
                    player_columns.append((filename, col))
                elif 'city' in clean_col:
                    city_columns.append((filename, col))
        
        return {
            'all_columns': all_columns,
            'turn_columns': turn_columns,
            'player_columns': player_columns,
            'city_columns': city_columns
        }
    
    def create_relationship_matrix(self, patterns):
        """Create a matrix showing relationships between files"""
        
        # Files with turn data (temporal relationships)
        turn_files = set([filename for filename, col in patterns['turn_columns']])
        
        # Files with player data (competitive relationships)
        player_files = set([filename for filename, col in patterns['player_columns']])
        
        # Files with city data (economic relationships)
        city_files = set([filename for filename, col in patterns['city_columns']])
        
        relationships = {
            'temporal_network': list(turn_files),
            'competitive_network': list(player_files),
            'economic_network': list(city_files),
            'core_junction': list(turn_files & player_files),  # Files with both turn and player
            'city_junction': list(turn_files & player_files & city_files)  # Full economic model
        }
        
        return relationships
    
    def analyze_file_categories(self, analysis_results):
        """Categorize files by their primary domain"""
        
        categories = {
            'core_stats': [],
            'ai_behavior': [],
            'military_combat': [],
            'diplomacy': [],
            'economy_trade': [],
            'culture_religion': [],
            'city_management': [],
            'game_systems': []
        }
        
        for filename, info in analysis_results.items():
            if 'error' in info:
                continue
                
            filename_lower = filename.lower()
            columns = [col.lower() for col in info.get('columns', [])]
            
            # Categorize based on filename and columns
            if 'player_stats' in filename_lower or 'playerscore' in filename_lower:
                categories['core_stats'].append(filename)
            elif filename_lower.startswith('ai_'):
                categories['ai_behavior'].append(filename)
            elif 'combat' in filename_lower or 'military' in filename_lower or 'barbarian' in filename_lower:
                categories['military_combat'].append(filename)
            elif 'diplomacy' in filename_lower:
                categories['diplomacy'].append(filename)
            elif 'trade' in filename_lower or 'economy' in filename_lower or any('gold' in col for col in columns):
                categories['economy_trade'].append(filename)
            elif 'cultural' in filename_lower or 'religion' in filename_lower or any('tourism' in col for col in columns):
                categories['culture_religion'].append(filename)
            elif 'city' in filename_lower or 'build' in filename_lower:
                categories['city_management'].append(filename)
            else:
                categories['game_systems'].append(filename)
        
        return categories
    
    def find_joinable_columns(self, analysis_results):
        """Find columns that can be used for joins between tables"""
        
        join_candidates = defaultdict(list)
        
        # Standard join patterns
        join_patterns = {
            'temporal': ['game turn', 'turn'],
            'player': ['player', 'civilization', 'civ'],
            'city': ['city', 'city name'],
            'unit': ['unit', 'unit type'],
            'tech': ['tech', 'technology'],
            'civic': ['civic', 'civics'],
            'building': ['building', 'structure'],
            'district': ['district'],
            'religion': ['religion', 'faith'],
            'resource': ['resource', 'strategic', 'luxury']
        }
        
        for filename, info in analysis_results.items():
            if 'error' in info:
                continue
                
            columns = info.get('columns', [])
            
            for col in columns:
                col_lower = col.strip().lower()
                
                for pattern_type, patterns in join_patterns.items():
                    for pattern in patterns:
                        if pattern in col_lower:
                            join_candidates[pattern_type].append({
                                'file': filename,
                                'column': col,
                                'sample_values': info.get('column_analysis', {}).get(col, {}).get('sample_values', [])
                            })
        
        return join_candidates
    
    def generate_sql_schemas(self, categories, join_candidates):
        """Generate SQL schema recommendations for each category"""
        
        schemas = {}
        
        # Core master tables
        schemas['core_tables'] = '''
-- Master player statistics table
CREATE TABLE player_stats (
    game_turn INTEGER,
    player_name VARCHAR(50),
    num_cities INTEGER,
    population INTEGER,
    techs INTEGER,
    civics INTEGER,
    yield_science INTEGER,
    yield_culture INTEGER,
    yield_production INTEGER,
    total_score INTEGER,
    PRIMARY KEY (game_turn, player_name)
);

-- Player scoring breakdown
CREATE TABLE player_scores (
    game_turn INTEGER,
    player_id INTEGER,
    total_score INTEGER,
    score_civics INTEGER,
    score_empire INTEGER,
    score_tech INTEGER,
    score_religion INTEGER,
    FOREIGN KEY (game_turn) REFERENCES player_stats(game_turn)
);
'''
        
        # AI behavior tables
        schemas['ai_tables'] = '''
-- AI decision tracking
CREATE TABLE ai_decisions (
    game_turn INTEGER,
    player_name VARCHAR(50),
    decision_type VARCHAR(100),
    decision_value VARCHAR(500),
    priority_score DECIMAL,
    FOREIGN KEY (game_turn, player_name) REFERENCES player_stats(game_turn, player_name)
);

-- AI military strategy
CREATE TABLE ai_military_strategy (
    game_turn INTEGER,
    player_name VARCHAR(50),
    strategy_type VARCHAR(100),
    target_player VARCHAR(50),
    unit_allocation JSON,
    FOREIGN KEY (game_turn, player_name) REFERENCES player_stats(game_turn, player_name)
);
'''
        
        # Economic and city tables
        schemas['economic_tables'] = '''
-- City management decisions
CREATE TABLE city_decisions (
    game_turn INTEGER,
    player_name VARCHAR(50),
    city_name VARCHAR(100),
    decision_type VARCHAR(100),
    production_item VARCHAR(100),
    priority_score DECIMAL,
    FOREIGN KEY (game_turn, player_name) REFERENCES player_stats(game_turn, player_name)
);

-- Trade and economic data
CREATE TABLE economic_state (
    game_turn INTEGER,
    player_name VARCHAR(50),
    gold_balance INTEGER,
    gold_per_turn INTEGER,
    trade_routes INTEGER,
    luxury_resources JSON,
    FOREIGN KEY (game_turn, player_name) REFERENCES player_stats(game_turn, player_name)
);
'''
        
        return schemas
    
    def create_analysis_report(self):
        """Generate comprehensive relationship analysis report"""
        
        print("🔍 Loading CSV analysis results...")
        analysis_results = self.load_analysis_results()
        
        if not analysis_results:
            return
        
        print("📊 Identifying common patterns...")
        patterns = self.identify_common_patterns(analysis_results)
        
        print("🔗 Creating relationship matrix...")
        relationships = self.create_relationship_matrix(patterns)
        
        print("📂 Categorizing files...")
        categories = self.analyze_file_categories(analysis_results)
        
        print("🔑 Finding joinable columns...")
        join_candidates = self.find_joinable_columns(analysis_results)
        
        print("🗃️ Generating SQL schemas...")
        schemas = self.generate_sql_schemas(categories, join_candidates)
        
        # Generate detailed report
        report = self.generate_detailed_report(patterns, relationships, categories, join_candidates, schemas)
        
        # Save report
        timestamp = "20250803_relationships"
        report_filename = f"csv_relationships_{timestamp}.md"
        
        with open(report_filename, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"✅ Relationship analysis complete! Report saved to: {report_filename}")
        
        return {
            'patterns': patterns,
            'relationships': relationships,
            'categories': categories,
            'join_candidates': join_candidates,
            'schemas': schemas
        }
    
    def generate_detailed_report(self, patterns, relationships, categories, join_candidates, schemas):
        """Generate the detailed markdown report"""
        
        report = f"""# 🔗 Civ VI CSV Relationship Analysis Report

**Generated:** {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}
**Total Files Analyzed:** {len([f for f in categories.values() for files in f for f in files])}

---

## 📊 File Categorization

### 🏆 Core Statistics Files ({len(categories['core_stats'])})
{self._format_file_list(categories['core_stats'])}

### 🤖 AI Behavior Files ({len(categories['ai_behavior'])})
{self._format_file_list(categories['ai_behavior'])}

### ⚔️ Military & Combat Files ({len(categories['military_combat'])})
{self._format_file_list(categories['military_combat'])}

### 🤝 Diplomacy Files ({len(categories['diplomacy'])})
{self._format_file_list(categories['diplomacy'])}

### 🏙️ City Management Files ({len(categories['city_management'])})
{self._format_file_list(categories['city_management'])}

### 🎭 Culture & Religion Files ({len(categories['culture_religion'])})
{self._format_file_list(categories['culture_religion'])}

### 🎮 Game Systems Files ({len(categories['game_systems'])})
{self._format_file_list(categories['game_systems'])}

---

## 🔗 Relationship Networks

### ⏰ Temporal Network (Turn-based analysis)
**Files with Game Turn data:** {len(relationships['temporal_network'])}
{self._format_file_list(relationships['temporal_network'])}

### 🏛️ Competitive Network (Player-based analysis)  
**Files with Player data:** {len(relationships['competitive_network'])}
{self._format_file_list(relationships['competitive_network'])}

### 🏗️ Core Junction (Turn + Player)
**Files with both Turn and Player data:** {len(relationships['core_junction'])}
{self._format_file_list(relationships['core_junction'])}

---

## 🔑 Join Key Analysis

### 🕐 Temporal Keys (Game Turn)
**Files:** {len(patterns['turn_columns'])}
```
{self._format_join_details(patterns['turn_columns'])}
```

### 👑 Player Keys  
**Files:** {len(patterns['player_columns'])}
```
{self._format_join_details(patterns['player_columns'])}
```

### 🏘️ City Keys
**Files:** {len(patterns['city_columns'])}
```
{self._format_join_details(patterns['city_columns'])}
```

---

## 💾 Recommended Database Schema

{schemas.get('core_tables', '')}

{schemas.get('ai_tables', '')}

{schemas.get('economic_tables', '')}

---

## 🎯 ML Analysis Opportunities

### Victory Prediction Models
- **Data Sources:** {', '.join(relationships['core_junction'][:5])}...
- **Key Features:** Science yields, Culture yields, Military units, Diplomacy scores
- **Prediction Target:** Victory type and timing

### Strategic Decision Analysis  
- **Data Sources:** {', '.join(categories['ai_behavior'][:3])}...
- **Key Features:** AI decision patterns, Resource allocation, Priority scoring
- **Analysis Target:** Optimal strategy identification

### Economic Modeling
- **Data Sources:** {', '.join(categories['city_management'] + categories['economy_trade'])}
- **Key Features:** City production, Trade routes, Resource management
- **Modeling Target:** Economic efficiency optimization

---

## 🚀 Implementation Priority

### Phase 1: Core Data Pipeline
1. Load core statistics files ({len(categories['core_stats'])} files)
2. Establish temporal and player relationships
3. Create unified player progression dataset

### Phase 2: AI Behavior Integration
1. Process AI decision files ({len(categories['ai_behavior'])} files)  
2. Link decisions to outcomes
3. Build decision effectiveness models

### Phase 3: Advanced Analytics
1. Integrate all domain-specific files
2. Create comprehensive game state representation
3. Build predictive models for all victory types

---

**🎮 Result: Complete relational framework for Civilization VI game intelligence and ML analysis!**
"""
        
        return report
    
    def _format_file_list(self, files):
        """Format a list of files for markdown"""
        if not files:
            return "- *None*"
        return '\n'.join([f"- `{file}`" for file in files])
    
    def _format_join_details(self, join_data):
        """Format join column details"""
        if not join_data:
            return "No temporal keys found"
        
        formatted = []
        for filename, column in join_data[:10]:  # Limit to first 10
            formatted.append(f"{filename}: '{column}'")
        
        if len(join_data) > 10:
            formatted.append(f"... and {len(join_data) - 10} more files")
        
        return '\n'.join(formatted)

def main():
    print("🔍 Starting CSV relationship analysis...")
    
    analyzer = CivRelationshipAnalyzer()
    results = analyzer.create_analysis_report()
    
    if results:
        print("\n📊 Analysis Summary:")
        print(f"- Temporal network: {len(results['relationships']['temporal_network'])} files")
        print(f"- Competitive network: {len(results['relationships']['competitive_network'])} files") 
        print(f"- Core junction: {len(results['relationships']['core_junction'])} files")
        print(f"- Join candidates identified: {len(results['join_candidates'])} types")
    
    print("\n✅ Relationship analysis complete!")

if __name__ == "__main__":
    main()
