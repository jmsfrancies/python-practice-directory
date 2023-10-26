#!/bin/bash

#Script that finds the ip addresses for the designated target and outputs the data into a text file

 nslookup www.truemfg.com | grep [0-9]| grep -v 127* | awk -F " " '{print ($2)}' >> ./truemfg.txt
