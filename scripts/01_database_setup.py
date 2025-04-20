"""
Script for SQLite database and tables creation
"""
import sqlite3

def create_database():
    """Creates the database and all necessary tables"""
    conn = sqlite3.connect('python_database.db')
    cursor = conn.cursor()
    
    # Table creation (example)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Departments (
        department_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
    ''')
    
    # Add other tables here...
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
    print("Database created successfully!")
