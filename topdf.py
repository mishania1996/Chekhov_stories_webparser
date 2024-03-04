#Takes stories from '/stories' and makes a tex file in 'notestopdf'
import os
import re
import longstrings

os.mkdir('notestopdf')
os.mkdir('notestopdf/TeX_files')

directory = 'stories'


#sort the list of files based on the first modified time

files_times = [(file, os.path.getmtime(directory+'/'+file)) for file in os.listdir(directory)] 
files_sorted = sorted(files_times, key = lambda x : x[1])

#creates main tex file

with open(r"notestopdf/main.tex", 'w') as f:
    f.write(longstrings.maintexbeginning)

j=1 #index of a current book
for file, _ in files_sorted: #get a file from /stories
	storyfile = open(directory+'/'+file)
	x = storyfile.readlines()
	n = len(x)
	if len(x[0]) < 300:
	    title = x[0] #title consists of the first line and possibly next lines if they have no lower chars (but if else case is created to take care of the exceptional case
	else:
	    title = ' '
	storytxt = ''
	get_title = True
	
	for i in range(1,n-4):
		if get_title:
			lowerchars = re.search('[а-я]', x[i])
			if not lowerchars:
				title += x[i] 
				continue
			else:
				get_title = False
		storytxt += "\n" + x[i]
	#maintex appending include chapter lines
	with open(r"notestopdf/main.tex", 'a') as f:
	    f.write(r"\include{./TeX_files/chapter" + str(j)+r"}" + "\n")
	
	#creating a chapter file
	with open(r"notestopdf/TeX_files/chapter" + str(j) + ".tex" , 'w') as f:
	    f.write(r"\chapter{" + title + "}\n" + storytxt)
	
	j += 1
	
#maintex final edit
with open(r"notestopdf/main.tex", 'a') as f:
    f.write(longstrings.maintexending)
	
