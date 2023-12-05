res = 0
numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight','nine']

with open('1.txt', 'r') as file:
    for line in file:
        digits = []
        num = ''
        for char in line:
            num += char
            if num in numbers:
                digits.append(numbers.index(num)+1)
                num = ''

        res += (digits[0]*10) + digits[-1]

print(res)