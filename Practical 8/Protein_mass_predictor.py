# ===== 1. define the function protein_mass ======
aa_mass = {
    "G": 57.02,
    "A": 71.04,
    "S": 87.03,
    "P": 97.05,
    "V": 99.07,
    "T": 101.05,
    "C": 103.01,
    "I": 113.08,
    "L": 113.08,
    "N": 114.04,
    "D": 115.03,
    "Q": 128.06,
    "K": 128.09,
    "E": 129.04,
    "M": 131.04,
    "H": 137.06,
    "F": 147.07,
    "R": 156.10,
    "Y": 163.06,
    "W": 186.08
}
def protein_mass(seq):
    total_mass = 0
    for aa in seq:
        if aa in aa_mass:
            total_mass += aa_mass[aa]
        else:
            print(f"Unknown amino acid: {aa}")
    return total_mass

# ===== 2. An example function call ======
example_seq = "GAVLIP"
example_mass = protein_mass(example_seq)
print(f"Total protein mass (for example): {example_mass:.2f} amu")
