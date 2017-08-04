#!/usr/bin/python

print ("This program takes genome positions from a .sam file and returns the DNA seqeunces flanking it") 

scaf = raw_input("Enter the name of the .fasta file--the reference to which your read is mapped--or a pathway to it:\n\n")
sam = raw_input("Enter the name of the .sam alignment file or a pathway to the file:\n\n")
upstream = raw_input("How many bp (give me an integer) upstream do you want to take?\n\n")
downstream = raw_input("How many bp downstream do you want to take?\n\n")

seq_name = []   #list for sequence names
ref_name = []   #list for reference scaffold names
pos = []        #the base-pair position of the scaffold

for line in open(sam):
	if not line.startswith('@'): 
		ID = line.strip().split()
		seq_name.append(ID[0])
		ref_name.append(ID[2])
		pos.append(ID[3])
		
#####################A function to parse the fasta file ###################################

def fasta_reader(filename):
	from Bio.SeqIO.FastaIO import FastaIterator
	with open(filename) as handle:
		for record in FastaIterator(handle):
			yield record
			
#str(entry.id) is the header of fasta entry
#str(entry.seq) is the sequence of specific fasta entry
			
scaffolds = []
			
for entry in fasta_reader(scaf):
	if str(entry.id) in ref_name:
		scaffolds.append(entry)

##########################################################################################

with open("haplotypes.fasta", "w") as file: 		
	for lineA, lineB, lineC in zip(seq_name,ref_name,pos):
		for fasta in scaffolds:
			if lineB == fasta.id:
				file.writelines(">%s\n%s\n" % (lineA,fasta.seq[int(lineC)-int(upstream):int(lineC)+int(downstream)]))
