#!/usr/bin/env python3

import random
import string
from fpdf import *
body = """
Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College 
in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from section
 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of 
Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.

The standard chunk of Lorem Ipsum 
used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.
"""
def random_name():
	return ''.join(random.choice(string.ascii_lowercase+string.digits) for _ in range(12))


pdf = fpdf.FPDF(format='letter') #pdf format
pdf.add_page() #create new page
pdf.set_font("Arial", size=12) # font and textsize
for line in body.split('\n') :
	pdf.cell(200, 10, txt=str(line), ln=1, align="L")
pdf.output("test.pdf")

