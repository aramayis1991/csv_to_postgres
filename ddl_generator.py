import os
import pandas as pd

def infer_sql_type(dtype):
    """Infer SQL data type based on pandas data type."""
    if pd.api.types.is_integer_dtype(dtype):
        return "INTEGER"
    elif pd.api.types.is_float_dtype(dtype):
        return "REAL"
    elif pd.api.types.is_bool_dtype(dtype):
        return "BOOLEAN"
    elif pd.api.types.is_datetime64_any_dtype(dtype):
        return "TIMESTAMP"
    else:
        return "TEXT"

def generate_ddl_for_csv(file_path, table_name):
    """Generate DDL for a single CSV file."""
    df = pd.read_csv(file_path, nrows=100)  # Read a sample of 100 rows to infer schema

    columns = []
    for col in df.columns:
        sql_type = infer_sql_type(df[col].dtype)
        columns.append(f"\"{col}\" {sql_type}")

    ddl = f"CREATE TABLE \"{table_name}\" (\n" + \
          ",\n    ".join(columns) + \
          "\n);"
    return ddl

def generate_ddl_for_folder(folder_path):
    """Generate DDL statements for all CSV files in a folder."""
    ddl_statements = []

    for file_name in os.listdir(folder_path):
        if file_name.endswith('.csv'):
            table_name = os.path.splitext(file_name)[0]
            file_path = os.path.join(folder_path, file_name)
            ddl = generate_ddl_for_csv(file_path, table_name)
            ddl_statements.append(ddl)

    return ddl_statements

def save_ddl_to_file(ddl_statements, output_file):
    """Save generated DDL statements to a file."""
    with open(output_file, 'w') as f:
        f.write("\n\n".join(ddl_statements))

if __name__ == "__main__":
    folder_path = os.path.join(os.path.dirname(__file__), 'csv_files')
    output_file = os.path.join(os.path.dirname(__file__), 'init.sql')

    if not os.path.exists(folder_path):
        print(f"The folder '{folder_path}' does not exist. Please create it and add your CSV files.")
    else:
        ddl_statements = generate_ddl_for_folder(folder_path)
        save_ddl_to_file(ddl_statements, output_file)
        print(f"DDL statements have been saved to {output_file}")

