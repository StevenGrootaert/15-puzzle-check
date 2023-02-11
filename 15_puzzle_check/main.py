import fifteen

print(" . . . . . 15 puzzle validity check . . . . .\nChecks if a user defined 15 puzzle is solvable\n")
print("Enter the tile values starting from the TOP row moving LEFT to RIGHT.\nThen do the same for the next row below till you reach the BOTTOM row\n")
print("Enter the blank space as '16'")
print("Only enter values 1 through 16")

incoming = fifteen.get_inputs()

fifteen.print_puzzle(incoming)

solution_transpositions = fifteen.find_incoming_transpositions(incoming)
solution_parity = fifteen.find_incoming_parity(incoming)

print(f"\nthe number of transpositions is: {solution_transpositions}")
print(f"the parity of the solution is: {solution_parity}")
fifteen.solvable(solution_parity, solution_transpositions)
