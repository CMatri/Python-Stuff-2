import sys

f = open(sys.argv[1], 'r')
f.seek(0xA, 0)
f.seek(ord(f.read()[0]), 0)
exec(f.read().replace('\x00', ''))