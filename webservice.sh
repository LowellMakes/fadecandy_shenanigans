#!/bin/bash

name=$1
services="mario piday flame pacman lowellmakes picam video mariovideo"

killservice(){
 pidfile="/var/run/$1.pid"
 if [ -f $pidfile ] ; then
	echo $pidfile exists
	svcpid=$(cat $pidfile)
	service $i stop
	sleep 1
	kill -9 $svcpid
 fi
}

for i in $services
	do
		if [ $i != "$name" ] ; then
			killservice $i	
		fi
done
if [ "$name" != none ] ; then
 service $name start &
fi
