from pathlib import Path
import csv
import json
import sqlite3

CWD = Path.cwd()
DISABILITY_SENATORS_FILE = CWD / Path('./data/disability-senators.csv')
DB_SCHEMA = CWD / Path('schema.sql')
DISABILITY_SENATORS_JSON_OUTPUT = CWD / Path('diability_senators.json')
conn = sqlite3.connect('disability_senators.db')
c = conn.cursor()

def generate_disability_senator_database(data):
  with DB_SCHEMA.open() as schema:
    schema = schema.read()
    c.executescript(schema)

  for row in data:
    c.execute('INSERT INTO disability_senators VALUES (?, ?, ?)', (row['SER'], row['Name'], row['Gender']))
  conn.commit()

def generate_disability_senator_json(data):
  rec = []
  for row in data:
    rec.append({'SER': row["SER"], 'name': row["Name"], 'gender': row["Gender"]})
  DISABILITY_SENATORS_JSON_OUTPUT.write_text(json.dumps(rec))
    
if __name__ == '__main__':
  with DISABILITY_SENATORS_FILE.open() as csvfile:
    senator_reader = csv.DictReader(csvfile)
    generate_disability_senator_json(senator_reader)
    generate_disability_senator_database(senator_reader)
  exit(0)
