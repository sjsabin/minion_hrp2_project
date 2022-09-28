# pfhrp2 typing script
#
# Usage:
#
# python hrp2.py [INPUT/PATH] [OUTPUT/PATH/FILENAME.txt]
#
# Note: No trailing "/" necessary in input path. Input path is directory with desired fasta files.

import sys
import glob

Path = str(sys.argv[1] + "/*.fasta")  # user has to change the path whith all the fasta files
#Path = str(sys.argv[1]) <-- The issue is bash interpreting the "*.fasta" rather than the python script interpreting the *.fasta
#output = (sys.argv[2])

# Write output header string
head_long = ("filename\tsequence\tstart_VDD\tStop_CLRH\tHRP3\tAmbiguit_check\tLength_between_start_and_stop\ttotal_length_of_repeats\tresidues\texon_1\texon2_start\trepeat_type\trepeat_type_count")
head_wide = ("filename\tsequence\tstart_VDD\tStop_CLRH\tHRP3\tAmbiguit_check\tLength_between_start_and_stop\ttotal_length_of_repeats\tresidues\texon_1\texon2_start\ttype1\ttype2\ttype3\ttype4\ttype5\ttype6\ttype7\ttype8\ttype9\ttype10\ttype11\ttype12\ttype13\ttype14\ttype30\ttype31")

# Create a list of output strings, populate with header string
out_ls_long = [head_long]
out_ls_wide = [head_wide]
files = glob.glob(Path)
start_1 = "VDD"
stop_1 = "CLRH"
HRP3 = "ANHGFHFNLHDNNSHTLHHAKANACFDD"    #also look for HRP3 gene presence/absence

for name in files:
	with open (name) as f:
		lines = f.readlines()
		seqnames = []
		headidx = []
		namesplt = name.split("/")
		nm = namesplt[len(namesplt)-1]
		for i in lines:
			if ">" in i:
				x = i.split()
				y = lines.index(i)
				seqnames.append(x[0])
				headidx.append(y)
		for j in range(0, len(headidx)):
			i = headidx[j]
			y = i+1
			if j < len(headidx)-1:
				x = headidx[j+1]-1
			else:
				x = len(lines)-1
			if y==x:
				contents = lines[y]
			else:
				contents = lines[y:x]
			if start_1 in contents:
				start = "VDD is present"
			else:
				start = "No VDD found"
			if stop_1 in contents:
				stop = "CLRH is present"
			else:
				stop = "No CLRH found"
			if HRP3 in contents:
				hrp3 = "HRP3 is present"
			else :
				hrp3 = "No HRP3"

        #count all the bases between start and stop codon
			try:
				start_len = contents.index("VDD")
				stop_len = contents.index("CLRH")
			except:
				all_dna = 0
				ambiguity = "NA"
			else:
				all_dna = len(contents[start_len : (stop_len + 4)]) - 7
				if "X" in contents[start_len : stop_len] :
					ambiguity = "TRUE"
				else:
					ambiguity = "False"

			exon_1 = contents.count("MVSFSKNKVLSAAVFASVLLLDN")
			exon2_start = contents.count("NNSAFNNNLCSKNA")

			type1 = contents.count("AHHAHHVAD")
			type2 = contents.count("AHHAHHAAD")
			type3= contents.count("AHHAHHAAY")
			type5= contents.count("AHHAHHASD")
			type10= contents.count("AHHAAAHHATD")
			type11= contents.count("AHN")
			type12= contents.count("AHHAAAHHEAATH")
			type14= contents.count("AHHAHHATD")
			type30 = contents.count("AHHAVD")
			type31 = contents.count("SHHAAY")
			type7 = contents.count("AHHAAD") -  type2
			type8 = contents.count("AHHAAY") - type3
			type13 = contents.count("AHHASD") - type5
			type6 = contents.count("AHHATD") - (type10 + type14)
			type9 = contents.count("AAY") - (type8 + type3 + type31)
			total_AHH = 2*type1 + 2*type2 + 2*type3 + 2*type5 + 2*type10 + 2*type12 + 2*type14 + type7 + type8 + type13 + type6 + type30
			type4 = contents.count("AHH") - total_AHH
			# Store all repeat types and their respective counts in a dictionary
			type_list = {'type1': str(type1), 'type2': str(type2), 'type3': str(type3), 'type4': str(type4), 'type5': str(type5), 'type6': str(type6), 'type7': str(type7), 'type8': str(type8), 'type9': str(type9), 'type10': str(type10), 'type11': str(type11), 'type12': str(type12), 'type13': str(type13), 'type14': str(type14), 'type30': str(type30), 'type31': str(type31)}
			# total bases for all above repeat type
			total_bases = type1 * len("AHHAHHVAD") + type2 * len("AHHAHHAAD") + type3 * len("AHHAHHAAY") + type4 * len("AHH") + type5 * len("AHHAHHASD") + type6 *len("AHHATD") + type7 * len("AHHAAD")+ type8 * len("AHHAAY") + type9 * len("AAY") + type10 * len("AHHAAAHHATD") +type11 * len("AHN") + type12 * len("AHHAAAHHEAATH") + type13 * len("AHHASD") + type14 * len("AHHAHHATD") + type30 * len("AHHAVD") + type31 * len("SHHAAY")
			residue = all_dna - total_bases
			seqname = seqnames[j]
			#seqname = lines[i].split()[0]
			ln = str(str(nm) + '\t' + str(seqname) + '\t' + start + '\t' + stop + '\t' + hrp3 + '\t' + ambiguity + '\t' + str(all_dna) + '\t' + str(total_bases) + '\t' + str(residue) + '\t' + str(exon_1) + '\t' + str(exon2_start) + '\t' + str(type1) + '\t' + str(type2) + '\t' + str(type3) + '\t' + str(type4) + '\t' + str(type5) + '\t' + str(type6) + '\t' + str(type7) + '\t' + str(type8) + '\t' + str(type9) + '\t' + str(type10) + '\t' + str(type11) + '\t' + str(type12) + '\t' + str(type13) + '\t' + str(type14) + '\t' + str(type30) + '\t' + str(type31))
			out_ls_wide.append(ln)
			for key in type_list:
				ln = str(str(nm) + '\t' + str(seqname) + '\t' + start + '\t' + stop + '\t' + hrp3 + '\t' + ambiguity + '\t' + str(all_dna) + '\t' + str(total_bases) + '\t' + str(residue) + '\t' + str(exon_1) + '\t' + str(exon2_start) + '\t' + str(key) + '\t' + str(type_list[key]))
				out_ls_long.append(ln)

with open("results_wide.txt", "w") as outF:
	for line in out_ls_wide:
		outF.write(line)
		outF.write("\n")

with open("results_long.txt", "w") as outF:
	for line in out_ls_long:
		outF.write(line)
		outF.write("\n")
