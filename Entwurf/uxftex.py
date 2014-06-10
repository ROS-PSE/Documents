#!/usr/bin/python

import sys
import xml.etree.ElementTree as ET

inputfile = ""
outputfile = ""
d = True

def writeToFile(data):
	with open(outputfile, "a") as myfile:
		myfile.write("\section " + data["classname"] + "\n")
		myfile.write(data["description"] + "\n")
		myfile.write("\n")
		if "attributes" in data.keys() and len(data["attributes"]) > 0:
			myfile.write("\subsection Attributes\n")
			myfile.write("\\begin{itemize}\n")
			for a in data["attributes"]:
				myfile.write("\\item " + a["visibility"] + " " + a["type"] + " " + a["name"] + "\nTODO: Description\n")
			myfile.write("\\end{itemize}\n")
		if "methods" in data.keys() and len(data["methods"]) > 0:
			myfile.write("\subsection Methods\n")
			myfile.write("\\begin{itemize}\n")
			for a in data["methods"]:
				myfile.write("\\item " + a["visibility"] + " " + a["type"] + " " + a["name"] + "\nTODO: Description\n")
			myfile.write("\\end{itemize}\n")

def visibility(symbol):
	if symbol == "-":
		return "private"
	elif symbol == "#":
		return "protected"
	elif symbol == "+":
		return "public"
	elif symbol == "~":
		return "package"
	else:
		return "public"

def parsePnl(pnlattr):
	cursor = 0
	result = {}
	if d:
		result["classname"] = pnlattr[0]
		result["description"] = "\n".join(pnlattr[1:])
	else:
		state = 0
		# classname irgendwie machen
		result["attributes"] = []
		result["methods"] = []
		k = ["classname", "attributes", "methods"]
		while cursor < len(pnlattr):
			line = pnlattr[cursor]
			if line == "--":
				state += 1
			if state in range(1, 2):
				o = {}
				if line[1] == " ":
					o["visibility"] = visibility(line[0])
					line = line[2:]
				x = line.split(":")
				o["type"] = x[-1]
				o["name"] = ":".join(x[0, -1]).strip()
				result[k[state]].add(o)
			cursor += 1
	return result

def readFile():
	tree = ET.parse(inputfile)
	root = tree.getroot()
	for element in root:
		if element.tag == "element":
			if element.find('type').text == "com.umlet.element.Class":
				pnlattr = element.find('panel_attributes').text
				if not pnlattr == "100%":
					writeToFile(parsePnl(pnlattr.split('\n')))

def clearFile(f):
	open(f, 'w').close()

def main(args):
	global inputfile, outputfile
	if len(args) < 1:
		print("give an input file")
		sys.exit(1)
	else:
		inputfile = args[0]
	if len(args) >= 2:
		outputfile = args[1]
	else:
		outputfile = inputfile[0:-3] + "tex"
	clearFile(outputfile)
	readFile()

if __name__ == "__main__":
	main(sys.argv[1:])