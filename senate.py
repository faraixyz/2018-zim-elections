import sqlite3
from pathlib import Path
from elect_parser import ElectParser
from party_formats import sanitize_party


class SenateParser(ElectParser):
    def __init__(self, label, src: Path):
        self._fieldnames = ['province', 'ser', 'name', 'gender', 'party']
        self._elects = []
        self._label = label
        with open(src, 'r') as source_file:
            lines = source_file.readlines()
            for province_line_no in range(0, len(lines), 25):
                province = lines[province_line_no].rstrip("\n").rstrip(" ")
                r = (province_line_no+1, province_line_no+25, 4)
                for candidate_line_no in range(*r):
                    candidate = {field: '' for field in self._fieldnames}
                    candidate['province'] = province
                    candidate['ser'] = lines[candidate_line_no].rstrip("\n")
                    name = lines[candidate_line_no+1].rstrip("\n")
                    candidate['name'] = name.rstrip(" ").replace("  ", " ")
                    gender = lines[candidate_line_no+2].rstrip("\n")
                    candidate['gender'] = gender
                    party = lines[candidate_line_no+3].rstrip("\n")
                    candidate['party'] = sanitize_party(party)
                    self._elects.append(candidate)

w = SenateParser(Path(__file__).stem, Path('./data/senate.txt'))
w.toAll(Path('output'), schema_file=Path('./data/schemas/senate.schema.sql'))
