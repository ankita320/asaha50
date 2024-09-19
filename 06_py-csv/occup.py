import random
import csv
def occup_d():
    with open("./occupations.csv", mode ='r') as file:
       d = {}
       csvFile = csv.DictReader(file)
       for lines in csvFile:
            d[lines.get('Job Class')] = float(lines.get('Percentage'))
       return d
                
def rando_occup(x):
    sum_v = 0
    r = random.uniform(0,x.get('Total'))
    for i in x:
        print(i)
        print(x.get(i))
        sum_v += x.get(i)
        print(sum)
        if sum_v > r:
            return {i:x.get(i)}
            
