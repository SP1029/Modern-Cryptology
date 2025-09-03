from des_functions import *
from constants import *
from supporting_functions import *

ip_xor_to_op_xor = {}
for i in range(8):
    ip_xor_to_op_xor[i] = {}
    for j in range(64):
        ip_xor_to_op_xor[i][format(j, '06b')] = set()
   
for i in range(8):
    for a in range(64):
        for b in range(64):
            bit_string1 = format(a ,'06b')
            bit_string2 = format(b ,'06b') 
            ip_xor = compute_xor(bit_string1, bit_string2)
            op1 = get_output_s_box(S_BOXES[i], bit_string1)
            op2 = get_output_s_box(S_BOXES[i], bit_string2)
            op_xor = compute_xor(op1, op2)
            ip_xor_to_op_xor[i][ip_xor].add(op_xor)

def des_encode_single(plain_text):
    cipher_text = ""
    while cipher_text=="" or len(cipher_text)!=16 or cipher_text.isalpha()==False:
        subprocess.call("./level4.sh " + plain_text, shell=True)
        with open("temp", 'r') as f:
            cipher_text = f.readline()[:-1]
    return cipher_text

def des_encode_multiple(plain_texts):
    
    # Making the code file
    f = open("des_encode_multiple.sh", 'w+')
    
    f.write(starting_code)
    for p in plain_texts:
        f.write(p + "\nc\n")
    f.write(ending_code)
    f.close()
    subprocess.call("./des_encode_multiple.sh", shell=True)
    
    # Reading the ciphertexts
    f = open("./logs", 'r')

    cipher_texts = []
    next_cipher_flag = False

    line = f.readline()
    while line!="":
        if next_cipher_flag:
            next_cipher_flag = False
            cipher_texts.append(line[2:-1])
        
        if line==marker_log_line:
            next_cipher_flag = True
            
        line = f.readline()
        
    f.close()
    
    return cipher_texts