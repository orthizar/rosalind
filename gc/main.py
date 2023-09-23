# arguments = """
# >Rosalind_6404
# CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
# TCCCACTAATAATTCTGAGG
# >Rosalind_5959
# CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
# ATATCCATTTGTCAGCAGACACGC
# >Rosalind_0808
# CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
# TGGGAACCTGCGGGCAGTAGGTGGAAT
# """
arguments = open('rosalind_gc.txt').read().strip()
dna_strings = {
    x: y for x, y in [(x.split('\n')[0], ''.join(x.split('\n')[1:])) for x in arguments.split('>')[1:]]
}

max_gc = [None, 0]
for name, dna in dna_strings.items():
    gc = (dna.count('C') + dna.count('G')) / len(dna)
    max_gc = [name, gc*100] if gc*100 > max_gc[1] else max_gc

print(max_gc[0])
print(max_gc[1])