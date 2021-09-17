import csv

f = open('graph/data.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)

date_list = []
case_dict = {}
death_dict = {}

for i, line in enumerate(rdr):
    if i == 0:
        for i, date in enumerate(line):
            if i < 3:
                pass
            else:
                x = date
                x = x.replace(" ", "")
                date_list.append(x)
    else:
        if line[1] == '확진자수':
            case_dict[line[0]] = line[3:]
        else:
            death_dict[line[0]] = line[3:]


    #print(i)
    #print(line)
print(date_list)
f.close()