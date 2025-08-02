#!/usr/bin/env python3
"""
Setup database connection in Superset for Civ VI data
"""

import requests
import json

def setup_database_connection():
    print("🔧 Setting up PostgreSQL database connection in Superset...")
    
    # Login to Superset
    session = requests.Session()
    login_data = {"username": "admin", "password": "admin", "provider": "db"}
    login_response = session.post("http://localhost:8088/api/v1/security/login", json=login_data)
    login_response.raise_for_status()
    
    access_token = login_response.json()["access_token"]
    session.headers.update({"Authorization": f"Bearer {access_token}"})
    
    # Check existing databases
    response = session.get("http://localhost:8088/api/v1/database/")
    response.raise_for_status()
    databases = response.json()["result"]
    
    print("Current databases:")
    for db in databases:
        print(f"- {db['database_name']}: {db['sqlalchemy_uri']}")
    
    # Check if our database already exists
    for db in databases:
        if "civ6" in db["database_name"].lower() or "postgresql" in db["sqlalchemy_uri"]:
            print(f"✅ Found existing database: {db['database_name']} (ID: {db['id']})")
            return db["id"]
    
    # Create new database connection
    print("🏗️ Creating new PostgreSQL database connection...")
    database_data = {
        "database_name": "Civ VI Analytics",
        "sqlalchemy_uri": "postgresql://civ6_user:civ6_password@localhost:5432/civ6_analytics",
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
    
    response = session.post("http://localhost:8088/api/v1/database/", json=database_data)
    response.raise_for_status()
    
    database_id = response.json()["id"]
    print(f"✅ Created database connection (ID: {database_id})")
    
    # Test the connection
    test_response = session.post(f"http://localhost:8088/api/v1/database/{database_id}/validate_parameters")
    if test_response.status_code == 200:
        print("✅ Database connection test successful!")
    else:
        print("⚠️ Database connection test failed, but connection was created")
    
    return database_id

if __name__ == "__main__":
    try:
        db_id = setup_database_connection()
        print(f"\n🎉 Database setup complete! Database ID: {db_id}")
    except Exception as e:
        print(f"❌ Error setting up database: {e}")
        import traceback
        traceback.print_exc()
