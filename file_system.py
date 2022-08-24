import sys, os

print(f'File: {__file__}')
print(f'Args: {sys.argv}')
sfile = os.path.abspath(sys.argv[0])
print(f'Reading: {sfile}')


if not os.path.exists(sfile):
    print('File not found')
    exit(1)

f = open(sfile, 'r')
line = f.readline()
print(line)

chars = f.read(10)
print(f'Chars: *{chars}*')

# Positions
print(f'Position: {f.tell()} of {os.stat(sfile).st_size}')

# seek
f.seek(10)
print(f'Position: {f.tell()} of {os.stat(sfile).st_size}')

print('--------------------------------')
for l in f.readlines():
    print(l.strip())

# close the files
f.close()
