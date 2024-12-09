
day = 9

example_input = '2333133121414131402'

# load input puzzle 1
input = open(f'AOC2024_day{day}_input.txt','r')
lines=input.readlines()

files = list(lines[0][:-1])

def create_file_mapping(file):
    new_file = []
    id = -1

    for index, number in enumerate(file):
        
        if index%2 == 0:
            is_file = True
            id += 1
        else:
            is_file = False
        
        if is_file:
            new_file.extend([id] * int(number))
        else:
            new_file.extend('.' * int(number))

    return new_file

example_file = create_file_mapping(example_input)

def find_index_from_back(list):
    for i in range(len(list) - 1, -1, -1):  # Loop from the end of the string to the start
        if list[i] != ".":
            return (list[i], i)
    return False


def restructure_file(file):
    new_file = file
    last_number = None

    for index, value in enumerate(new_file):
        
        if all(element == "." for element in new_file[index:]):
            print("Only dots remain, stopping loop")
            break
        
        if type(value) is int:
            continue
        elif value == ".":
            last_number = find_index_from_back(new_file)[0]
            last_number_index = find_index_from_back(new_file)[1]
            
            if last_number:
                new_file[index] = last_number
                new_file[last_number_index] = "."
        

    return new_file

new_file = restructure_file(example_file)

def check_sum(file):
    
    checksum = 0
    
    for index, value in enumerate(file):
        
        if all(char == "." for char in file[index:]):
            print("Only dots remain, stopping loop")
            break
        
        checksum += index*value
        
    return checksum

check_sum(new_file)

mapping_file = create_file_mapping(files)
new_files = restructure_file(mapping_file)
checksum = check_sum(new_files)


# part 2
# adjust functions a little
def create_new_file_mapping(file):
    new_file = []
    id = -1

    for index, number in enumerate(file):
        
        if index%2 == 0:
            is_file = True
            id += 1
        else:
            is_file = False
        
        if is_file:
            if int(number) > 0:
                new_file.append([id] * int(number))
        else:
            if int(number) > 0:
                new_file.append(['.']*int(number))

    return new_file

example_file = create_new_file_mapping(example_input)

def restructure_file_new(file):
    
    new_file = sum(file, [])  # Flatten the input list

    # Step 1: Identify dot groups (start and end indices) and count the numbers
    dot_groups = []
    current_start = None

    # Detect dot groups and store their start and end indices
    for index, element in enumerate(new_file):
        if element == '.':
            if current_start is None:
                current_start = index
        else:
            if current_start is not None:
                dot_groups.append((current_start, index - 1))
                current_start = None

    if current_start is not None:
        dot_groups.append((current_start, len(new_file) - 1))

    # Count numbers in the input
    num_groups = {}
    for element in new_file:
        if element != '.':
            num_groups[element] = num_groups.get(element, 0) + 1

    # Sort number groups by size descending, then by number value
    sorted_num_groups = sorted(num_groups.items(), key=lambda x: (-x[1], -x[0]))

    # Step 2: Place numbers into dot groups
    for number, count in sorted_num_groups:
        for i, (start, end) in enumerate(dot_groups):
            dot_length = end - start + 1
            if dot_length >= count:  # Check if the dot group can fit the numbers
                # Replace dots with the current number group
                new_file[start:start + count] = [number] * count
                
                # Update the dot group for any remaining dots
                if dot_length > count:
                    dot_groups[i] = (start + count, end)
                else:
                    dot_groups.pop(i)
                break  # Move to the next number group

    # Convert the list back to a string
    output_str = ''.join(map(str, new_file))
    print(output_str)


    return output_str

restructure_file_new(example_file)


def check_sum_new(file):
    
    checksum = 0
    
    for index, value in enumerate(file):
        
        if value == '.':
            print("This is a dot")
            continue
        
        checksum += index*int(value)
        
    return checksum

check_sum([item for sublist in new_file for item in sublist])