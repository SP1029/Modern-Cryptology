import subprocess
import random
from constants import *

def get_val_ch(char):
    return (ord(char) - ord('a'))%16

def str_to_byte(pair):
    val1 = (letters.index(pair[0]) - letters.index('f'))%16
    val2 = (letters.index(pair[1]) - letters.index('f'))%16
    return val1 * 16 + val2

def byte_to_str(val):
    val1 = val//16
    val2 = val%16
    ix1 = (letters.index('f') + val1)%16
    ix2 = (letters.index('f') + val2)%16
    return letters[ix1] + letters[ix2]

def str_to_bits(string):
    val = 0
    for i in range(8):
        val+=str_to_byte(string[2*i:2*(i+1)])
        if i!=7:
            val*=256
    return format(val, '064b')

def bits_to_str(bits):
    string = ""
    for i in range(8):
        val = int(bits[8*i:8*(i+1)],2)
        string = string + byte_to_str(val)
    return string

def bits_to_hex(bits):
    return format(int(bits,2), '016x')

def get_other_xor_string(input_string, xor_val_string):
    other_string = ""
    for i in range(64):
        if input_string[i]==xor_val_string[i]:
            other_string+='0'
        else:
            other_string+='1'
    return other_string

def compute_xor(string1, string2):
    ans = ""
    for i in range(len(string1)):
        if string1[i]==string2[i]:
            ans+='0'
        else:
            ans+='1'
    return ans

def compute_and(string1, string2):
    ans = ""
    for i in range(len(string1)):
        if string1[i]==string2[i] and string1[i]=='1':
            ans+='1'
        else:
            ans+='0'
    return ans

def get_pair(input_xor_string):
    num = random.randint(0, MAX_INT)
    input_bits_string = format(num, '064b')
    other_bits_string = get_other_xor_string(input_bits_string, input_xor_string)
    input_char_string = bits_to_str(input_bits_string)
    other_char_string = bits_to_str(other_bits_string)
    return input_char_string, other_char_string