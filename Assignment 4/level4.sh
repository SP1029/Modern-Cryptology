#!/bin/bash
encode () 
{
    timeout 0.3 sshpass -p $SERVER_PASS ssh -tt student@$SERVER_IP > logs <<commands
    $USER_ID
    $USER_PASS
    4
    go
    dive
    dive
    back
    pull
    back
    back
    go
    wave
    back
    back
    thrnxxtzy
    the_magic_of_wand
    c
    read
    $1
commands

    message=$(tail -n4 ./logs | head -n1)
    echo $message > temp
}
plain_text=$1
encode $plain_text