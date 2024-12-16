# ETL Project
This project extracts data from a CSV file, transforms it 
using PySpark, and loads it into a PostgreSQL database. 
It then provides several SQL queries to perform on the resulting data. 

# How to Run
1. Build and start the containers:
   docker-compose build
   docker-compose up

2. Verify the ETL process:  
   docker-compose logs spark-etl

3. Access the PostgreSQL database:  
   Connect to the PostgreSQL database using:
   docker-compose exec db psql -U postgres -d mydb

4. Manually create the table (if required):
   \i /app/sql/create_table.sql

5. Use queries from file
   queries.sql

P.S. First load can be long, cause load unused dependencies not enough time