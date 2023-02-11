# the natural or home condition of the puzzle and the parity of a 4x4 home field
HOME=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
PARITY_ARRAY=["E","O","E","O","O","E","O","E","E","O","E","O","O","E","O","E"]

def assert_valid_input(input_list,input_set):
    i, j = 1, 17
    puzzle_range = all(num >= i and num < j for num in input_list)
    if len(input_list) < 16:
        raise Exception("not enough tiles entered")
    elif len(input_list) > 16:
        raise Exception("too many tiles entered")
    elif len(input_set) != len(input_list):
        dups = find_duplications(input_list,input_set)
        raise Exception("There are duplicates:" + str(dups))
    elif (puzzle_range == False):
        raise Exception("input outside of puzzle range (1-16)")

def get_inputs(): #would be nice to add an exit/escape program ?
    while True:
        try:
            tiles = (input("\nType the tile values seperated by a space: \n").split(' '))
            input_list = [int(tile) for tile in tiles]
            input_set = set(input_list)
            assert_valid_input(input_list,input_set)
        except Exception as e:
            print("\nbad input: " + str(e)) 
            continue
        else:
            return input_list
        break

def find_duplications(input_list, input_set):
    # print("\nduplicate tiles entered:")
    unique = set()
    for num in input_list:
        if num not in unique:
            unique.add(num)
        else:
            unique = unique - set([num])
    dups = (input_set - unique)
    
    return dups

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
    parity = PARITY_ARRAY[blank_space]
    incoming_parity = 'EVEN'
    if parity == 'O':
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
        if transposed[i] != HOME[i]:
        # see the steps of each transposition line by line
            print(transposed)
        # find index value of next tile needed
            transpose = transposed.index(HOME[i])
        # swaping index values
            transposed[i], transposed[transpose] = transposed[transpose], transposed[i]
        # add to transposition count
            transposition_count += 1
    if transposed != HOME:
        raise Exception("transposition unsuccessful")
    # prints the final completed transposed incoming input
    print(transposed)
    return transposition_count

def solvable(solution_parity, solution_transpositions):
    if (((solution_transpositions)%2) == 0) & (solution_parity == 'EVEN'):
        print("the puzzle is solvable\n")
        return True
    elif (((solution_transpositions)%2) == 1) & (solution_parity == 'ODD'):
        print("the puzzle is solvable\n")
        return True
    else:
        print("the puzzle is NOT solvable\n")
        return False
