#!/bin/bash

## FILE TO FIND TOP 10 WORDS USED IN THE BOOK *The Time Machine* BY *H. G. Wells*
#### Author: Rob


## Storing the URL to the book in a variable
URL_TM="https://www.gutenberg.org/files/22382/22382-0.txt"

## Command to find most common words
curl -k $URL_TM 2>/dev/null | ## Obtaining book from webpage
 sed -n '/START OF THIS PROJECT GUTENBERG/, /END OF THIS PROJECT GUTENBERG/p' > la_iliada2.txt
