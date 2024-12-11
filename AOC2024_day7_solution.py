from itertools import product

day = 7

example_input = [{190: (10, 19)},
                 {3267: (81, 40, 27)},
                 {83: (17, 5)},
                 {156: (15, 6)},
                 {7290: (6, 8, 6, 15)},
                 {161011: (16, 10, 13)},
                 {192: (17, 8, 14)},
                 {21037: (9, 7, 18, 13)},
                 {292: (11, 6, 16, 20)}]

puzzle_input = []
with open(f'AOC2024_day{day}_input.txt', 'r') as file:
    for line in file:
        # Split the line into key and value
        key, value = line.strip().split(': ')
        # Convert the value into a tuple of integers
        value_tuple = tuple(map(int, value.split()))
        # Append the dictionary to the result list
        puzzle_input.append({int(key): value_tuple})




possible_operators = ["+", "*"]

summation = []
for dict in puzzle_input:
    
    for result, equation in dict.items():
        operator_positions = len(equation)-1
        
            
        # number of possible arrangements: len-1 ^ 2
        possible_permutations = [p for p in product(possible_operators, repeat = operator_positions)]

        outcomes = []
        
        for permutation in possible_permutations:
            intermittent_result = equation[0]
            
            for number, operator in zip(equation[1:], permutation):
                
                if operator == "+":
                    intermittent_result += number
                elif operator == "*":
                    intermittent_result *= number
            
            outcomes.append(intermittent_result)
            
        
    #print([singular_outcome for singular_outcome in [outcome for outcome in outcomes] if singular_outcome == result])
    summation.append(set([singular_outcome for singular_outcome in [outcome for outcome in outcomes] if singular_outcome == result]))
      
output = 0
for s in summation:
    output += sum(s)
    #summation.append(sum([outcome for outcome in outcomes if outcome == result]))
        
        
# part 2
possible_operators = ["+", "*", "||"]

summation = []
for dict in puzzle_input:
    
    for result, equation in dict.items():
        operator_positions = len(equation)-1
        
            
        # number of possible arrangements: len-1 ^ 2
        possible_permutations = [p for p in product(possible_operators, repeat = operator_positions)]

        outcomes = []
        
        for permutation in possible_permutations:
            intermittent_result = equation[0]
            
            for number, operator in zip(equation[1:], permutation):
                
                if operator == "+":
                    intermittent_result += number
                elif operator == "*":
                    intermittent_result *= number
                elif operator == "||":
                    intermittent_result = int(str(intermittent_result)+str(number))
            
            outcomes.append(intermittent_result)
            
        
    #print([singular_outcome for singular_outcome in [outcome for outcome in outcomes] if singular_outcome == result])
    summation.append(set([singular_outcome for singular_outcome in [outcome for outcome in outcomes] if singular_outcome == result]))
      
output = 0
for s in summation:
    output += sum(s)
    #summation.append(sum([outcome for outcome in outcomes if outcome == result]))
        
        
    
