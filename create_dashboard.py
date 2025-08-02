#!/usr/bin/env python3
"""
Auto-create Civ VI Dashboard in Superset
This script programmatically creates the complete dashboard with all charts
"""

import requests
import json
import time
import sys

class SupersetDashboardCreator:
    def __init__(self, base_url="http://localhost:8088", username="admin", password="admin"):
        self.base_url = base_url
        self.username = username
        self.password = password
        self.session = requests.Session()
        self.csrf_token = None
        self.access_token = None
        
    def login(self):
        """Login to Superset and get authentication tokens"""
        print("🔐 Logging into Superset...")
        
        # Get CSRF token
        csrf_response = self.session.get(f"{self.base_url}/login/")
        csrf_response.raise_for_status()
        
        # Login
        login_data = {
            "username": self.username,
            "password": self.password,
            "provider": "db"
        }
        
        login_response = self.session.post(
            f"{self.base_url}/api/v1/security/login",
            json=login_data
        )
        login_response.raise_for_status()
        
        self.access_token = login_response.json()["access_token"]
        self.session.headers.update({"Authorization": f"Bearer {self.access_token}"})
        
        print("✅ Successfully logged into Superset")
        
    def get_database_id(self):
        """Get the database ID for our PostgreSQL connection"""
        print("🔍 Finding PostgreSQL database...")
        
        response = self.session.get(f"{self.base_url}/api/v1/database/")
        response.raise_for_status()
        
        databases = response.json()["result"]
        for db in databases:
            if "civ6" in db["database_name"].lower() or "postgresql" in db["sqlalchemy_uri"]:
                print(f"✅ Found database: {db['database_name']} (ID: {db['id']})")
                return db["id"]
                
        raise Exception("❌ Could not find PostgreSQL database")
        
    def create_dataset(self, database_id):
        """Create the civ_game_data dataset"""
        print("📊 Creating civ_game_data dataset...")
        
        dataset_data = {
            "database": database_id,
            "schema": "public",
            "table_name": "civ_game_data"
        }
        
        response = self.session.post(
            f"{self.base_url}/api/v1/dataset/",
            json=dataset_data
        )
        
        if response.status_code == 422:
            # Dataset might already exist
            print("ℹ️ Dataset might already exist, trying to find it...")
            datasets_response = self.session.get(f"{self.base_url}/api/v1/dataset/")
            datasets = datasets_response.json()["result"]
            
            for dataset in datasets:
                if dataset["table_name"] == "civ_game_data":
                    print(f"✅ Found existing dataset (ID: {dataset['id']})")
                    return dataset["id"]
        
        response.raise_for_status()
        dataset_id = response.json()["id"]
        print(f"✅ Created dataset (ID: {dataset_id})")
        return dataset_id
        
    def create_chart(self, dataset_id, chart_config):
        """Create a chart with the given configuration"""
        print(f"📈 Creating chart: {chart_config['slice_name']}")
        
        chart_data = {
            "datasource_id": dataset_id,
            "datasource_type": "table",
            "slice_name": chart_config["slice_name"],
            "viz_type": chart_config["viz_type"],
            "params": json.dumps(chart_config["params"])
        }
        
        response = self.session.post(
            f"{self.base_url}/api/v1/chart/",
            json=chart_data
        )
        response.raise_for_status()
        
        chart_id = response.json()["id"]
        print(f"✅ Created chart: {chart_config['slice_name']} (ID: {chart_id})")
        return chart_id
        
    def create_dashboard(self, chart_ids):
        """Create the main dashboard with all charts"""
        print("🏆 Creating Civ VI Analytics Dashboard...")
        
        dashboard_data = {
            "dashboard_title": "🏆 Civ VI Race Analytics",
            "slug": "civ6-race-analytics",
            "position_json": json.dumps(self.generate_dashboard_layout(chart_ids)),
            "css": """
                .dashboard-header {
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                }
                .chart-container {
                    border-radius: 8px;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                }
            """,
            "json_metadata": json.dumps({
                "timed_refresh_immune_slices": [],
                "expanded_slices": {},
                "refresh_frequency": 0,
                "default_filters": {},
                "color_scheme": "supersetColors"
            }),
            "slices": chart_ids
        }
        
        response = self.session.post(
            f"{self.base_url}/api/v1/dashboard/",
            json=dashboard_data
        )
        response.raise_for_status()
        
        dashboard_id = response.json()["id"]
        print(f"✅ Created dashboard (ID: {dashboard_id})")
        return dashboard_id
        
    def generate_dashboard_layout(self, chart_ids):
        """Generate the dashboard layout configuration"""
        return {
            "DASHBOARD_VERSION_KEY": "v2",
            "ROOT_ID": {
                "children": ["GRID_ID"],
                "id": "ROOT_ID",
                "type": "ROOT"
            },
            "GRID_ID": {
                "children": [f"ROW-{i}" for i in range(len(chart_ids))],
                "id": "GRID_ID",
                "type": "GRID"
            },
            **{
                f"ROW-{i}": {
                    "children": [f"CHART-{chart_id}"],
                    "id": f"ROW-{i}",
                    "meta": {"background": "BACKGROUND_TRANSPARENT"},
                    "type": "ROW"
                } for i, chart_id in enumerate(chart_ids)
            },
            **{
                f"CHART-{chart_id}": {
                    "children": [],
                    "id": f"CHART-{chart_id}",
                    "meta": {
                        "chartId": chart_id,
                        "height": 400,
                        "sliceName": f"Chart {chart_id}",
                        "width": 12
                    },
                    "type": "CHART"
                } for chart_id in chart_ids
            }
        }
        
    def create_complete_dashboard(self):
        """Create the complete Civ VI dashboard with all charts"""
        try:
            self.login()
            database_id = self.get_database_id()
            dataset_id = self.create_dataset(database_id)
            
            # Chart configurations
            charts_config = [
                {
                    "slice_name": "🏆 Civilization Race - Score Timeline",
                    "viz_type": "line",
                    "params": {
                        "metrics": ["total_score"],
                        "groupby": ["civilization"],
                        "granularity_sqla": "game_turn",
                        "time_range": "No filter",
                        "adhoc_filters": [],
                        "row_limit": 1000,
                        "order_desc": True,
                        "show_markers": True,
                        "line_interpolation": "linear",
                        "color_scheme": "supersetColors"
                    }
                },
                {
                    "slice_name": "🔬 Science Race Timeline", 
                    "viz_type": "line",
                    "params": {
                        "metrics": ["yields_science"],
                        "groupby": ["civilization"],
                        "granularity_sqla": "game_turn",
                        "time_range": "No filter",
                        "adhoc_filters": [],
                        "row_limit": 1000,
                        "show_markers": True,
                        "line_interpolation": "linear",
                        "color_scheme": "bnbColors"
                    }
                },
                {
                    "slice_name": "🎭 Culture Race Timeline",
                    "viz_type": "line", 
                    "params": {
                        "metrics": ["yields_culture"],
                        "groupby": ["civilization"],
                        "granularity_sqla": "game_turn",
                        "time_range": "No filter",
                        "adhoc_filters": [],
                        "row_limit": 1000,
                        "show_markers": True,
                        "line_interpolation": "linear",
                        "color_scheme": "lyftColors"
                    }
                },
                {
                    "slice_name": "📊 Current Turn Leaderboard",
                    "viz_type": "table",
                    "params": {
                        "metrics": ["total_score", "yields_science", "yields_culture", "population", "num_cities"],
                        "groupby": ["civilization"],
                        "adhoc_filters": [
                            {
                                "clause": "WHERE",
                                "subject": "game_turn",
                                "operator": "==",
                                "comparator": "(SELECT MAX(game_turn) FROM civ_game_data)"
                            }
                        ],
                        "row_limit": 10,
                        "order_desc": True,
                        "order_by_cols": ["total_score"],
                        "table_timestamp_format": "%Y-%m-%d %H:%M:%S"
                    }
                }
            ]
            
            # Create all charts
            chart_ids = []
            for chart_config in charts_config:
                chart_id = self.create_chart(dataset_id, chart_config)
                chart_ids.append(chart_id)
                time.sleep(1)  # Rate limiting
                
            # Create dashboard
            dashboard_id = self.create_dashboard(chart_ids)
            
            dashboard_url = f"{self.base_url}/superset/dashboard/{dashboard_id}/"
            print(f"\n🎉 SUCCESS! Civ VI Dashboard created!")
            print(f"🔗 Dashboard URL: {dashboard_url}")
            print(f"🎯 Dashboard shows your {len(chart_ids)} charts with race analysis")
            
            return dashboard_id, dashboard_url
            
        except Exception as e:
            print(f"❌ Error creating dashboard: {e}")
            import traceback
            traceback.print_exc()
            return None, None

def main():
    print("🏆 Civ VI Dashboard Auto-Creator")
    print("=" * 50)
    
    creator = SupersetDashboardCreator()
    dashboard_id, dashboard_url = creator.create_complete_dashboard()
    
    if dashboard_id:
        print(f"\n✅ Dashboard creation completed successfully!")
        print(f"🎮 Your Civ VI race analysis is ready at: {dashboard_url}")
    else:
        print(f"\n❌ Dashboard creation failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()
