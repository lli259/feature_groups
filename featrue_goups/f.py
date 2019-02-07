import re
with open("f.txt") as f:
	lines=f.read()
	#print(lines)
	f=re.findall(r"'\w+'",lines)
	for i in f:
		print(i)
