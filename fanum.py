import sys
import re

def main():
	infile = "";
	outfile = "";
	prefix = "FA"
	if len(sys.argv) < 2:
		infile = input("Please give an input file:\n")
	else:
		infile = sys.argv[1]
	if len(sys.argv) < 3:
		outfile = str(input("Please give an output file\nType 0 for output to the console\nType 1 to overwrite the input file:\n"))
	else:
		outfile = sys.argv[2]
	if outfile == "1":
		outfile = infile
	if len(sys.argv) == 4:
		prefix = sys.argv[3]

	content = []
	with open(infile) as f:
		content = f.readlines()

	globcounter = 0
	subcounter = 0
	output = []
	for x in range(len(content)):
		content[x] = content[x].rstrip()
		m = re.search('(\s*)(%?)(.*)', content[x])
		if len(content[x]) > 0 and len(m.group(2)) < 1:
			if len(m.group(1)) == 0:
				subcounter = 0
				globcounter += 100
			else:
				subcounter += 10
			nr = "{0:0>4}".format(globcounter + subcounter)
			line = "\\item[/" + prefix + nr + "/] " + content[x].strip()
			output.append(line)
		else:
			output.append("")

	if outfile == "0":
		print("------------------")
		for i in range(len(output)):
			print(output[i])
	else:
		f = open(outfile,'w')
		for i in range(len(output)):
			f.write(output[i] + "\n")
		f.close()


if __name__ == "__main__":
	main()