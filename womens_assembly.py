from pathlib import Path
from elect_parser import ElectParser
from party_formats import sanitize_party


class WomensAssemblyParser(ElectParser):
    def __init__(self, label, src):
        self._elects = []
        self._label = label
        self._fieldnames = ['province', 'ser', 'name', 'gender', 'party']
        with open(src, 'r') as txtdata:
            lines = txtdata.readlines()
            for province_line_no in range(0, len(lines), 25):
                province = lines[province_line_no].rstrip('\n').rstrip(' ')
                linenos = (province_line_no+1, province_line_no+25, 4)
                for candidate_line_no in range(*linenos):
                    candidate_obj = {field: '' for field in self._fieldnames}
                    ser = lines[candidate_line_no].rstrip("\n")
                    name = lines[candidate_line_no+1].rstrip("\n").rstrip(" ")
                    gender = lines[candidate_line_no+2].rstrip("\n")
                    party = lines[candidate_line_no+3].rstrip("\n")
                    party = sanitize_party(party)
                    candidate_obj['ser'] = ser
                    candidate_obj['province'] = province
                    candidate_obj['name'] = name
                    candidate_obj['gender'] = gender
                    candidate_obj['party'] = party
                    self._elects.append(candidate_obj)


if __name__ == "__main__":
    p = WomensAssemblyParser(Path(__file__).stem, "./data/womens-assembly.txt")
    p.toAll(Path("./output"),
            schema_file=Path("./data/schemas/womens_assembly.schema.sql"))
