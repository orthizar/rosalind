#s = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
s = open("rosalind_dna.txt").read().strip()
for i in "ACGT":
    print(s.count(i), end=" ")