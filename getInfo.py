#!/usr/bin/env python3 
from pprint import pprint
from removeDup import * 
import pylightxl as xl 
import pdfplumber
from openpyxl import load_workbook
import re 
import os
#conversion = pdftables_api.Client('v3lvfs4bh8nv')
#conversion.xlsx('invoice2.pdf','output')
#file = 'output.xlsx'

def main() : 
	os.chdir('test_folder')
	for file in os.listdir('.') :
		if file.endswith('.pdf') :
			print(find_values(file))

def find_values(file_name) :
	reg = re.compile(r'\$?\d{1,}\s?\d{1,},\d{1,}\s?€?\.?\d{1,}|\$\d{1,}\.\d{1,}\.|\$\d{1,}\.\d{1,}')
	regR = re.compile(r'\d{1,}\.\d{1,}')
	with pdfplumber.open(file_name) as pdf  :
		first_page = pdf.pages[0]
		pdfText = first_page.extract_text()
		l = sorted(reg.findall(pdfText))
		l = [x.replace(' ','').replace(',','.') for x in l]
		l = removeDup(l)
		l = [float(regR.findall(x)[0]) for x in l]
		l = sorted(l,key=float)
		TTCTOTAL = l[-1]
		HT = l[-2]
		TTC = TTCTOTAL-HT	
		return (str(TTCTOTAL).replace('.',','),str(HT).replace('.',','),str(round(TTC,4)).replace('.',','))		


if __name__ == '__main__' :
	main()
