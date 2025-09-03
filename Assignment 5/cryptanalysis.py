import subprocess
from constants import *

def encode_single(plain_text):
    cipher_text = ""
    while cipher_text=="" or len(cipher_text)!=16 or cipher_text.isalpha()==False:
        subprocess.call("./level5.sh " + plain_text, shell=True)
        with open("temp", 'r') as f:
            cipher_text = f.readline()[:-1]
    return cipher_text

def encode_multiple(plain_texts):
    
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