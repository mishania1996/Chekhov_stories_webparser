# Chekhov_stories_parser
Parses stories from a website and creates a pdf book out of it.

This python3 script scrapes short stories from chehov-lit.ru and eventually compiles the stories into a PDF format.

Libraries used:
BeautifulSoup4, time, re, os, and requests.

How to run:
1.Execute main.py to run the script. This will create text files in '/stories' 

2.Execute topdf.py. This will write a tex code in '/notestopdf' which can be compiled to a pdf book using TeXstudio.

Components:
'parsestory.py': This module contains a function that takes URL of a story and writes its content into a text file within the '/stories' directory.
'main.py': This script navigates through story links on http://chehov-lit.ru/chehov/text/rasskazy.htm, identifies the story links, and invokes 'parsestory.py' for each story.

Ethics:
To avoid overloading the website's servers, the script includes 2-second delay after parsing each story.

License:
This project is licensed under MIT License.
