#!/usr/bin/env python3

import cgi;

#Debugging output
import cgitb

#Send errors to browser
cgitb.enable

#Print HTML MIME-TYPE header
print ('Content-type:text/html\n')
print()


ID=("ID")
acc=("acc")
prod=("prod")
loc=("loc")

data=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

#Create summary list table
html ='<!DOCTYPE html>\n'
html += '<html>\n'
html += '<head>\n'
html += '<title>RGR3 Genome Browser</title>\n'
html += '<link type="text/css" rel="stylesheet" href="http://student.cryst.bbk.ac.uk/~sr002/css/sumlist.css">\n'
html += '</head>\n\n'
html += '<body>\n'
html += '<table>\n'
html += '<caption>CHROMOSOME 3</caption>\n'
html += '<tr>\n'
html += '<th>Gene ID</th>\n'
html += '<th>GenBank Accession</th>\n'
html += '<th>Protein product</th>\n'
html += '<th>Chromosomal location</th>\n'
html += '</tr>\n'
for row in data:
    html += '<tr>\n'
    html += '<td>' + ID + '</td>\n'
    html += '<td>' + acc + '</td>\n'
    html += '<td>' + prod + '</td>\n'
    html += '<td>' + loc + '</td>\n'
    html += '</tr>\n'

html += '</table>\n'
html += '</body>\n'
html += '</html>\n'
print(html)
