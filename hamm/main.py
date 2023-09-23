# arguments = """
# GAGCCTACTAACGGGAT
# CATCGTAATGACGGCCT
# """.strip()
arguments = open('rosalind_hamm.txt').read().strip()
dna_strings = arguments.split('\n')
distance = 0
for a, b in zip(*dna_strings):
    distance += a != b

print(distance)