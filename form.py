#!/usr/bin/env python3

import cgi;

#Debugging output
import cgitb

#Send errors to browser
cgitb.enable	

#Grab form contents
form = cgi.FieldStorage()

#Get data from fields:
#Radio button search
search_type = form.getvalue("search_type")
#Entered data
    data = form.getvalue("data")
else:
    data = "None entered"

#Entered sequence
    seq = form.getvalue("seq")
else:
    seq = "None entered"


#analysis type checkbox 
an_type  = form.getlist("an_type")

#Print HTML MIME-TYPE header
print ("Content-type:text/html\n")
print()
html = "<html>\n"
html += "<head>\n"
html += "<title>RGR3 Genome Browser</title>\n"
html += "</head>\n\n"
html += "<body>\n"
html += "<h2>RGR3 Genome Browser Results</h2>\n"

html += "<p>You searched on: <b>" + search_type + "</b></p>\n"
html += "<p>Value entered: <b>" + data + "</b></p>\n"

#sequence textarea
html += "<h2>Your sequence was:</h2>\n"





html += "<p><b>The following types of analysis were performed:</b></p>\n"

#Return unordered list of analysis type chosen
html += "<ul>"
    if a == "EcoRI":
    if a == "BamHI":
    if a == "BsuMI":

html += "</body>\n"
html += "</html>\n"

print(html)