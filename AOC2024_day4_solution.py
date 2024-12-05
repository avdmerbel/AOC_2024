import numpy as np
import re

day = 4

# get the input
data_array = np.loadtxt(f'AOC2024_day{day}_input.txt', dtype='str')

example_array = ["MMMSXXMASM",
                 "MSAMXMSMSA",
                 "AMXSXMAAMM",
                 "MSAMASMSMX",
                 "XMASAMXAMM",
                 "XXAMMXXAMA",
                 "SMSMSASXSS",
                 "SAXAMASAAA",
                 "MAMMMXMMMM",
                 "MXMXAXMASX"]

# find everything horizontally both ways
# easy: search pattern XMAS and SAMX

pattern = re.compile("XMAS")
backward_pattern = re.compile("SAMX")

count_horizontal = 0
for row in example_array:
    count_horizontal += len(re.findall(pattern, row)) + len(re.findall(backward_pattern, row))

# find everything vertically both ways
# harder: index on one element and corresponding index on the next 

def check_elements_vertical(arr, var1='X', var2='M', var3='A', var4='S'):
    count = 0  # Initialize a counter to count how many times the conditions are met

    # Iterate through each row in the array (up to len(arr) - 3)
    for i in range(len(arr)-3):  # We need at least 4 rows to check
        for j in range(len(arr[i])):  # Iterate through each element in the row
            # Debugging: print current indices and values
            print(f"Checking element at row {i}, column {j}: {arr[i][j]}")
            
            # Check if the element in the current row matches var1
            if arr[i][j] == var1:
                print(f"Match found for var1 at {arr[i][j]}")

                # Check if the element in the next row matches var2
                if arr[i+1][j] == var2:
                    print(f"Match found for var2 at {arr[i+1][j]}")

                    # Check if the element in the next row matches var3
                    if arr[i+2][j] == var3:
                        print(f"Match found for var3 at {arr[i+2][j]}")

                        # Check if the element in the next row matches var4
                        if arr[i+3][j] == var4:
                            print(f"Match found for var4 at {arr[i+3][j]}")
                            count += 1  # Increment the count when all checks pass

    
    # Iterate through each row in the array (up to len(arr) - 3)
    for i in range(len(arr)-1,2,-1):  # We need at least 4 rows to check
        for j in range(len(arr[i])):  # Iterate through each element in the row
            # Debugging: print current indices and values
            print(f"Checking element at row {i}, column {j}: {arr[i][j]}")
            
            # Check if the element in the current row matches var1
            if arr[i][j] == var1:
                print(f"Match found for var1 at {arr[i][j]}")

                # Check if the element in the next row matches var2
                if arr[i-1][j] == var2:
                    print(f"Match found for var2 at {arr[i-1][j]}")

                    # Check if the element in the next row matches var3
                    if arr[i-2][j] == var3:
                        print(f"Match found for var3 at {arr[i-2][j]}")

                        # Check if the element in the next row matches var4
                        if arr[i-3][j] == var4:
                            print(f"Match found for var4 at {arr[i-3][j]}")
                            count += 1  # Increment the count when all checks pass

    return count  # Return the total count of occurrences

count_vertical = check_elements_vertical(example_array)

# find everything diagonally all four ways
def check_elements_diagonally(arr, var1='X', var2='M', var3='A', var4='S'):
    count = 0

    # Left to right up to down
    for i in range(len(arr)-3):  # We need at least 4 rows to check
        for j in range(len(arr[i])-3):  # Iterate through each element in the row with at least four spaces
            # Debugging: print current indices and values
            print(f"Checking element at row {i}, column {j}: {arr[i][j]}")
            
            # Check if the element in the current row matches var1
            if arr[i][j] == var1:
                print(f"Match found for var1 at {arr[i][j]}")

                # Check if the element in the next row matches var2
                if arr[i+1][j+1] == var2:
                    print(f"Match found for var2 at {arr[i+1][j+1]}")

                    # Check if the element in the next row matches var3
                    if arr[i+2][j+2] == var3:
                        print(f"Match found for var3 at {arr[i+2][j+2]}")

                        # Check if the element in the next row matches var4
                        if arr[i+3][j+3] == var4:
                            print(f"Match found for var4 at {arr[i+3][j+3]}")
                            count += 1  # Increment the count when all checks pass

    # right to left up to down
    for i in range(len(arr)-3):  # We need at least 4 rows to check
        for j in range(len(arr[i])-1,2,-1):  # Iterate through each element in the row with at least four spaces
            # Debugging: print current indices and values
            print(f"Checking element at row {i}, column {j}: {arr[i][j]}")
            
            # Check if the element in the current row matches var1
            if arr[i][j] == var1:
                print(f"Match found for var1 at {arr[i][j]}")

                # Check if the element in the next row matches var2
                if arr[i+1][j-1] == var2:
                    print(f"Match found for var2 at {arr[i+1][j-1]}")

                    # Check if the element in the next row matches var3
                    if arr[i+2][j-2] == var3:
                        print(f"Match found for var3 at {arr[i+2][j-2]}")

                        # Check if the element in the next row matches var4
                        if arr[i+3][j-3] == var4:
                            print(f"Match found for var4 at {arr[i+3][j-3]}")
                            count += 1  # Increment the count when all checks pass

    # right to left down to up
    for i in range(len(arr)-1,2,-1):  # We need at least 4 rows to check
        for j in range(len(arr[i])-1,2,-1):  # Iterate through each element in the row with at least four spaces
            # Debugging: print current indices and values
            print(f"Checking element at row {i}, column {j}: {arr[i][j]}")
            
            # Check if the element in the current row matches var1
            if arr[i][j] == var1:
                print(f"Match found for var1 at {arr[i][j]}")

                # Check if the element in the next row matches var2
                if arr[i-1][j-1] == var2:
                    print(f"Match found for var2 at {arr[i-1][j-1]}")

                    # Check if the element in the next row matches var3
                    if arr[i-2][j-2] == var3:
                        print(f"Match found for var3 at {arr[i-2][j-2]}")

                        # Check if the element in the next row matches var4
                        if arr[i-3][j-3] == var4:
                            print(f"Match found for var4 at {arr[i-3][j-3]}")
                            count += 1  # Increment the count when all checks pass

    # left to right down to up
    for i in range(len(arr)-1,2,-1):  # We need at least 4 rows to check
        for j in range(len(arr[i])-3):  # Iterate through each element in the row with at least four spaces
            # Debugging: print current indices and values
            print(f"Checking element at row {i}, column {j}: {arr[i][j]}")
            
            # Check if the element in the current row matches var1
            if arr[i][j] == var1:
                print(f"Match found for var1 at {arr[i][j]}")

                # Check if the element in the next row matches var2
                if arr[i-1][j+1] == var2:
                    print(f"Match found for var2 at {arr[i-1][j+1]}")

                    # Check if the element in the next row matches var3
                    if arr[i-2][j+2] == var3:
                        print(f"Match found for var3 at {arr[i-2][j+2]}")

                        # Check if the element in the next row matches var4
                        if arr[i-3][j+3] == var4:
                            print(f"Match found for var4 at {arr[i-3][j+3]}")
                            count += 1  # Increment the count when all checks pass

    return count

count_diagonal = check_elements_diagonally(example_array)

count_horizontal+count_vertical+count_diagonal

horizontal = 0
for row in data_array:
    horizontal += len(re.findall(pattern, row)) + len(re.findall(backward_pattern, row))

solution = horizontal + check_elements_diagonally(data_array) + check_elements_vertical(data_array)

def check_mas(arr, var1='M', var2='A', var3='S'):

    count = 0

    for i in range(len(arr)-2):  # We need at least 3 rows to check
        for j in range(len(arr[i])-2):  # Iterate through each element in the row with at least four spaces
        # Check if the element in the current row is M
            if arr[i][j] == var1:
                # check if two columns over is 'S'
                if arr[i][j+2] == var3:
                    # check if middle is 'A'
                    if arr[i+1][j+1] == var2:
                        # check if two rows down left is 'M'
                        if arr[i+2][j] == var1:
                            # check if two rows down right is 'S'
                            if arr[i+2][j+2] == var3:
                                count += 1  # Increment the count when all checks pass

    for i in range(len(arr)-2):  # We need at least 3 rows to check
        for j in range(len(arr[i])-2):  # Iterate through each element in the row with at least four spaces
        # Check if the element in the current row is S
            if arr[i][j] == var3:
                # check if two columns over is 'M'
                if arr[i][j+2] == var1:
                    # check if middle is 'A'
                    if arr[i+1][j+1] == var2:
                        # check if two rows down left is 'S'
                        if arr[i+2][j] == var3:
                            # check if two rows down right is 'M'
                            if arr[i+2][j+2] == var1:
                                count += 1  # Increment the count when all checks pass
    
    for i in range(len(arr)-2):  # We need at least 3 rows to check
        for j in range(len(arr[i])-2):  # Iterate through each element in the row with at least four spaces
        # Check if the element in the current row is M
            if arr[i][j] == var1:
                # check if two columns over is 'M'
                if arr[i][j+2] == var1:
                    # check if middle is 'A'
                    if arr[i+1][j+1] == var2:
                        # check if two rows down left is 'S'
                        if arr[i+2][j] == var3:
                            # check if two rows down right is 'S'
                            if arr[i+2][j+2] == var3:
                                count += 1  # Increment the count when all checks pass

    for i in range(len(arr)-2):  # We need at least 3 rows to check
        for j in range(len(arr[i])-2):  # Iterate through each element in the row with at least four spaces
        # Check if the element in the current row is S
            if arr[i][j] == var3:
                # check if two columns over is 'S'
                if arr[i][j+2] == var3:
                    # check if middle is 'A'
                    if arr[i+1][j+1] == var2:
                        # check if two rows down left is 'M'
                        if arr[i+2][j] == var1:
                            # check if two rows down right is 'M'
                            if arr[i+2][j+2] == var1:
                                count += 1  # Increment the count when all checks pass
    
    return count

check_mas(example_array)

check_mas(data_array)