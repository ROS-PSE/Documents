#!/usr/bin/python
# -*- coding: utf8 -*-

import sys
import xml.etree.ElementTree as ET
import re

inputfile = ""
outputfile = ""
d = False

def writeToFile(data):
	with open(outputfile, "a") as myfile:
		myfile.write("\n\n\subsection{" + data["classname"].strip() + "}\n")
		myfile.write(data["description"] + "\n")
		myfile.write("\n")
		if "attributes" in data.keys() and len(data["attributes"]) > 0:
			myfile.write("\subsubsection{Attributes}\n")
			myfile.write("\\begin{itemize}\n")
			for a in data["attributes"]:
				if "visibility" in a:
					myfile.write("\t\\item " + a["visibility"] + " " + a["type"] + " " + a["name"] + "\\\\\n\t" + a["description"] + "\n")
			myfile.write("\\end{itemize}\n")
		if "methods" in data.keys() and len(data["methods"]) > 0:
			myfile.write("\subsubsection{Methods}\n")
			myfile.write("\\begin{itemize}\n")
			for a in data["methods"]:
				if "visibility" in a:
					myfile.write("\t\\item " + a["visibility"] + " " + a["type"] + " " + a["name"] + "\\\\\n\t" + a["description"] + "\n")
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
		result["classname"] = ""
		result["description"] = "TODO: Description"
		result["attributes"] = []
		result["methods"] = []
		k = ["classname", "attributes", "methods"]
		o = {}
		desc = False
		while cursor < len(pnlattr):
			line = pnlattr[cursor]
			# line = re.sub(r'/(.*)/', '\\\\textit{\\1}', line)
			line = line.replace('_', '\_')
			if line == "--":
				state += 1
				cursor += 1
				continue
			if state == 0:
				# if line[0].encode('utf8') == u"\u00AB".encode('utf8'):
					# result["classname"]+= line[1:-1].capitalize() + " "
				if line[0:2] == "//":
					result["description"] = line[2:].strip()
				else:
					result["classname"]+= line + " "
			if state == 1 or state == 2:
				abstract = False
				if line[0] == "/":
					if line[1] == "/":
						# comment
						o["description"] = line[2:].strip()
						cursor += 1
						continue
					else:
						# abstract
						abstract = True
						line = line[1:-1]
				if line[0] in ["-", "+", "~"]:
					o["visibility"] = visibility(line[0])
					if abstract:
						o["visibility"] += " abstract"
					line = line[1:]
				x = line.split(":")
				o["type"] = x[-1]
				o["name"] = ":".join(x[0:-1]).strip()
				if not "description" in o:
					o["description"] = "TODO: Description"
				result[k[state]].append(o)
				o = {}
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