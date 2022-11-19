def to_rna(dna_strand):
return dna_strand.replace("A", "U").replace("T", "A").replace("G", "r").replace("C", "G").replace("r", "C")
