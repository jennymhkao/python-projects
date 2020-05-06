'''Rewrite the program that prompts the user for a list of 
numbers and prints out the maximum and minimum of the numbers 
at the end when the user enters "done". Write the program to 
store the numbers the user enters in a list and use the max() 
and min() functions to compute the maximum and minimum numbers 
after the loop completes.
'''

numList = list()

while(True):
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    numList.append(value)

print('Maximum:', max(numList))
print('Minimum:', min(numList))
