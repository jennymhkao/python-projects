'''Write a program that reads a file and prints 
the letters in decreasing order of frequency. 
Your program should convert all the input to 
lower case and only count the letters a-z. Your 
program should not count spaces, digits, punctuation, 
or anything other than the letters a-z. Find text 
samples from several different languages and see how 
letter frequency varies between languages. Compare 
your results with the tables at wikipedia.org/wiki/Letter_frequencies.
'''

fname = input('Enter file name: ')
try:    
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
di = dict()

for line in fhand:
    case = line.lower()
    words = case.split()
    for word in words:
        for letter in word:
            if letter in alphabets:
                di[letter] = di.get(letter, 0) + 1
            else:
                continue

ls = list()
for letter, count in di.items():
    newtup = (count, letter)
    ls.append(newtup)

ls = sorted(ls, reverse=True)

num = 0
for count, letter in ls:
    num = num + 1
    print(letter, count)

print(ls[:5])
print(num)




    