#!/bin/bash

USERDIR=/home/$USER/nixScavengerHunt/users

if [[ ! -d $USERDIR ]];
then
	mkdir $USERDIR
fi

STUDENTS=./studentNames.txt

while read -r line; do
    #echo "adduser $line"
    LOWERCASE=${line,,}
    echo $LOWERCASE
    sudo adduser -q --disabled-password $LOWERCASE
    echo "y"
    sudo mkdir /home/$LOWERCASE/.ssh
    sudo chown $USER /home/$LOWERCASE/.ssh
    ssh-keygen -b 2048 -t rsa -f "$USERDIR/$LOWERCASE.pem" -N "" -m PEM
    mv $USERDIR/$LOWERCASE.pem.pub /home/$LOWERCASE/.ssh/authorized_keys
    sudo chown -R $LOWERCASE /home/$LOWERCASE/.ssh
done <$STUDENTS

clear

echo "Users all created. Pem files are in $USERDIR"