#!/usr/bin/env python3

import cgi;

#Debugging output
import cgitb

#Send errors to browser
cgitb.enable

#Print HTML MIME-TYPE header
print ("Content-type:text/html\n")
print()


ID=("ID")
acc=("acc")
prod=("prod")
loc=("loc")

data=[1,2,3,4,5,6,7,8,9]

#Create summary list table
html = "<html>\n"
html += "<head>\n"
html += "<title>RGR3 Genome Browser</title>\n"
html += "</head>\n\n"
html += "<body>\n"
html += "<table>\n"
for row in data:
    html += "<tr>\n"

html += "</body>\n"
html += "</html>\n"