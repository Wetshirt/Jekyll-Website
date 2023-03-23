"""
Input: obsidian markdown file
output: jekyll docs post
args: filePath, dstCategory

"""

import argparse
import os

def fileTransformer(path, category):

	print("Transfer " + path + " (Y/N)? ")
	transfer = input()

	if transfer != "" and transfer != "Y" and transfer != "y":
		print('Not Transfer')
		return
	
	# add jekyll front to content
	lines = [
		'---',
		'title: ' + os.path.basename(path),
		'layout: docs',
		'permalink: /:categories/:title/',
		'---'
	]

	content = ''
	for line in lines:
		content = content + line + '\n'

	inputfile = open(path, "r", encoding="utf-8")
	fileData = inputfile.read() 
	print(fileData)

	dstPath = 'docs/' + category + '/_posts/0001-01-99-' + os.path.basename(path)
	outputfile = open(dstPath, "w", encoding="utf-8")
	outputfile.seek(0, 0) 
	outputfile.write(content + '\n'+ fileData) 
	outputfile.close()


	# with open(path, 'r+', encoding="utf-8") as file: 
	#    file_data = file.read() 
	#    file.seek(0, 0) 
	#    file.write(content + '\n'+ file_data) 
	#    file.close()

	# save to category folder

	print ('finished')


def main():

	parser = argparse.ArgumentParser()
	parser.add_argument('-c', '--category')      # option that takes a value

	args = parser.parse_args()
	category = args.category

	# list .md files under folder
	currentPath = os.path.dirname(os.path.realpath(__file__))

	files = []
	# Iterate directory
	for file in os.listdir(currentPath):
		# check only text files
		if file.endswith('.md'):
			files.append(file)
	print(files)

	for f in files:
		fileTransformer(os.path.join(currentPath, f), category) 
    

if __name__ == "__main__":

	main()
