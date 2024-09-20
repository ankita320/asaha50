'''Ankita Saha, Andy Shyklo
  Python Pigs
  SoftDev
  Reading CSV Files and Practicing W/ Random
  2024-9-19
  time spent: 0.9 hours
  '''
import random
import csv

def job_d():
    with open("./occupations.csv", mode ='r') as file:
        d = {}
        total = 0
        csvFile = csv.DictReader(file)
        for lines in csvFile:
            if not lines.get('Job Class') == 'Total':
                d[lines.get('Job Class')] = float(lines.get('Percentage'))
            else:
                total = float(lines.get('Percentage'))
                
        
        sum_v = 0
        #print(total)
        r = random.uniform(0,total)
        for i in d:
        #print(i)
        #print(d.get(i))
            sum_v += d.get(i) #adds up the percentages as it loops, if exceeds the random number, returns current one, weighted random
        #print(sum)
            if sum_v > r:
                return {i:d.get(i)}
print(job_d())
