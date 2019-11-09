#!/bin/bash
echo Hello, World!
NOW=$(date +"%Y-%m-%d")
echo $NOW
FILE="backup.$NOW.tar.gz"
echo "Backing up data to /nas42/backup.$NOW.tar.gz file, please wait..."
# rest of script
tar -czvf  /Users/amin/Desktop/backup.$NOW.tar.gz /Users/amin/Desktop/Fraud_Detection/ 

