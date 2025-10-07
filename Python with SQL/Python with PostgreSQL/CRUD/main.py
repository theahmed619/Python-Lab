import psycopg2

hostname = "localhost"
database = "demo"
username = "postgres"
password = "root"
port_id = 5432

try:
    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=password,
        port=port_id
    )
    print(conn, "connection established")

except Exception as error:
    print("Connection failed:", error)

finally:
    # Close only if connection was established
    if 'conn' in locals() and conn:
        conn.close()
