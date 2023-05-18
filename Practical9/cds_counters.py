seq = 'ATGCAATCGACTACGATCTGAGAGGGCCTAA'
# Importing the regular expression module
import re
# Split the sequence at the first occurrence of the start codon "ATG"
start_codon = re.split("ATG", seq, 1)
possible_number = 0
# Check if a start codon was found in the sequence
if len(start_codon) > 1:
    coding = re.findall(r"(TAA|TAG|TGA)", start_codon[1])
    possible_number = len(coding)
print(possible_number)
