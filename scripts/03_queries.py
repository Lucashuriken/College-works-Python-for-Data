"""
Contains all SQL queries for the project
"""
import sqlite3

def get_avg_salary_by_dept():
    """
    Query 01: Average salary by department for completed projects
    Returns:
        list: Query results
    """
    conn = sqlite3.connect('python_database.db')
    cursor = conn.cursor()
    
    query = '''
    SELECT
        Departments.name,
        AVG(Employees.salary),
        GROUP_CONCAT(Projects.name, ', ')
    FROM Projects
    JOIN Employees ON Projects.responsible_employee_id = Employees.employee_id
    JOIN Departments ON Employees.department_id = Departments.department_id
    WHERE Projects.status = 'Completed'
    GROUP BY Departments.name;
    '''
    
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    
    return results

# Add other query functions here...

if __name__ == "__main__":
    # Execution example
    results = get_avg_salary_by_dept()
    for row in results:
        print(f"Department: {row[0]}")
        print(f"Average Salary: {row[1]:.2f}")
        print(f"Completed Projects: {row[2]}\n")
