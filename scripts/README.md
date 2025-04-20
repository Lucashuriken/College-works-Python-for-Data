# Database Project with Python

**Student:** Lucas Sousa  
**Email:** lucas.hsousa@al.infnet.edu.br  

## Description
This project demonstrates SQLite database manipulation with Python, including:
- Database creation
- CSV data import
- Complex queries
- JSON export for Looker Studio analysis

## Project Structure
- `data/`: Original CSV files
- `scripts/`: Python scripts for database manipulation
- `outputs/`: JSON results for analysis

## Implemented Queries
1. Average salary by department (completed projects)
2. Most used material resources
3. Total project cost by department
4. Active projects with details
5. Project with most dependents involved

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run scripts in order:
   ```bash
   python scripts/01_database_setup.py
   python scripts/02_data_import.py
   python scripts/03_queries.py
   python scripts/04_json_converter.py
