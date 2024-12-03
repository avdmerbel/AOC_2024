day = 2

# load input puzzle 1
input = open(f'AOC2024_day{day}_input.txt','r')
lines=input.readlines()

# get the lists of numbers
list1=[]
for line in lines:
    list1.append(line.split())

list1 = [[int(item) for item in sublist] for sublist in list1]


def check(row):
    if all(i > j for i, j in zip(row, row[1:])) | all(i < j for i, j in zip(row, row[1:])) and all(abs(i-j) >= 1 and abs(i-j) <=3 for i, j in zip(row, row[1:])):
        return True
    
    return False

count=0
for row in list1:
    if check(row): 
        count += 1

count=0
for row in list1:
    if check(row):
        count+=1
    else:
        for index in range(len(row)):
            indexed_row = row[:index] + row[index+1:]  
            if check(indexed_row):
                count+=1
                break
                