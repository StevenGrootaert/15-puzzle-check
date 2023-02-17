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
        raise Exception("duplicate tiles entered:" + str(dups))
    elif (puzzle_range == False):
        raise Exception("input outside of puzzle range (1-16)")

def get_inputs():
    while True:
        try:
            tiles = (input("\nType the tile values seperated by a space: \n").split(' '))
            input_list = [int(tile) for tile in tiles]
            input_set = set(input_list)
            assert_valid_input(input_list,input_set)
        except ValueError as v:
            print("\nonly numbers please: " + str(v.args))
            continue
        except Exception as e:
            print("\nbad input: " + str(e)) 
            continue
        else:
            return input_list
        break

def find_duplications(input_list, input_set):
    unique = set()
    for num in input_list:
        if num not in unique:
            unique.add(num)
        else:
            unique = unique - set([num])
    duplications = (input_set - unique)
    return duplications

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
    transposed=incoming.copy()
    transposition_count = 0
    for i in range(len(transposed)):
        if transposed[i] != HOME[i]:
            transpose = transposed.index(HOME[i])
            transposed[i], transposed[transpose] = transposed[transpose], transposed[i]
            transposition_count += 1
    if transposed != HOME:
        raise Exception("transposition unsuccessful")
    return transposition_count

def print_transpositions(incoming):
    transposed=incoming.copy()
    for i in range(len(transposed)):
        if transposed[i] != HOME[i]:
            print(transposed)
            transpose = transposed.index(HOME[i])
            transposed[i], transposed[transpose] = transposed[transpose], transposed[i]
    print(transposed)

def check_solvable(solution_parity, solution_transpositions):
    if (((solution_transpositions)%2) == 0) & (solution_parity == 'EVEN'):
        return True
    elif (((solution_transpositions)%2) == 1) & (solution_parity == 'ODD'):
        return True
    else:
        return False
