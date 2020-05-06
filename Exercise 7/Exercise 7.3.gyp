'''Modify the program that prompts the user for the file name so 
that it prints a funny message when the user types in the exact 
file name "na na boo boo". The program should behave normally for 
all other files which exist and don't exist.
'''

fname = input('Enter the file name: ')
if fname == "na na boo boo" :
    print("NA NA BOO BOO TO YOU - You've been punk'd!")
try:
    fhand = open(fname)
    inp = fhand.read()
    print(len(inp))
except: 
    print('File cannot be opened:', fname)
    exit()

