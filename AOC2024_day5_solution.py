day = 5

# get the input
#input = open(f'AOC2024_day{day}_input.txt','r')
input = open(f'example_day5.txt', 'r')
lines=input.readlines()

# find where the rules end and updates start
cut = lines.index('\n')

# prepare data
# get rules and updates in a tuple (ordered and unchangeable)
rules_base = []
updates_base = []

for line in lines[0:cut]:
    rules_base.append(line.split())
for line in lines[cut+1:len(lines)]:
    updates_base.append(line.split())

rules = []
for rule in rules_base:
    rules.append(tuple(map(int, rule[0].split('|'))))
    
updates = []
for update in updates_base:
    updates.append(tuple(map(int, update[0].split(','))))
    
def check_rule(update, rules):
    # get indices from the update 
    # check orders in the rules
    
    print(update)
    
    for index, value in enumerate(update):
        
        # first find all rules where the current number should be first
        number_first = [rule for rule in rules if rule[0]==value]
        print(f'rules with given number first: {number_first}')
        
        # find all rules where the current number should come after some other number
        number_last = [rule for rule in rules if rule[1]==value]
        print(f'rules with given number last: {number_last}')
        
        number_in_after_rule =[]
        number_in_before_rule=[]
        # find all numbers that are both in the after rule and in the update
        if any(number in update[:index] + update[index+1:] for number in [after[1] for after in number_first]): 
            number_in_after_rule = [number for number in update[:index] + update[index+1:] if number in [after[1] for after in number_first]]
        print(f'numbers in update and before rule: {number_in_before_rule}')
        # find all numbers that are both in the before rule and in the update
        if any(number in update[:index] + update[index+1:] for number in [before[0] for before in number_last]): 
            number_in_before_rule = [number for number in update[:index] + update[index+1:] if number in [before[0] for before in number_last]]
        print(f'numbers in update and after rule: {number_in_after_rule}')
        # get the indices of all matching numbers in the tuple
        indices_after = [i for i, value in enumerate(update) if value in number_in_after_rule]
        indices_before = [i for i, value in enumerate(update) if value in number_in_before_rule]
        print(f'indices after: {indices_after}')
        print(f'indices before: {indices_before}')
        
        print(f'index is:{index}')
        
        if index > any(indices_after) or index < any(indices_before):
            print('update is not valid')
            break
        else: 
            print("update is valid")
     
     
check_rule(update=updates[0], rules=rules)   
count=[]
for update in updates:  
    count.append(check_rule(update=update, rules=rules))
        
        

