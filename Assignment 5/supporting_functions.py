import subprocess
from constants import *
import numpy as np

def get_val_ch(char):
    return (ord(char) - ord('a'))%16

def str_to_int(pair):
    val1 = (letters.index(pair[0]) - letters.index  ('f'))%16
    val2 = (letters.index(pair[1]) - letters.index('f'))%16
    return val1 * 16 + val2

def int_to_str(val):
    val1 = val//16
    val2 = val%16
    ix1 = (letters.index('f') + val1)%16
    ix2 = (letters.index('f') + val2)%16
    return letters[ix1] + letters[ix2]

def pair_to_poly(pair):
    p = []
    val = str_to_int(pair)
    for i in range(7):
        p.append(val%2)
        val//=2
    p.reverse()
    p = np.poly1d(p)
    return p

def poly_to_pair(poly):
    pair = ""
    val = 0
    coeff = np.append(np.zeros(7 - poly.c.size), poly.c)
    for i in range(7):
        val += 2**(6 - i) * coeff[i]
    val = int(val)
    pair = int_to_str(val)
    return pair 

def int_to_poly(n):
    p = pair_to_poly(int_to_str(n))
    return p

def poly_to_int(p):
    n = str_to_int(poly_to_pair(p))
    return n

def add_poly(p1, p2):
    p3 = p1 + p2
    p = []
    for c in p3.c:
        p.append(int(abs(c)%2))
    p = np.poly1d(p)
    return p

def mult_poly_back(p1, p2):
    p3 = p1 * p2
    p3 = (p3/IRR_7_POLY)[1]
    p = []
    for c in p3.c:
        p.append(int(abs(c)%2))
    p = np.poly1d(p)
    return p

MULT_MAT = np.zeros((128, 128), dtype=np.int32)
for i in range(128):
    a = int_to_poly(i)
    for j in range(128):
        b = int_to_poly(j)
        c = mult_poly_back(a, b)
        c = poly_to_int(c)
        MULT_MAT[i][j] = c

def mult_poly(p1, p2):
    a = poly_to_int(p1)
    b = poly_to_int(p2)
    return int_to_poly(MULT_MAT[a][b])
    
POWER_MAT = np.zeros((127,128), dtype=np.int32)
for i in range(128):
    a = int_to_poly(i)
    temp = int_to_poly(i)
    mypower = 1
    POWER_MAT[mypower][i] = poly_to_int(temp)
    for j in range(2,127):
        temp = mult_poly(temp, a)
        mypower+=1
        POWER_MAT[mypower][i] = poly_to_int(temp)

def power_poly(p, n):
    val = poly_to_int(p)
    return int_to_poly(POWER_MAT[n][val])