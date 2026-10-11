import sqlite3

conn = sqlite3.connect("marine_life.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS marine_observation (
    observation_id INTEGER PRIMARY KEY,
    animal_name TEXT NOT NULL,
    animal_group TEXT NOT NULL,
    habitat TEXT NOT NULL,
    depth_m INTEGER NOT NULL,
    estimated_weight_kg REAL NOT NULL
)
""")

cursor.execute("DELETE FROM marine_observation")

observations = [
    (1, "Blue Whale", "Mammal", "Open Ocean", 30, 120000.0),
    (2, "Bottlenose Dolphin", "Mammal", "Open Ocean", 15, 250.0),
    (3, "Green Sea Turtle", "Reptile", "Coral Reef", 10, 160.0),
    (4, "Clownfish", "Fish", "Coral Reef", 5, 0.3),
    (5, "Hammerhead Shark", "Fish", "Open Ocean", 70, 230.0),
    (6, "Giant Octopus", "Mollusc", "Seabed", 40, 25.0),
    (7, "Manta Ray", "Fish", "Open Ocean", 25, 1350.0),
    (8, "Starfish", "Echinoderm", "Seabed", 20, 0.5)
]

import sqlite3

conn = sqlite3.connect("marine_life.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS marine_observation (
    observation_id INTEGER PRIMARY KEY,
    animal_name TEXT NOT NULL,
    animal_group TEXT NOT NULL,
    habitat TEXT NOT NULL,
    depth_m INTEGER NOT NULL,
    estimated_weight_kg REAL NOT NULL
)
""")

cursor.execute("DELETE FROM marine_observation")

observations = [
    (1, "Blue Whale", "Mammal", "Open Ocean", 30, 120000.0),
    (2, "Bottlenose Dolphin", "Mammal", "Open Ocean", 15, 250.0),
    (3, "Green Sea Turtle", "Reptile", "Coral Reef", 10, 160.0),
    (4, "Clownfish", "Fish", "Coral Reef", 5, 0.3),
    (5, "Hammerhead Shark", "Fish", "Open Ocean", 70, 230.0),
    (6, "Giant Octopus", "Mollusc", "Seabed", 40, 25.0),
    (7, "Manta Ray", "Fish", "Open Ocean", 25, 1350.0),
    (8, "Starfish", "Echinoderm", "Seabed", 20, 0.5)
]

cursor.executemany("""
INSERT INTO marine_observation
VALUES (?, ?, ?, ?, ?, ?)
""", observations)

cursor.execute("SELECT * FROM marine_observation")
print("All Observations:")
for row in cursor.fetchall():
    print(row)

cursor.execute("SELECT animal_group FROM marine_observation")
print("\nAll Animal Groups:")
for row in cursor.fetchall():
    print(row)

cursor.execute("SELECT DISTINCT animal_group FROM marine_observation")
print("\nUnique Animal Groups:")
for row in cursor.fetchall():
    print(row)

cursor.execute("""
SELECT COUNT(DISTINCT animal_group)
FROM marine_observation
""")
print("\nUnique Animal Groups Count:", cursor.fetchone()[0])

cursor.execute("""
SELECT COUNT(observation_id)
FROM marine_observation
""")
print("\nTotal Observations:", cursor.fetchone()[0])

cursor.execute("""
SELECT COUNT(observation_id)
FROM marine_observation
WHERE habitat = 'Open Ocean'
""")
print("\nOpen Ocean Observations:", cursor.fetchone()[0])

cursor.execute("""
SELECT SUM(estimated_weight_kg)
FROM marine_observation
""")
print("\nTotal Estimated Weight (kg):", cursor.fetchone()[0])

cursor.execute("""
SELECT AVG(depth_m)
FROM marine_observation
""")
print("\nAverage Observation Depth (m):", cursor.fetchone()[0])

cursor.execute("""
SELECT
    COUNT(observation_id),
    COUNT(DISTINCT animal_group),
    SUM(estimated_weight_kg),
    AVG(depth_m)
FROM marine_observation
""")

print("\nCombined Aggregate Results:")
print(cursor.fetchone())

conn.commit()
conn.close()