#!/bin/bash

USERDIR=/home/septri/users

if [[ ! -d $USERDIR ]];
then
	mkdir $USERDIR
fi

ssh-keygen -b 2048 -t rsa -f "/home/septri/users/test" -N ""
