import re
data = open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa")
print("Please enter a stop codon [TAA/TAG/TGA]")
stop_codons = input("")
if not re.match("TAA|TAG|TGA", stop_codons):
    print("The input is not a stop codon")
else:
    output = open(stop_codons+"_stop_genes.fa", "w")
    seq = ""
    for line in data:
        if line.startswith(">"):
            seq += "\n"
            gene = re.split(" ", line, 1)[0]
            if re.findall(stop_codons, seq):
                num = len(re.findall(stop_codons, seq))
                output.write(seq%(str(num)))
            seq = ""
            count = 0
            num = 0
        elif not line.startswith(">"):
            count += 1
            if count == 1:
                seq += gene + " coding_sequences: %s" + "\n"
            seq += line[:-1]
data.close()
output.close()
