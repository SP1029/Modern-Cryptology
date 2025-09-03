import numpy as np
from constants import *
from supporting_functions import *

def initial_permutation(bit_string):
    y = np.reshape(np.array(list(bit_string)), [8,8])
    y = np.fliplr(y.T)
    order = [1,3,5,7,0,2,4,6]
    y = y[order, :]
    y = np.reshape(y, [64])
    y = ''.join(list(y))
    return y

def inv_initial_permutation(bit_string):
    y = np.reshape(np.array(list(bit_string)), [8,8])
    y = np.reshape(np.array(list(y)), [8,8])
    y = np.flipud(y.T)
    order = [4,0,5,1,6,2,7,3]
    y = y[:, order]
    y = np.reshape(y, [64])
    y = ''.join(list(y))
    return y

def expansion(bit_string):
    y = np.array(list(bit_string))
    y = y[[31,0,1,2,3,4,3,4,5,6,7,8,7,8,9,10,11,12,11,12,13,14,15,16,15,16,17,18,19,20,19,20,21,22,23,24,23,24,25,26,27,28,27,28,29,30,31,0]]
    y = ''.join(list(y))
    return y

def permutation(bit_string):
    y = np.array(list(bit_string))
    y = y[[15,6,19,20,28,11,27,16,0,14,22,25,4,17,30,9,1,7,23,13,31,26,2,8,18,12,29,5,21,10,3,24]]
    y = ''.join(list(y))
    return y

def inv_permutation(bit_string):
    y = np.array(list(bit_string))
    y = y[[8,16,22,30,12,27,1,17,23,15,29,5,25,19,9,0,7,13,24,2,3,28,10,18,31,11,21,6,4,26,14,20]]
    y = ''.join(list(y))
    return y

def get_output_s_box(s_box, bit_string):
    row = int(bit_string[0] + bit_string[5], 2)
    col = int(bit_string[1:-1], 2)
    val = s_box[row][col]
    return format(val, '04b')

def s_boxes_encode(bit_string):
    ans = ""
    for i in range(8):
        ans+=get_output_s_box(S_BOXES[i], bit_string[6*i:6*(i+1)])
    return ans

def encode_round(bit_string, round_key):
    l = bit_string[0:32]
    r = bit_string[32:]
    initial_r = r
    
    r = expansion(r)
    r = compute_xor(r, round_key)
    r = s_boxes_encode(r)
    r = permutation(r)
    r = compute_xor(l, r)
    l = initial_r
    
    ans = l + r
    return ans

def left_shift(bit_string, count):
    bit_string = bit_string[count:] + bit_string[:count]
    return bit_string

def compute_keys(key):
    keys = []
    y = np.array(list(key))
    
    c = y[PERMUTED_CHOICE1C]
    c = ''.join(list(c))
    d = y[PERMUTED_CHOICE1D]
    d = ''.join(list(d))
    
    for i in range(16):
        c = left_shift(c, KEY_SHIFT_SCHEDULE[i])
        d = left_shift(d, KEY_SHIFT_SCHEDULE[i])
        bit_string = c + d
        y = np.array(list(bit_string))
        round_key = y[PERMUTED_CHOICE2]
        round_key = ''.join(list(round_key))
        keys.append(round_key)
        
    return keys
        
def encode_des(bit_string, keys, rounds):
    bit_string = initial_permutation(bit_string)
    for i in range(rounds):
        bit_string = encode_round(bit_string, keys[i])
    bit_string = bit_string[32:] + bit_string[:32]
    bit_string = inv_initial_permutation(bit_string)
    return bit_string

def decode_round(bit_string, round_key):
    l = bit_string[:32]
    r = bit_string[32:]
    
    r_old = l
    r_old = expansion(r_old)
    r_old = compute_xor(r_old, round_key)
    r_old = s_boxes_encode(r_old)
    r_old = permutation(r_old)
    l_old = compute_xor(r, r_old)
    
    return l_old +l
    
def decode_des(bit_string, keys, rounds):
    bit_string = initial_permutation(bit_string)
    bit_string = bit_string[32:] + bit_string[:32]
    for i in range(rounds):
        key_ix = rounds - 1 - i
        bit_string = decode_round(bit_string, keys[key_ix])
    bit_string = inv_initial_permutation(bit_string)
    return bit_string

def add_parity_key(key):
    new_key = ""
    for i in range(8):
        byte_key = key[i*7:(i+1)*7] + '_'
        new_key+=byte_key
    return new_key
    