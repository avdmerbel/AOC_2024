
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

    def define_dot_groups(new_file):
        dot_groups = {}

        i = 0
        while i < len(new_file):
            # Find dot groups
            if new_file[i] == '.':
                start = i
                while i < len(new_file) and new_file[i] == '.':
                    i += 1
                dot_groups[start] = i - start
            else:
                i += 1

        return sorted(dot_groups.items())
    
    def define_num_groups(new_file):
        num_groups = {}
        
        i = 0
        while i < len(new_file):
            # Find number groups
            if isinstance(new_file[i], int):
                start = i
                current_num = new_file[i]
                while i < len(new_file) and new_file[i] == current_num:
                    i += 1
                num_groups[start] = i - start
            else:
                i += 1
        return sorted(num_groups.items(), reverse=True)
    
    sorted_dot_groups = define_dot_groups(new_file)
    sorted_num_groups = define_num_groups(new_file)

    for num_start, num_length in sorted_num_groups:
        
        # Find a suitable dot group
        for dot_start, dot_length in sorted_dot_groups:
            if dot_length >= num_length and num_start > dot_start:  # Check if the dot group can accommodate the number group
                # Move the number group
                
                new_file[dot_start:dot_start + num_length] = [new_file[num_start]] * num_length

                # Move the dot group to the original number group position
                new_file[num_start:num_start + num_length] = ['.'] * num_length

                # Update the dot group location
                if dot_length > num_length:  # Some dots are left
                    new_dot_start = dot_start + num_length
                    remaining_dots = dot_length - num_length

                    sorted_dot_groups.remove((dot_start, dot_length))
                    sorted_dot_groups.append((new_dot_start, remaining_dots))
                    sorted_dot_groups.sort()
                else:  # All dots are consumed, move the full dot group
                    new_dot_start = num_start
                    sorted_dot_groups.remove((dot_start, dot_length))
                    sorted_dot_groups.append((new_dot_start, dot_length))
                    sorted_dot_groups.sort()
                #print(f"  Updated dot groups: {sorted_dot_groups}")
                break
        #print(f"State of data after processing group: {new_file}")
    return new_file

example_rearranged = rearrange_file(example_file)


def check_sum_new(file):
    
    checksum = 0
    
    for index, value in enumerate(file):
        
        if value == '.':
            continue
        
        checksum += index*int(value)
        
    return checksum

check_sum_new(example_rearranged)

files_mapping = create_new_file_mapping(files)
rearranged_files = rearrange_file(files_mapping)
check_sum_new(rearranged_files)