from pathlib import Path
import csv
import json
import sqlite3


class ElectParser():
    def __init__(self, label):
        self._fieldnames = []
        self._elects = []
        self._label = label

    def toJSON(self, output_file):
        with open(output_file, 'w') as json_output:
            json.dump(self._elects, json_output)

    def toCSV(self, output_file):
        with open(output_file, 'w', newline='') as csvfile:
            csvwriter = csv.DictWriter(csvfile, fieldnames=self._fieldnames)
            csvwriter.writeheader()
            csvwriter.writerows(self._elects)

    def toDB(self, schema_file, db_file, dump_file=None):
        conn = sqlite3.connect(db_file)
        c = conn.cursor()
        v = str(tuple(('?' for i in self._fieldnames))).replace('\'', '')
        insert_q = f"INSERT INTO {self._label} VALUES {v}"
        with open(schema_file, 'r') as schema:
            c.executescript(schema.read())
        for row in self._elects:
            value = (row[field] for field in self._fieldnames)
            c.execute(insert_q, tuple(value))
        conn.commit()
        if dump_file is not None:
            with open(dump_file, 'w') as dump:
                for line in conn.iterdump():
                    dump.write(line)
        conn.close()

    def toAll(self, default_dest_dir: Path, **kwargs):
        if "csv_dest" in kwargs:
            self.toCSV(kwargs["csv_dest"])
        else:
            self.toCSV(default_dest_dir / Path(f"{self._label}.csv"))

        if "json_dest" in kwargs:
            self.toJSON(kwargs["json_dest"])
        else:
            self.toJSON(default_dest_dir / Path(f"{self._label}.json"))

        if "schema_file" in kwargs:
            arg = [kwargs["schema_file"]]
            if "db_dest" in kwargs:
                arg.append(kwargs["db_dest"])
            else:
                arg.append(default_dest_dir / Path(f"{self._label}.db"))
            if "db_dump_dest" in kwargs:
                arg.append(kwargs["db_dump_dest"])
            else:
                arg.append(default_dest_dir / Path(f"{self._label}.sql"))
            self.toDB(*arg)
