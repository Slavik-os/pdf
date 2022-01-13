#!/usr/bin/env python3 
from pprint import pprint
from removeDup import * 
import pylightxl as xl 
import pdfplumber
from openpyxl import load_workbook
import re 
#conversion = pdftables_api.Client('v3lvfs4bh8nv')
#conversion.xlsx('invoice2.pdf','output')
#file = 'output.xlsx'


reg = re.compile(r'[0-9]{1,}\.\d{1,}|\d{1,}\s\d{1,},\d{1,}')
with pdfplumber.open(r'invoice2.pdf') as pdf  :
	first_page = pdf.pages[0]
	pdfText = first_page.extract_text()
	l = sorted(reg.findall(pdfText))
	l = [x.replace(' ','').replace(',','.') for x in l]
	l = removeDup(l)
	TTCTOTAL = float(l[-1])
	HT = float(l[-2])
	TTC = round(TTCTOTAL - HT) 
