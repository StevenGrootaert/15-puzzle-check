# TEST CASES (comment out the get_inputs function)
#incoming=[1,5,9,13,2,6,10,14,3,7,11,15,4,8,12,16]
#incoming=[7,8,9,10,6,1,2,11,5,4,3,12,16,15,14,13]
#incoming=[1,8,9,16,2,7,10,15,3,6,11,14,4,5,12,13]
#incoming=[15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,16]
#incoming=[1,2,3,4,9,8,7,6,5,10,11,12,13,16,15,14]

def get_inputs():
    while True:
        try:
            tiles = (input("\nType the tile values seperated by a space: \n").split(' '))
            input_list = [int(tile) for tile in tiles]
            input_set = set(input_list)
            i, j = 1, 17
            puzzle_range = all(num >= i and num < j for num in input_list)
        except ValueError:
            print("\nplease only numerical numbers")
            continue
        if len(input_list) < 15:
            print("\nnot enough tiles entered")
            if len(input_set) != len(input_list):
                find_duplications(input_list, input_set)
        if len(input_list) > 16:
            print("\ntoo many tiles entered")
            if len(input_set) != len(input_list):
                find_duplications(input_list, input_set)
        if len(input_list) == 15:
            if len(input_set) != len(input_list):
                find_duplications(input_list, input_set)
        elif puzzle_range == False:
            print("\ntile entered outside of puzzle range (1-16)")
        else:
            return input_list
        break

def find_duplications(input_list, input_set):
    print("\nduplicate tiles entered:")
    unique = set()
    for num in input_list:
        if num not in unique:
            unique.add(num)
        else:
            unique = unique - set([num])
    dups = (input_set - unique)
    print(dups)
    print("try again")
    get_inputs()

def print_puzzle(incoming):
    print("\n---------------------")
    print(f"| {incoming[0]:^2} | {incoming[1]:^2} | {incoming[2]:^2} | {incoming[3]:^2} |")
    print("---------------------")
    print(f"| {incoming[4]:^2} | {incoming[5]:^2} | {incoming[6]:^2} | {incoming[7]:^2} |")
    print("---------------------")
    print(f"| {incoming[8]:^2} | {incoming[9]:^2} | {incoming[10]:^2} | {incoming[11]:^2} |")
    print("---------------------")
    print(f"| {incoming[12]:^2} | {incoming[13]:^2} | {incoming[14]:^2} | {incoming[15]:^2} |")
    print("---------------------\n")

def find_incoming_parity(incoming):
    blank_space = incoming.index(16)
    parity = parity_array[blank_space]
    incoming_parity = 'unknown'
    if parity == 'E':
        incoming_parity = 'EVEN'
        return incoming_parity
    elif parity == 'O':
        incoming_parity = 'ODD'
        return incoming_parity
    else:
        return incoming_parity

def find_incoming_transpositions(incoming):
    #make a deep copy of incoming array to not alter orginal
    transposed=incoming.copy()
    transposition_count = 0
    # it prints the first line as the incoming and if there's another transposition will print the current state of the transposed list
    for i in range(len(transposed)):
        if transposed[i] != home[i]:
        # see the steps of each transposition line by line
            print(transposed)
        # find index value of next tile needed
            transpose = transposed.index(home[i])
        # swaping index values
            transposed[i], transposed[transpose] = transposed[transpose], transposed[i]
        # add to transposition count
            transposition_count += 1
    if transposed != home:
        raise Exception("transposition unsuccessful")
    # prints the final completed transposed incoming input
    print(transposed)
    return transposition_count

def solvable(solution_parity, solution_transpositions):
    if (((solution_transpositions)%2) == 0) & (solution_parity == 'EVEN'):
        print("the puzzle is solvable\n")
    elif (((solution_transpositions)%2) == 1) & (solution_parity == 'ODD'):
        print("the puzzle is solvable\n")
    else:
        print("the puzzle is NOT solvable\n")

# the natural or home condition of the puzzle and the parity of a 4x4 home field
home=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
parity_array=["E","O","E","O","O","E","O","E","E","O","E","O","O","E","O","E"]

print(" . . . . . 15 puzzle validity check . . . . .\nChecks if a user defined 15 puzzle is solvable\n")
print("Enter the tile values starting from the TOP row moving LEFT to RIGHT.\nThen do the same for the next row below till you reach the BOTTOM row\n")
print("Enter the blank space as '16'")
print("Only enter values 1 through 16")

incoming = get_inputs()
# copy TEST CASES for 'incoming'
print_puzzle(incoming)

solution_transpositions = find_incoming_transpositions(incoming)
solution_parity = find_incoming_parity(incoming)

print(f"\nthe number of transpositions is: {solution_transpositions}")
print(f"the parity of the solution is: {solution_parity}")
solvable(solution_parity, solution_transpositions)