import random
import csv

def job_d():
    with open("./occupations.csv", mode ='r') as file:
        d = {}
        csvFile = csv.DictReader(file)
        for lines in csvFile:
            d[lines.get('Job Class')] = float(lines.get('Percentage'))
        
        sum_v = 0
        r = random.uniform(0,d.get('Total'))
        for i in d:
        #print(i)
        #print(d.get(i))
            sum_v += d.get(i) #adds up the percentages as it loops, if exceeds the random number, returns current one, weighted random
        #print(sum)
            if sum_v > r:
                return {i:d.get(i)}
print(job_d())
