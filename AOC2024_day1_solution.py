day = 1
# load input puzzle 1
input = open(f'AOC_day{day}_input.txt','r')
lines=input.readlines()

# get the lists of numbers
list1=[]
list2=[]
for line in lines:
    list1.append(int(line.split()[0]))
    list2.append(int(line.split()[1]))

# sort smallest to largest
list1_sorted = sorted(list1)
list2_sorted = sorted(list2)

# find the differences
differences = []
for number in range(len(list1_sorted)):
    difference = abs(list1_sorted[number] - list2_sorted[number]) # absolute because distance not difference
    differences.append(difference)
    
# solution: total distance between numbers
sum(differences)

# PART 2

total_count = {}
for number in list2:
    total_count[number] = total_count.get(number,0) + 1

similarities =[]
for number in list1:
    if number in total_count.keys():
        similarity = number*total_count[number]
    else:
        similarity=0

    similarities.append(similarity)
    
sum(similarities)