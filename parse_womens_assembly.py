import csv
import os

source_file_loc = os.path.join(os.getcwd(), "womens-assembly.txt")
parsed_file_loc = os.path.join(os.getcwd(), "womens-assembly.csv")

with open(parsed_file_loc, "w", newline="\n") as dest_file:
    csvwriter = csv.writer(dest_file)
    headers = ["Province", "SER", "NAME", "GENDER", "PARTY"]
    csvwriter.writerow(headers)
    with open(source_file_loc, "r") as source_file:
        lines = source_file.readlines()
        for province_line_no in range(0, len(lines), 25):
            province = lines[province_line_no].rstrip("\n")
            for candidate_line_no in range(province_line_no+1, province_line_no+25, 4):
                ser = lines[candidate_line_no].rstrip("\n")
                name = lines[candidate_line_no+1].rstrip("\n")
                gender = lines[candidate_line_no+2].rstrip("\n")
                party = lines[candidate_line_no+3].rstrip("\n")
                csvwriter.writerow((province, ser, name, gender, party))
