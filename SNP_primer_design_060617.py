import sys
import io
import urllib2


def query_dbSNP(file_in):
	file_out = open(file_in[0:-4]+'.fasta', 'w+b')
	file_handle = open(file_in, 'rb')
	#snp_list = []
	mixed_bases = ['R', 'Y', 'M', 'K', 'S', 'W', 'H', 'B', 'V', 'D', 'N']
	for line in file_handle:
		if line.startswith('rs'):
			rsid = line.rstrip()
			url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=snp&id='+rsid+'&report=FASTA'
			snp_query = urllib2.urlopen(url)
			snp_query_output = snp_query.read()
			file_out.write(snp_query_output)
	file_out.seek(0)
	rs_list_fasta = file_out.read()
	#print 'type', type(rs_list_fasta)
	#print 'rs_list_fasta'+rs_list_fasta
	return rs_list_fasta, mixed_bases
	file_out.close()

def make_batch_input_for_biosearch():
	file_in = sys.argv[1]
	rs_list_fasta, mixed_bases = query_dbSNP(file_in)
	#file_in = open('rs_list.fasta')
	print rs_list_fasta, mixed_bases
	file_out = open(file_in[0:-4]+'_snp.fasta', 'wb')
	
	for line in rs_list_fasta.split('\n'):
		if line.startswith('>'):
			DNA = ''
			line = line.rstrip().split('|')
			rs_name = '>'+line[2].split()[0]+'\n'
			snp = '['+line[8].replace('alleles=', '').replace('\"', '')+']'
			print rs_name, snp
			file_out.write(rs_name)
		elif not line.startswith('>') and line not in mixed_bases:
			DNA = line.replace(' ', '')
			print 'DNA', DNA
			file_out.write(DNA+'\n')
		elif line in mixed_bases:
			multibase = line
			snp_region = line.replace(multibase, snp)
			print 'snp_region', snp_region
			file_out.write(snp_region)	
			
			
	
	file_out.close()
make_batch_input_for_biosearch()	