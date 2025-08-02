#!/usr/bin/env python3
"""
Quick debug to see what's in turn 10
"""

import pandas as pd
import os

log_dir = r"C:\Users\rhode\AppData\Local\Firaxis Games\Sid Meier's Civilization VI\Logs"
df = pd.read_csv(os.path.join(log_dir, "Player_Stats.csv"))

print("🔍 Turn 10 Debug:")
turn10 = df[df['Game Turn'] == 10]
print(f"Records in turn 10: {len(turn10)}")

print("\nCivilizations in turn 10:")
for _, row in turn10.iterrows():
    player = row[' Player']
    print(f"  • '{player}'")

print("\nKnown major civs list:")
known_major_civs = [
    'CIVILIZATION_NETHERLANDS', 'CIVILIZATION_ROME', 'CIVILIZATION_CHINA',
    'CIVILIZATION_ENGLAND', 'CIVILIZATION_CANADA', 'CIVILIZATION_GAUL'
]
for civ in known_major_civs:
    print(f"  • '{civ}'")

print("\nMatches:")
civs_in_turn10 = turn10[' Player'].unique()
matches = [civ for civ in civs_in_turn10 if civ in known_major_civs]
print(f"Found {len(matches)} matches: {matches}")
