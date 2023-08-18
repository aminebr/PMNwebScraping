import time
from cassandra.cluster import Cluster

MAX_RETRIES = 10
RETRY_INTERVAL = 10  # seconds

def connect_to_cassandra():
    for _ in range(MAX_RETRIES):
        try:
            cluster = Cluster(['cassandra'])
            session = cluster.connect()
            return cluster,session
        except Exception as e:
            print(f"Failed to connect to Cassandra: {e}")
            print(f"Retrying in {RETRY_INTERVAL} seconds...")
            time.sleep(RETRY_INTERVAL)
    raise RuntimeError("Failed to connect to Cassandra after multiple retries.")


cluster,session = connect_to_cassandra()

print(f"Successfully connected to Cassandra")
# Create the keyspace
session.execute("CREATE KEYSPACE IF NOT EXISTS weather WITH replication = {'class':'SimpleStrategy', 'replication_factor':1}")

# Use the keyspace
session.set_keyspace('weather')

# Create the table
session.execute(
    """
    CREATE TABLE IF NOT EXISTS weather.weather_data (
        id UUID PRIMARY KEY,
        country text,
        city text,
        temperature text,
        weather text,
    )
    """
)

cluster.shutdown()