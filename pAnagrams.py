# This Python file uses the following encoding: utf-8
import os, sys

def build_dict(path):
	alpha={}
	f=open(path,"r")
	for line in f.readlines():
		line=line.strip()
		key=sorted_line(line)

		if key in alpha:
			v=alpha.get(key)+","+line
			alpha[key]=v
		else:
			alpha[key]=line
	return alpha
def sorted_line(line):
	chars=[c for c in line]
	chars.sort()
	return "".join(chars)

def anagram(alpha,line):

	key=sorted_line(line)
	values=alpha.get(key,"NONE")
	return values.split(",")


alpha=build_dict(r"persian_word_list.txt")
results=anagram(alpha,str(sys.argv[1]))
rfile=open('results.txt','w')
for item in results:
	rfile.write("%s\n" % item)
print("Anagrams for "+str(sys.argv[1])+" was written to results.txt file.")
print("results num: "+str(len(results)))


