"""
Script to import CSV data into the database
"""
import csv
import sqlite3

def import_csv_to_db(csv_file, table_name):
    """
    Imports data from CSV to database table
    
    Args:
        csv_file (str): Path to CSV file
        table_name (str): Target table name
    """
    conn = sqlite3.connect('python_database.db')
    cursor = conn.cursor()
    
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader)
        
        # Creates placeholder string for values
        placeholders = ', '.join(['?'] * len(headers))
        
        # Inserts data
        for row in reader:
            cursor.execute(f"INSERT INTO {table_name} VALUES ({placeholders})", row)
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    # Example usage:
    # import_csv_to_db('data/Departments.csv', 'Departments')
    pass
