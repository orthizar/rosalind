# t = 'GATGGAACTTGACTACGTAAATT'
t = open('rosalind_rna.txt').read().strip()
u = t.replace('T', 'U')
print(u)