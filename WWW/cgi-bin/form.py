#!/usr/bin/env python3
#file for index page on gene analysis submission
import cgi;

#Debugging output
import cgitb

#Send errors to browser
cgitb.enable	

#Grab form contents
form = cgi.FieldStorage()

#Get data from fields:
#Radio button search
if form.getvalue("search_type"):
    search_type = form.getvalue("search_type")
else:
    search_type = "None"

#Entered data
if form.getvalue("data"):
    data = form.getvalue("data")
else:
    data = "None entered"

#analysis type checkbox 
an_type  = form.getlist("an_type")
#sticky end option menu
sticky_ends = form.getlist("sticky_ends")

#Print HTML MIME-TYPE header
print ('Content-type:text/html\n')
print()
html ='<!DOCTYPE html>\n'
html += '<html>\n'
html += '<head>\n'
html += '<meta charset="utf-8">\n' 
html += '<title>RGR3 Genome Browser</title>\n'

#css stylesheet for page
html += '<link type="text/css" rel="stylesheet" href="http://student.cryst.bbk.ac.uk/~sr002/css/rgr3.css">\n'
#css stylesheet for codon frequencies frame to override the iframe size on the index page in css/rgr3.css
html += '<link type="text/css" rel="stylesheet" href="http://student.cryst.bbk.ac.uk/~sr002/css/codonsz.css">\n'
html += '</head>\n\n'
html += '<body>\n'

#header
html += '<header>\n'
html += '<h1>RGR <span class="red">3</span> Genome Browser</h1>\n'
html +=	'<h2>Homo sapiens (Human) Chromosome 3</h2>\n' 
html += '</header>\n'

#navigation toolbar
html += '<nav>\n'
html += '<ul>\n'
html +=	'<li><a href="http://student.cryst.bbk.ac.uk/~sr002/index.html">HOME</a></li>\n'
html +=	'<li><a href="http://student.cryst.bbk.ac.uk/~sr002/codon.html">CODON FREQUENCIES</a><li>\n'
html += '<li><a href="http://student.cryst.bbk.ac.uk/~sr002/about.html">ABOUT</a></li>\n'
html +=	'<li><a href="http://student.cryst.bbk.ac.uk/~sr002/help.html">HELP</a></li>\n'
html +=	'</ul>\n'	
html += '</nav>\n'

html += '<h2>RGR<span class="red">3</span> Genome Browser Results</h2>\n'

#search_type value
html += '<p>You searched on: <b>' + search_type + '</b></p>\n'
html += '<p>Value entered: <b>' + data + '</b></p>\n'

html += '<p><b>The following types of analysis were performed:</b></p>\n'

#Return unordered list of analysis type chosen
html += '<ul>'
for a in an_type:
    if a == "dna_seq":
        html += '<li>Compete DNA sequence</li>\n'
    if a == "aa_seq":
        html += '<li>Amino acid sequence</li>\n'
    if a == "codon":#Insert codon table
        html += '<iframe src ="http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/sr002/codon.py"></iframe>\n'

#return result of the sticky enzyme data entry chosen
for v in sticky_ends:
    if v == "EcoRI":
        html += '<li>EcoRI</li>\n'
    if v == "BamHI":
        html += '<li>BamHI</li>\n'
    if v == "BsuMI":
        html += '<li>BsuMI</li>\n' 
html += '</ul>\n'

html += '<footer>\n'
#CSS level 3 Validated
html += '<p>\n'
html += '<a href="http://jigsaw.w3.org/css-validator/check/referer">\n'
html += '<img style="border:0;width:88px;height:31px" src="http://jigsaw.w3.org/css-validator/images/vcss-blue" alt="Valid CSS!" />\n'
html += '</a>\n'
html += '</p>\n'
html += '</footer>\n'

html += '</body>\n'
html += '</html>\n'

print(html)
