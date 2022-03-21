import csv
import numpy
import pandas


Path=r"Data\DB_Validations_OPUS.csv"

Dict_Data={}
with open(Path, 'r',encoding='utf8') as file:
        reader = csv.reader(file)
        Header=next(reader)
        print(Header)


        for line in reader:
            # print(line,type(line))
            Date=line[0]
            Hour=line[1]
            Station=line[2]
            Users=line[3]

            if Station not in Dict_Data.keys():
                Dict_Data[Station]={}
            if Date not in Dict_Data[Station].keys():
                Dict_Data[Station][Date]={}
            if Hour not in Dict_Data[Station][Date].keys():
                Dict_Data[Station][Date][Hour]=Users

print(Dict_Data)