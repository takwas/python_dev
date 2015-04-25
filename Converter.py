
# This module provides a series of conversion
# functions.
#
# This is solely for my practice.
#
#

import math


zero = 0

def far_to_cel(farenheit_val):
	far_const_1 = 32
	far_const_2 = 1.8
	
	return (farenheit_val-far_const_1)/far_const_2

def cel_to_far(celsius_val):
	far_const_1 = 32
	far_const_2 = 1.8
	
	return far_const_1+(celsius_val*fa)

def naria_to_doll():
	return zero

def doll_to_naira():
	return zero

def pnd_to_doll():
	return zero

def doll_to_pnd():
	return zero

def naira_to_pnd():
	return zero

def pnd_to_naira():
	return zero


def hex_to_dec(hex):
	map = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12,'D':13, 'E':14, 'F':15}
	hex_str = str(hex)
	hex_ls = []
	high_pow = len(hex)-1
	hex_base = 16
	dec = 0
	
	for char in hex_str:
		hex_ls += list(char)
	
	for item in hex_ls:
		dec += map.get(item) * math.pow(hex_base, high_pow)
		high_pow -= 1
	
	return int(dec)
	
