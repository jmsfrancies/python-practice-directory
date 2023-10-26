#!/bin/bash
#
#Script that finds the ip addresses for the designated target and outputs the data into a text file
#
echo "Please enter the FQDN of your target: "
read target
nslookup $target | grep [0-9]| grep -v 127* | awk -F " " '{print ($2)}' >> ./ipaddress.txt
