import re
import os
from pymetamap import MetaMap
from quickumls import QuickUMLS

"""This is a script that inputs local text files and outputs Patient IDs and UMLS terms.

This script splits text files within the working directory into lines, removes any lines with commonly 
negated terms and then extracts UMLS information from the remaining positive lines. This script outputs Patient IDs, 
given that the name of the file is the Patient ID, and UMLS information for non-negated text lines. The default 
is to also output each line that has positive terms. This can easily be commented out if desired. 
This script is meant for use with UCSF clinical notes. Please see the README file for information on the UMLS
metathesaurus and QuickUMLS installations.
"""

## if running more than once, comment this line out. Will result in error if you try to define 'matcher' more than once.
## path should be your destination_path created during QuickUMLS installation. Change accordingly.
matcher = QuickUMLS('/Users/madisonmyers/Desktop/QuickUMLS-master/destination_path')        

location = os.getcwd()## Will use the directory you are working in. Make sure notes/text files are available in this folder.

for file in os.listdir(location):
    if file.endswith(".txt"):
        ## many of the UCSF clinical notes need utf-8 encoding else it will result in an error
        open_file = open(file, 'r', encoding='utf-8', errors='ignore')
        doclist = [ line for line in open_file ]
        docstr = '' . join(doclist)
        bn_sents = re.split(r'[.!?]', docstr)
        out=matcher.match(bn_sents, result)
        filename = file.split(".")[0].split("/")[-1]
        ## most common negated terms in clinical text
        f = ["not", "no", "denies", "without", "no evidence", "with no", "negative for"]
        ## add filename for any text file you don't want to input. Common examples are below.
#         if filename == "requirements":
#             continue
#         if filename == "LICENSE":
#             continue
        for line in bn_sents:
            if any(i.lower() in line.lower() for i in f):
                continue
        else:
            print("PATIENT ID:", filename)
            ## can comment print(line) out if you do not wish to print the positive lines out
            print (line)
            print("UMLS: ", out)
            print("----------------------------------")
