"""
Converts query results to JSON for Looker Studio
"""
import json
from datetime import datetime
from .queries import get_avg_salary_by_dept  # Imports query functions

def save_to_json(data, filename):
    """
    Saves data in JSON format
    
    Args:
        data: Data to be saved
        filename (str): Output filename
    """
    # Converts datetime to string if needed
    def default_serializer(o):
        if isinstance(o, datetime):
            return o.isoformat()
        raise TypeError(f"Object of type {o.__class__.__name__} is not JSON serializable")
    
    with open(f'outputs/{filename}', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, default=default_serializer, ensure_ascii=False)

if __name__ == "__main__":
    # Example for query 01
    results = get_avg_salary_by_dept()
    data = [{
        "department": row[0],
        "average_salary": float(row[1]),
        "projects": row[2].split(', ')
    } for row in results]
    
    save_to_json(data, 'salary_average.json')
    print("JSON generated successfully!")
