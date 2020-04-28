numList = list()

while(True):
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    numList.append(value)

print('Maximum:', max(numList))
print('Minimum:', min(numList))
