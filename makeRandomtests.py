#!/usr/bin/env python3
import os
import random
import string


def random_name():
	return ''.join(random.choice(string.ascii_uppercase +string.digits) for _ in range(12))


os.chdir('test_folder')



