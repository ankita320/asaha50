def bitstream(){
    f = open("krewes.txt", "r")
    r = f.read().split('@@@')
    
<<<<<<< HEAD
    d4 = {}
    d5 = {}
    arr = [d4,d5]
    
    for i in r:
        if i[0] == '4':
            
=======
    arr = []
    
    for i in r:
        j = i.split("$$$")
        arr.append(arr)
            
    d = {4:[],5:[]}
    for k in arr:
        if k[0] == 4:
            d[4].append({k[1]: k[2]})
        elif k[0] == 5:
            d[5].append({k[1]: k[2]})
            
    num = random.randint(4,5)
    p = random.randint(len(d.get(num))-1)


    k = list(d.get(num)[p])[0]
    v = list(d.get(num)[p])[1]

    return "PERIOD: " + num + "; NAME: " + k + "; VALUE: " + v
        

    '''
list=[dictionary_4, dictionary_5]
dictionary_4={name:ducky,]
splice first at $$$ and put intwo tuple of length 3
splice at @@@, put tuples in list

'''
    }
