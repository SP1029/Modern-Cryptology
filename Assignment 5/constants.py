import numpy as np

letters = ['q', 'r', 's', 't', 'u', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']

# x^7 + x + 1
IRR_7_POLY = np.poly1d([1, 0, 0, 0, 0, 0, 1, 1])

starting_code = '''
#!/bin/bash
encode () 
{
    timeout 2.5 sshpass -p $SERVER_PASS ssh -tt student@$SERVER_IP > logs <<commands
    $USER_ID
    $USER_PASS
    5
    go
    wave
    dive
    go
    read
'''

ending_code = '''
commands
}
encode
    '''
    
marker_log_line = "Slowly, a new text starts appearing on the screen. It reads ...\n"