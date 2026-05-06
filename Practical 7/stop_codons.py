import re

# ====== 1. read the FASTA file ======
with open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r") as infile:
    sequences = {}
    for line in infile:
        line = line.strip()
        if line.startswith(">"):
            current_header = line
            sequences[current_header] = ""
        else:
            sequences[current_header] += line

# ====== 2. genes with stop codon ======
with open("stop_genes.fa", "w") as outfile:
    for header, seq in sequences.items():
        stop_codon_found = []
        start_positions = [i for i in range(len(seq)-2) if seq[i:i+3] == 'ATG']
        for start_pos in start_positions:
            for i in range(start_pos, len(seq)-2, 3):
                codon = seq[i:i+3]
                if codon in ["TAA", "TAG", "TGA"]:
                    stop_codon_found.append(codon)
                    break  # stop the ORF when finding the first stop codon
        if stop_codon_found:
            unique_codons = list(set(stop_codon_found))
            gene_name = header.split()[0][1:]
            outfile.write(f">{gene_name}; {', '.join(sorted(set(stop_codon_found)))}\n")
            for i in range(0, len(seq), 60):
                outfile.write(seq[i:i+60] + "\n")
