import psycopg2
import time

def count_active_connections():
    conn = psycopg2.connect("dbname=postgres user=postgres")
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM pg_stat_activity WHERE state = 'active';")
    active_connections = cur.fetchone()[0]
    conn.close()
    return active_connections

def monitor_connections():
    while True:
        active_connections = count_active_connections()
        print(f"Número de conexões ativas: {active_connections}")
        time.sleep(1)  # Verifica a cada 5 segundos

if __name__ == "__main__":
    monitor_connections()
