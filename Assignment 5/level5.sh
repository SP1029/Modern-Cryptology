#!/bin/bash
encode () 
{
    timeout 0.25 sshpass -p $SERVER_PASS ssh -tt student@$SERVER_IP > logs <<commands
    $USER_ID
    $USER_PASS
    5
    go
    wave
    dive
    go
    read
    $1
commands

    message=$(tail -n4 ./logs | head -n1)
    echo $message > temp
    echo $message
}
plain_text=$1
encode $plain_text
exit