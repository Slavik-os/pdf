#!/usr/bin/env python3
import re

num = '8233.08€'

reg = re.compile('\d{1,}\.\d{1,}')

print(reg.findall(num))
