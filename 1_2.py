num_3 = {"one":1, "two":2, "six":6}
num_4 = {"four":4, "five":5, "nine":9}
num_5 = {"three":3, "seven":7, "eight":8}

def getNumFromWord(line):
    temp_str = ''

    if len(line)>=3:
        if line[:3] in num_3:
            temp_str = num_3[line[:3]]
    
    if len(line)>=4:
        if line[:4] in num_4:
            temp_str = num_4[line[:4]]

    if len(line)>=5:
        if line[:5] in num_5:
            temp_str = num_5[line[:5]]

    return temp_str
    
def firstDigit(line):
    temp_str = ''
    ptr = 0
    while ptr<len(line) and temp_str=='':
        if line[ptr].isnumeric():
            return int(line[ptr])
        else:
            temp_str = getNumFromWord(line[ptr:])

        ptr += 1
    return int(temp_str)
        
def secondDigit(line):
    temp_str = ''
    ptr = -1
    while (0-ptr)<=len(line) and temp_str=='':
        if line[ptr].isnumeric():
            return int(line[ptr])
        else:
            temp_str = getNumFromWord(line[ptr:])

        ptr -= 1    

    return int(temp_str)


with open('1.txt', 'r') as file:
    res = 0
    for line in file:
        dig1 = firstDigit(line)
        dig2 = secondDigit(line)

        res += (dig1*10) + dig2

print(res)