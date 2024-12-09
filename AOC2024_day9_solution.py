
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

def rearrange_file(file):
    # Flatten the input list
    new_file = sum(file, [])

    # Step 1: Identify dot groups (start and end indices)
    dot_groups = []
    current_start = None
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

    # Step 2: Count number groups
    num_groups = {}
    for element in new_file:
        if element != '.':
            num_groups[element] = num_groups.get(element, 0) + 1

    # Sort number groups by descending number value (largest first)
    sorted_num_groups = sorted(num_groups.items(), key=lambda x: -x[0])

    # Step 3: Place numbers into the dot groups
    for number, count in sorted_num_groups:
        placed = False  # Flag to check if the number group was placed

        for i in range(len(dot_groups)):
            start, end = dot_groups[i]
            dot_length = end - start + 1

            if dot_length >= count:  # Only place the number if the dot group is large enough
                # Replace dots with numbers
                new_file[start:start + count] = [number] * count

                # After placing the number group, replace the remaining spaces with dots
                remaining_dots = dot_length - count
                if remaining_dots > 0:
                    new_file[start + count:start + count + remaining_dots] = ['.'] * remaining_dots

                dot_groups[i] = None  # Mark this group as fully used
                placed = True  # Mark that we have placed the number group
                break  # Exit the loop as the number group has been placed

        # If the number group couldn't be placed, do nothing and move to the next number group
        if not placed:
            continue

        # Remove fully used dot groups
        dot_groups = [group for group in dot_groups if group is not None]

    # Convert the list back to a string
    return ''.join(map(str, new_file))



rearrange_file(example_file)


def check_sum_new(file):
    
    checksum = 0
    
    for index, value in enumerate(file):
        
        if value == '.':
            print("This is a dot")
            continue
        
        checksum += index*int(value)
        
    return checksum

check_sum([item for sublist in new_file for item in sublist])