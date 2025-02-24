# csv_to_postgres
This project has a folder where you can put csv files and convert it to a Postgres DB

Prerequisites:
- Docker
- Python

1. Make sure your Docker is running
2. Move your csv files to csv_files folder
3. Open your Terminal and navigate to the project
4. Run `python3 ddl_generator.py`
5. Check init.sql file and modify the DDL if needed
6. Run `docker compose up`
7. Open your db tool and connect to the DB with your data using the following credencials:
```   
   host: localhost
   port: 5432
   user: admin
   pass: admin
```
8. Enjoy your local db
