# SeqSeeker
Harvest flanking sequences surrounding a sam alignment

Let's say you have some short DNA reads mapped to a genome in .sam format. You now want to design PCR amplicons for these loci and need to have the flanking DNA sequences to design primers.

That's what this script does. 

seqSeeker.py will ask you for four inputs:

1) the fasta file reference that your read is mapped to
2) the .sam alignment file
3) an intiger indicating how many bp upstream you want to harvest
4) an intiger indicating how many bp downstream you want to harvest. 

This is useful if, for example, you want to design small multi-SNP haplotypes for population/stock assignment analysis

(see McKinney et al. 2017. Canadian Journal of Fisheries and Aquatic Sciences 74:429-434)
