#!/usr/bin/env python3
"""
Add PostgreSQL database connection to Superset
This fixes the "no schemas available" issue
"""

import requests
import json

def add_database_connection():
    """Add the PostgreSQL database connection to Superset"""
    print("🔧 Adding PostgreSQL database connection to Superset...")
    
    # Login to Superset
    session = requests.Session()
    
    try:
        # Login
        login_data = {
            "username": "admin", 
            "password": "admin", 
            "provider": "db"
        }
        
        print("🔐 Logging into Superset...")
        login_response = session.post(
            "http://localhost:8088/api/v1/security/login", 
            json=login_data
        )
        login_response.raise_for_status()
        
        access_token = login_response.json()["access_token"]
        session.headers.update({"Authorization": f"Bearer {access_token}"})
        print("✅ Login successful")
        
        # Check existing databases
        print("🔍 Checking existing databases...")
        response = session.get("http://localhost:8088/api/v1/database/")
        response.raise_for_status()
        databases = response.json()["result"]
        
        print("Current databases:")
        for db in databases:
            print(f"  - ID: {db['id']}, Name: {db['database_name']}")
            if "postgres" in db["sqlalchemy_uri"].lower() or "civ6" in db["database_name"].lower():
                print(f"    ✅ Found existing Civ VI database (ID: {db['id']})")
                return db["id"]
        
        # Create new database connection
        print("🏗️ Creating new PostgreSQL database connection...")
        database_data = {
            "database_name": "Civ VI Analytics",
            "sqlalchemy_uri": "postgresql://civ6_user:civ6_password@postgres:5432/civ6_analytics",
            "expose_in_sqllab": True,
            "allow_dml": False,
            "allow_file_upload": False,
            "extra": json.dumps({
                "metadata_params": {},
                "engine_params": {},
                "metadata_cache_timeout": {},
                "schemas_allowed_for_file_upload": []
            })
        }
        
        response = session.post(
            "http://localhost:8088/api/v1/database/", 
            json=database_data
        )
        
        if response.status_code == 422:
            print("⚠️ Database connection might already exist or there's a validation error")
            print(f"Response: {response.text}")
            return None
            
        response.raise_for_status()
        database_id = response.json()["id"]
        print(f"✅ Created database connection (ID: {database_id})")
        
        # Test the connection
        print("🧪 Testing database connection...")
        test_response = session.post(
            f"http://localhost:8088/api/v1/database/{database_id}/validate_parameters"
        )
        
        if test_response.status_code == 200:
            print("✅ Database connection test successful!")
        else:
            print(f"⚠️ Database connection test failed: {test_response.text}")
        
        # Get schemas to verify connection works
        print("📋 Fetching schemas...")
        schemas_response = session.get(
            f"http://localhost:8088/api/v1/database/{database_id}/schemas/"
        )
        
        if schemas_response.status_code == 200:
            schemas = schemas_response.json()["result"]
            print(f"✅ Found schemas: {schemas}")
        else:
            print(f"❌ Failed to fetch schemas: {schemas_response.text}")
        
        return database_id
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Network error: {e}")
        return None
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

def main():
    print("🏆 Civ VI Database Connection Setup")
    print("=" * 40)
    
    database_id = add_database_connection()
    
    if database_id:
        print(f"\n✅ Database connection setup completed!")
        print(f"🎯 Database ID: {database_id}")
        print(f"🔗 You can now create datasets from the 'civ_game_data' table")
        print(f"📊 Go to: http://localhost:8088/dataset/list/")
    else:
        print(f"\n❌ Database connection setup failed!")
        print(f"💡 Try manually adding it through the Superset UI:")
        print(f"   1. Go to Settings → Database Connections")
        print(f"   2. Click + Database")
        print(f"   3. Select PostgreSQL")
        print(f"   4. URI: postgresql://civ6_user:civ6_password@postgres:5432/civ6_analytics")

if __name__ == "__main__":
    main()
