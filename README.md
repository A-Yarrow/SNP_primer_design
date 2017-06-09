# SNP_primer_design
SNP_asssay_design.py takes one argument in the command line. This argument should be a text file with a list of SNPs by RS number.
Example:

rs1065852
rs1135840
rs16947
rs28371706
rs9923231

query_dbSNP(filename)
The first function (above) querys the dbSNP database for each rs number. It writes out a fasta a multiple fasta file with the same basename as the argument you pass in the command line (the list of rs numbers). The multiple fasta is returned as a string.

make_batch_input_for_biosearch()
These sequences are meant to query biosearch SNP primer design software. This function calls the query_dbSNP function and replaces the mixed_base nomenclature (mixed_bases = ['R', 'Y', 'M', 'K', 'S', 'W', 'H', 'B', 'V', 'D', 'N']) with the SNP, for example: [A/T]. The function returns a muliple fasta with the mixed base replaced by the SNP and writes the FASTA with the baseanme provided in the cammand line as well as "_snp.fasta" appended to it. Ten of these at a time can be copied into the biosearch SNP design website.

