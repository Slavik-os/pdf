#!/usr/bin/env python3

def removeDup(l):
	b = []
	for i in l :
		if i not in b :
			b.append(i)
	return b 


if __name__ == '__main__' :
	print(removeDup(['1','1','2','3']))
