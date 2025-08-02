#!/usr/bin/env python3
"""
Create the civ_game_data dataset in Superset
"""

import requests
import json

def create_dataset():
    """Create the civ_game_data dataset"""
    print("📊 Creating civ_game_data dataset in Superset...")
    
    # Login to Superset
    session = requests.Session()
    
    try:
        # Login
        login_data = {"username": "admin", "password": "admin", "provider": "db"}
        login_response = session.post("http://localhost:8088/api/v1/security/login", json=login_data)
        login_response.raise_for_status()
        
        access_token = login_response.json()["access_token"]
        session.headers.update({"Authorization": f"Bearer {access_token}"})
        print("✅ Login successful")
        
        # Check if dataset already exists
        print("🔍 Checking existing datasets...")
        response = session.get("http://localhost:8088/api/v1/dataset/")
        response.raise_for_status()
        datasets = response.json()["result"]
        
        for dataset in datasets:
            if dataset["table_name"] == "civ_game_data":
                print(f"✅ Dataset already exists (ID: {dataset['id']})")
                return dataset["id"]
        
        # Create new dataset
        print("🏗️ Creating civ_game_data dataset...")
        dataset_data = {
            "database": 1,  # The database ID we just created
            "schema": "public",
            "table_name": "civ_game_data"
        }
        
        response = session.post("http://localhost:8088/api/v1/dataset/", json=dataset_data)
        
        if response.status_code == 422:
            print("⚠️ Dataset creation validation error:")
            print(response.text)
            return None
            
        response.raise_for_status()
        dataset_id = response.json()["id"]
        print(f"✅ Created dataset (ID: {dataset_id})")
        
        # Get dataset details to verify
        details_response = session.get(f"http://localhost:8088/api/v1/dataset/{dataset_id}")
        if details_response.status_code == 200:
            details = details_response.json()["result"]
            print(f"📋 Dataset details:")
            print(f"   - Table: {details['table_name']}")
            print(f"   - Schema: {details['schema']}")
            print(f"   - Columns: {len(details.get('columns', []))} columns found")
            
            # Show some column names
            columns = details.get('columns', [])
            if columns:
                col_names = [col['column_name'] for col in columns[:5]]
                print(f"   - Sample columns: {', '.join(col_names)}")
        
        return dataset_id
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

def main():
    print("🏆 Civ VI Dataset Creation")
    print("=" * 30)
    
    dataset_id = create_dataset()
    
    if dataset_id:
        print(f"\n✅ Dataset creation completed!")
        print(f"🎯 Dataset ID: {dataset_id}")
        print(f"🔗 Create charts at: http://localhost:8088/explore/?datasource_type=table&datasource_id={dataset_id}")
        print(f"📊 Or go to Datasets: http://localhost:8088/dataset/list/")
    else:
        print(f"\n❌ Dataset creation failed!")

if __name__ == "__main__":
    main()
