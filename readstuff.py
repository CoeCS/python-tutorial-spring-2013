# readstuff.py --- read and print lines from a file

infile = open('in.txt', 'r')

outfile = open('out.txt', 'w')

for line in infile:
    s = line.upper()
    outfile.write(s)

