import psycopg2
from datetime import datetime, timedelta

def delete_old_data():
    conn = psycopg2.connect(
        host="localhost",
        dbname="demo",
        user="postgres",
        password="root",
        port="5432"
    )
    cursor = conn.cursor()

    cutoff_date = datetime.now() - timedelta(days=90)

    cursor.execute("""
    SELECT id FROM snapshot
    WHERE timestamp <= %s
    ORDER BY timestamp DESC
""", (cutoff_date,))

    result = cursor.fetchone()

    snapshot_id = result[0] if result else None
    print("Snapshot ID:", snapshot_id)

    if snapshot_id:
        cursor.execute("DELETE FROM users WHERE snapshotid < %s", (snapshot_id,))
        cursor.execute("DELETE FROM snapshot WHERE id < %s", (snapshot_id,))
        conn.commit()  # Commit deletion

        # Now VACUUM FULL outside of transaction
        conn.autocommit = True
        cursor.execute("VACUUM FULL snapshot")
        cursor.execute("VACUUM FULL users")
        print("VACUUM FULL done.")

    cursor.close()
    conn.close()

delete_old_data()
