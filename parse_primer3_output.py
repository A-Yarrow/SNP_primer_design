#/home/yarrow/anaconda/bin/python/
import pandas

def parse_primer3_output(infile):
    seq_id = [ ]
    file_handle = open(infile, 'rb')
    for line in file_handle:
        if line.startswith('SEQUENCE_ID'):
            ind = line.find('=')
            seq_id.append(line[ind+1:].strip('\n'))
    print seq_id
    
    file_handle.close()            
    

parse_primer3_output('biosearch_designs2primer3input.txt')