import os, sys; sys.path.append(os.path.join("..", "..", ".."))

from pattern.web import URL, Document, plaintext
from pattern.web import NODE, TEXT, COMMENT, ELEMENT, DOCUMENT

#dom is just for downloading whole html for the website till now didn't now what to do do exactly with it

dom = Document(URL("http://en.wikipedia.org/wiki/Machine_learning").download())
clean
print dom
