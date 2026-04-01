seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
import re
# find all the orf
orf_UAA = re.findall(r"(AUG.+?UAA)", seq) # the start codon can begin at any position 
orf_UAG = re.findall(r"(AUG.+?UAG)", seq) # so we don't need ^
orf_UGA = re.findall(r"(AUG.+?UGA)", seq)
orfs = orf_UAA + orf_UAG + orf_UGA
# find the largest orf
max_len = 0
max_orf = ""
for orf in orfs:
    if len(orf) > max_len and len(orf) % 3 == 0:
        max_len = len(orf)
        max_orf = orf
print("The largest orf is", max_orf)
print("The length is", len(max_orf))