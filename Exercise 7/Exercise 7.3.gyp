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

