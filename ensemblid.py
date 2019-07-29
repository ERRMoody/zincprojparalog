from Bio import SeqIO
import sys
import subprocess

taxaidlist = []
taxaspecieslist = []
taxaidtospecies = {}
taxaidlisttoconvert = []

with open('idlist.csv', 'r') as idcsv:
	for line in idcsv:
		idtoappend = line.split(',')[0]
		speciestoappend = line.split(',')[1]
		speciestoappend = speciestoappend.strip()
		taxaspecieslist.append(speciestoappend)
		taxaidlist.append(idtoappend)



taxaidtospecies = dict(zip(taxaidlist, taxaspecieslist))


filename = sys.argv[1]

with open (filename, 'r') as inputalignment:
    for line in inputalignment:
        if '>' in line:
            lengthcheck = line.split('0')[0]
            if 'MGP_' in line:
                lengthcheck = lengthcheck[1:-1]
                taxaidlisttoconvert.append(lengthcheck)
            elif 'FBp' in line:
                lengthcheck = lengthcheck[1:-1]
                taxaidlisttoconvert.append(lengthcheck)
            elif len(lengthcheck) >= 2:
                taxaid = lengthcheck
                taxaid = taxaid[1:-1]
                taxaidlisttoconvert.append(taxaid)
                	


for taxa in taxaidlisttoconvert:
    subprocess.call(['sed -i -e "s/'+taxa+'P/'+taxaidtospecies[taxa]+'_/gi" '+filename+' '], shell=True)
    
