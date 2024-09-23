<<<<<<< HEAD
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
            
=======
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
>>>>>>> 51c269351514d508696546153fda5e39a28675ab
