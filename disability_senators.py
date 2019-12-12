from pathlib import Path
import csv
import json
import sqlite3


class DisabilitySenatorParser():
    def __init__(self, src):
        self.__results = []
        with open(src, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.__results.append(dict(row))
        self.__fieldnames = ['ser', 'name', 'gender']

    def toJSON(self, output_file):
        with open(output_file, 'w') as json_output:
            json.dump(self.__results, json_output)

    def toCSV(self, output_file):
        with open(output_file, 'w', newline='') as csvfile:
            csvwriter = csv.DictWriter(csvfile, fieldnames=self.__fieldnames)
            csvwriter.writeheader()
            csvwriter.writerows(self.__results)

    def toDB(self, schema_file, db_file, dump_file=None):
        conn = sqlite3.connect(db_file)
        c = conn.cursor()
        with open(schema_file, 'r') as schema:
            c.executescript(schema.read())
        for row in self.__results:
            value = (row[field] for field in self.__fieldnames)
            c.execute('INSERT INTO disability_senators VALUES (?,?,?)',
                      tuple(value))
        conn.commit()
        if dump_file is not None:
            with open(dump_file, 'w') as dump:
                for line in conn.iterdump():
                    dump.write(line)
        conn.close()


if __name__ == '__main__':
    CWD = Path.cwd()
    OUTDIR = CWD / Path('output')
    DATADIR = CWD / Path('./data')
    if OUTDIR.exists() is False:
        OUTDIR.mkdir()
    DISABILITY_SENATORS_FILE = DATADIR / Path('disability-senators.csv')
    dsp = DisabilitySenatorParser(DISABILITY_SENATORS_FILE)

    DISABILITY_SENATORS_JSON_OUTPUT = OUTDIR / Path('diability_senators.json')
    dsp.toJSON(DISABILITY_SENATORS_JSON_OUTPUT)

    DISABILITY_SENATORS_CSV_OUTPUT = OUTDIR / Path('disability_senators.csv')
    dsp.toCSV(DISABILITY_SENATORS_CSV_OUTPUT)
    DB_SCHEMA = CWD / DATADIR / Path('schemas/disability_senators.schema.sql')
    DB_FILE = OUTDIR / Path('disability_senators.db')
    DUMP_FILE = OUTDIR / Path('disability_senators.sql')
    dsp.toDB(DB_SCHEMA, DB_FILE, DUMP_FILE)
