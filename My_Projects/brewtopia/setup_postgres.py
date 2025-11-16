#!/usr/bin/env python3
"""
PostgreSQL Setup Script for Brewtopia
This script helps you set up PostgreSQL database for the Brewtopia application.
"""

import os
import subprocess
import sys
from dotenv import load_dotenv

load_dotenv()

def run_command(command, description):
    """Run a shell command and handle errors."""
    print(f"\n[*] {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"[+] {description} completed successfully!")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"[-] Error during {description}:")
        print(f"Command: {e.cmd}")
        print(f"Error: {e.stderr}")
        return None

def check_postgres_installation():
    """Check if PostgreSQL is installed."""
    print("\n[*] Checking PostgreSQL installation...")

    # Check if psql command exists
    result = run_command("psql --version", "Checking PostgreSQL client")
    if result is None:
        print("\n[-] PostgreSQL is not installed or not in PATH.")
        print("\n[*] Please install PostgreSQL:")
        print("   - Windows: Download from https://www.postgresql.org/download/windows/")
        print("   - macOS: brew install postgresql")
        print("   - Ubuntu/Debian: sudo apt-get install postgresql postgresql-contrib")
        print("   - CentOS/RHEL: sudo yum install postgresql-server postgresql-contrib")
        return False

    print(f"[+] PostgreSQL found: {result.strip()}")
    return True

def create_database():
    """Create the PostgreSQL database and user."""
    db_url = os.getenv('DATABASE_URL')
    if not db_url:
        print("[-] DATABASE_URL not found in .env file")
        return False

    # Parse the database URL
    # Format: postgresql://username:password@host:port/database
    try:
        # For local development, we'll create the database
        print("\n[*] Setting up database...")

        # Connect to default postgres database to create our database
        commands = [
            'psql -U postgres -c "CREATE DATABASE brewtopia_db;"',
            'psql -U postgres -c "CREATE USER brewtopia_user WITH PASSWORD \'your_password\';"',
            'psql -U postgres -c "GRANT ALL PRIVILEGES ON DATABASE brewtopia_db TO brewtopia_user;"',
        ]

        for cmd in commands:
            result = run_command(cmd, f"Running: {cmd}")
            if result is None:
                print("[!] Command failed, but continuing...")

        print("[+] Database setup completed!")
        print("\n[*] Note: If you get authentication errors, you may need to:")
        print("   1. Set a password for the postgres user")
        print("   2. Or run this script as the postgres user: sudo -u postgres ./setup_postgres.py")
        print("   3. Or use a different database URL in your .env file")

        return True

    except Exception as e:
        print(f"[-] Error setting up database: {e}")
        return False

def test_connection():
    """Test the database connection."""
    print("\n[*] Testing database connection...")

    try:
        from app import db, app
        with app.app_context():
            # Try to create tables
            db.create_all()
            print("[+] Database connection successful!")
            print("[+] Tables created successfully!")
            return True
    except Exception as e:
        print(f"[-] Database connection failed: {e}")
        print("\n[*] Troubleshooting:")
        print("   1. Make sure PostgreSQL is running")
        print("   2. Check your DATABASE_URL in .env file")
        print("   3. Ensure the database and user exist")
        print("   4. Try: sudo systemctl start postgresql (Linux)")
        print("   5. Try: brew services start postgresql (macOS)")
        return False

def main():
    """Main setup function."""
    print("Brewtopia PostgreSQL Setup")
    print("=" * 40)

    if not check_postgres_installation():
        sys.exit(1)

    if not create_database():
        print("\n[!] Database creation had issues, but let's test the connection anyway...")

    if test_connection():
        print("\n[+] Setup completed successfully!")
        print("\n[*] You can now run your Flask application:")
        print("   python app.py")
        print("\n[*] Access your app at: http://127.0.0.1:3000/")
    else:
        print("\n[-] Setup failed. Please check the error messages above.")
        sys.exit(1)

if __name__ == "__main__":
    main()