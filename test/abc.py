#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 03:16:28 2017

@author: parth
"""

import graphviz as gv
from lxml import html

raw = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<title>Kalpdrum Passi</title>
</head>
<body background="blank_arrow.gif">
<h1>Kalpdrum Passi</h1>
<table border="0" width="80%">
<tr><td><img src="kalpdrum.jpg" width="340" height="400" alt="Kalpdrum
 Passi"></td>
 <td>Kalpdrum Passi<br>
 <a href="http://www.cs.laurentian.ca">Department of Mathematics &amp Computer
 Science</a><br>
 <a href="http://www.laurentian.ca">Laurentian University</a><br>
Ramsey Lake Rd.<br>
Sudbury, Ontario<br>
Canada P3E 2C6<br><br>
Phone: (705)675-1151 x2345<br>
Fax: (705)673-6591<br>
email: kpassi AT cs.laurentian.ca<br>
 </td>
</tr>
</table>
<p>&nbsp</p>
<hr>
<h2>Courses</h2>
<h3 style="text-indent: .5in;">Fall 2005</h3>
<ul style=text-indent:.5in;">
 <li><a href="cosc2307.html">COSC 2307: Database Programming</a>
 <li><a href="cosc3407.html">COSC 3407: Operating Systems I</a>
</ul>
<h3 style="text-indent:.5in;">Winter 2006</h3>
<ul style=text-indent:.5in;">
 <li><a href="cosc3406.html">COSC 3406: Computer Organization</a>
 <li><a href="cosc4806.html">COSC 4806: Web Data Management</a>
</ul>
<h3 style="text-indent:.5in;">Spring 2003</h3>
<ul style=text-indent:.5in;">
 <li><a href="cosc4606.html">COSC 4606: Database Management Systems</a>
</ul>
</body>
</html>"""

def traverse_tree(parent, graph, labels):
    labels[parent] = parent.tag
    graph.node = parent.tag
    for node in parent.getchildren():
        graph.edge(parent.tag, node.tag)
        traverse_tree(node, graph, labels)

g1 = gv.Graph(format='png')

labels = {}     # needed to map from node to tag
html_tag = html.document_fromstring(raw)
traverse_tree(html_tag,g1,labels)
#print(g1.source)
g1.render('img/hypertree')