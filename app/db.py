from cassandra.cluster import Cluster
import json
import uuid
from app import setup_cassandra

def insert_data(country,city,temperature,weather):
    cluster = Cluster(['cassandra'])
    session = cluster.connect('weather')

    # Generate a unique ID for each data entry
    data_id = uuid.uuid4()

    # Insert data into the Cassandra table
    session.execute(
        """
        INSERT INTO weather_data (id,country,city,temperature,weather)
        VALUES (%s, %s , %s, %s , %s)
        """,
        (data_id, country ,city ,temperature , weather)
    )

    cluster.shutdown()
