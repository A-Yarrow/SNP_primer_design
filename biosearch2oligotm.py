#/home/yarrow/anaconda/bin/python/
import argparse
import os
import csv

#compile from biosearch input for to primer 3 input
#create text file to check and return the contents for primer 3 input in next function.
#Will have to copy and past into "example file" to get primer 3 to run correctly
def biosearch2primer3_input(in_file):
    out_file = open(in_file[0:-4]+'2primer3input', 'w+b')
    with open(in_file, 'rb') as csvfile:
        biosearch_reader = csv.reader(csvfile, delimiter=',')
        biosearch_reader.next() #skip the header)
        for row in biosearch_reader:
            if '*' not in row[0]:
                SEQUENCE_ID=row[0]; SEQUENCE_PRIMER=row[3]; SEQUENCE_PRIMER_REVCOMP=row[9]; \
                SEQUENCE_INTERNAL_OLIGO=row[15]
            else:
                pass
            out_file.write('SEQUENCE_ID='+SEQUENCE_ID+'\n')
            out_file.write('PRIMER_TASK=check_primers'+'\n')
            out_file.write('SEQUENCE_PRIMER='+SEQUENCE_PRIMER+'\n')
            out_file.write('SEQUENCE_PRIMER_REVCOMP='+SEQUENCE_PRIMER_REVCOMP+'\n')
            out_file.write('SEQUENCE_INTERNAL_OLIGO='+SEQUENCE_INTERNAL_OLIGO+'\n')
            out_file.write('PRIMER_PICK_LEFT_PRIMER=0'+'\n')
            out_file.write('PRIMER_PICK_INTERNAL_OLIGO=0'+'\n')
            out_file.write('PRIMER_PICK_RIGHT_PRIMER=0'+'\n')
            out_file.write('PRIMER_SALT_DIVALENT=3'+'\n')
            #out_file.write('PRIMER_INTERNAL_SALT_DIVALENT=3'+'\n')
            out_file.write('PRIMER_SALT_MONOVALENT=50'+'\n')
            #out_file.write('PRIMER_SALT_MONOVALENT_INTERNAL=50'+'\n')
            out_file.write('PRIMER_DNTP_CONC=0.8'+'\n')
            #out_file.write('PRIMER_INTERNAL_DNTP_CONC=1'+'\n')
            out_file.write('='+'\n')
            
    #primer3_input = out_file.read()
    out_file.close()
    #return primer3_input
biosearch2primer3_input('biosearch_designs.csv')
#def run_primer3():
    #parser = argeparse.ArgumentParser(description="Execute Primer3 to give Tm values for biosearch designed primers")

#def_parse_output
#primer_3_input = biosearch2primer3_input('biosearch_designs.csv')
            