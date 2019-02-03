import csv
import os
from party_formats import sanitize_party
source_file_loc = os.path.join(os.getcwd(), "senate.txt")
parsed_file_loc = os.path.join(os.getcwd(), "senate.csv")

with open(parsed_file_loc, "w", newline="\n") as dest_file:
    csvwriter = csv.writer(dest_file)
    headers = ["Province", "SER", "Name", "Gender", "Party"]
    csvwriter.writerow(headers)
    with open(source_file_loc, "r") as source_file:
        lines = source_file.readlines()
        for province_line_no in range(0, len(lines), 25):
            province = lines[province_line_no].rstrip("\n").rstrip(" ")
            for candidate_line_no in range(province_line_no+1, province_line_no+25, 4):
                ser = lines[candidate_line_no].rstrip("\n")
                name = lines[candidate_line_no+1].rstrip("\n").rstrip(" ")
                gender = lines[candidate_line_no+2].rstrip("\n")
                party = lines[candidate_line_no+3].rstrip("\n")
                party = sanitize_party(party)
                csvwriter.writerow((province, ser, name, gender, party))
