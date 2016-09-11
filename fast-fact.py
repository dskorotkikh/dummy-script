#!/usr/bin/env python3
import sys
import math

def may_be_size(n, k):
	return (n/k)**0.5 * (1 + k - 2 * k**0.5)

def bin_pow(base, pw, mod):
	if pw == 0:
		return 1
	if pw == 1:
		return base % mod
	
	answ = bin_pow(base, pw//2, mod)
	answ = (answ * answ) % mod
	if pw % 2 == 1:
		answ = (answ * base) % mod
	return answ


def xgcd(b, n):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, b, n = b // n, n, b % n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return  b, x0, y0

def invert(val, mod):
	g, x, y = xgcd(val, mod)
	return (x % mod + mod ) % mod

def mitm(base, end, size, mod):
	# baby_steps = bintrees.FastAVLTree()
	baby_steps = {}

	giant_step_size = int(size**0.5)
	giant_step = bin_pow(base, giant_step_size, mod)
	step_back = invert(base, mod)
	baby_steps[end] = 0
	
	for i in range(1, giant_step_size):
		end = (end * step_back) % mod
		baby_steps[end] = i

	cbase = 1
	for i in range(giant_step_size):
		cbase = (cbase * giant_step) % mod
		if cbase in baby_steps :
			return (giant_step_size * (i+1) + baby_steps[cbase])

def bin_search(phi, mod):
	sm = mod - phi + 1
	l = 1
	r = sm // 2
	while True:
		m = (l + r) // 2
		c = (sm-m)*m 
		if c == mod :
			return sm-m, m

		if (sm-m)*m > mod :
			r = m-1
		else:
			l = m+1


base = 2
n = int(input("Enter a numer for factorization: "))
scale = float(input("Enter upper bound of the ratio factors: "))

# n = int('965718CFB8D95BB428BB91E035F4419', 16)	#124bit
# n = int('D3A5E76D05434AF243319D29FB3E91', 16)		#120bit
# n = int('2B40C2FECF1599351B9C1FB0957E9', 16)		#114bit
# n = int('2AB69932076246079FFE98782BF5', 16)		#110bit
# n = int('C732D1820ABC3E2E0DEF8DA1F8F', 16)		#108bit
# n = int('C5965E878687B9D4650965BD9', 16)		#100bit
# n = int('C909228DF0606DD23BABE199', 16)		#96bit
# n = int('A4639FCBCFDBBF31707601', 16)			#88bit
# n = int('BBDE063D957B4C8EF09D', 16)			#80bit
# n = int('349BAD29860D95DABE7', 16)			#74bit
# n = int('CF92644E65955889', 16)			#64bit
# p = 1223
# q = 1747
# p = 10**9+7
# q = 1073676287
# n = p * q

pw = n - 2*int(n**0.5)
pw -= pw % 4
end = bin_pow(base, pw, n)
size = int(may_be_size(n, scale))

print (math.ceil(math.log(n, 2)), 'bit', sep='-')

df = mitm(base**4, end, size//4+1, n)
if df is not None:
	df *= 4
	phi = (pw - df)
	p, q = bin_search(phi, n) 
	print ('p = {0}, q = {1}'.format(p, q))
