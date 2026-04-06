stop_codon = input("Enter a stop codon (TAA, TAG, TGA): ").upper()
if stop_codon not in ["TAA", "TAG", "TGA"]:
    raise ValueError("Invalid stop codon. Must be TAA, TAG, or TGA.")
from collections import Counter

codon_counts = Counter()
# read the input FASTA file
with open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r") as infile:
    sequences = {}
    for line in infile:
        line = line.strip()
        if line.startswith(">"):
            current_header = line
            sequences[current_header] = ""
        else:
            sequences[current_header] += line
            
for header, seq in sequences.items():
    # find the in-frame position of all the stop codons
    positions = [i for i in range(0, len(seq)-2, 3) if seq[i:i+3] == stop_codon]
    if not positions:
        continue  # skip if no stop codon
    stop_pos = positions[-1]  # the last stop codon
    # upstream codons
    for i in range(0, stop_pos, 3):
        codon_counts[seq[i:i+3]] += 1

import matplotlib.pyplot as plt

labels = codon_counts.keys()
sizes = codon_counts.values()

plt.figure(figsize=(8,8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title(f"Codon distribution upstream of {stop_codon}")
plt.savefig(f"codon_distribution_{stop_codon}.png")  # save the figure
plt.close()  