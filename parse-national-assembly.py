import csv
import os
import string

provinces_dir = os.path.join(os.getcwd(), "national-assembly")

with open("national_assembly.csv", "w", newline="\n") as national_assembly:
    headers = ["Province", "Constituency", "Name", "Gender", "Party", "Votes"]
    csvwriter = csv.writer(national_assembly)
    csvwriter.writerow(headers)
    tot = 0
    for province_dir in os.listdir(provinces_dir):
        province = province_dir.replace("-", " ").title()
        province_dir_loc = os.path.join(provinces_dir, province_dir)
        for const_file in os.listdir(province_dir_loc):
            const = os.path.splitext(const_file)[0].replace("--", "/")
            const = const.replace("-", " ").title()
            with open(os.path.join(province_dir_loc, const_file)) as prov_file:
                lines = prov_file.readlines()
                lines = list(map(lambda x: x.replace("\n", ""), lines))
                tot +=1
                for i in range(0, len(lines), 4):
                    name = lines[i].rstrip(" ").title()
                    gender = lines[i+1].strip(" ")
                    party = lines[i+2].rstrip(" ")
                    votes = int(lines[i+3].replace(" ", ""))
                    row = [province, const, name, gender, party, votes]
                    csvwriter.writerow(row)

print(tot)
                    

