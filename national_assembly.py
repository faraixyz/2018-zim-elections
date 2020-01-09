from pathlib import Path
from elect_parser import ElectParser
from party_formats import sanitize_party


class NationalAssemblyParser(ElectParser):
    def __init__(self, label, src: Path):
        self._fieldnames = ['province', 'constituency', 'name', 'gender',
                            'party', 'votes']
        self._elects = []
        self._label = label
        for province_dir in src.iterdir():
            province = province_dir.stem.replace('-', ' ').title()
            for constituency_file in province_dir.glob('*.txt'):
                constituency = constituency_file.stem.replace("--", "/") \
                    .replace('-', ' ').title()
                with constituency_file.open() as data:
                    lines = data.readlines()
                    lines = list(map(lambda x: x.replace("\n", ""), lines))
                    for i in range(0, len(lines), 4):
                        candidate = {field: '' for field in self._fieldnames}
                        party = lines[i+2].rstrip(" ")
                        candidate['party'] = sanitize_party(party)
                        name = lines[i].rstrip(" ").title().replace('  ', " ")
                        candidate['name'] = name
                        candidate['votes'] = int(lines[i+3].replace(" ", ""))
                        candidate['province'] = province
                        candidate['constituency'] = constituency
                        candidate['gender'] = lines[i+1].strip(" ")
                        self._elects.append(candidate)


if __name__ == "__main__":
    p = NationalAssemblyParser(Path(__file__).stem,
                               Path("./data/national-assembly"))
    p.toAll(Path("./output"),
            schema_file=Path("./data/schemas/national_assembly.schema.sql"))
