#!/bin/bash

# Wait until PostgreSQL is ready
until pg_isready -h db -U admin; do
  echo "Waiting for database connection..."
  sleep 2
done

# Load each CSV file into its corresponding table
for file in /csv_files/*.csv; do
  table_name=$(basename "$file" .csv)  # Get table name from the file name
  echo "Loading data from $file into table \"$table_name\"..."

  # Ensure table name with spaces is quoted in the SQL command
  psql -h db -U admin -d postgres -c "\COPY \"$table_name\" FROM '$file' DELIMITER ',' CSV HEADER;"
done

echo "Data loading completed."
