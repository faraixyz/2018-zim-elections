from pathlib import Path
import csv
from elect_parser import ElectParser


class DisabilitySenatorParser(ElectParser):
    def __init__(self, label, src):
        self._elects = []
        self._label = label
        with open(src, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self._elects.append(dict(row))
        self._fieldnames = ['ser', 'name', 'gender']


if __name__ == "__main__":
    p = DisabilitySenatorParser(Path(__file__).stem,
                                "./data/disability-senators.csv")
    p.toAll(Path("./output"),
            schema_file=Path("./data/schemas/disability_senators.schema.sql"))
