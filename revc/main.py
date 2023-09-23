# s = 'AAAACCCGGT'
s = open('rosalind_revc.txt').read().strip()
s_c = s[::-1].translate(str.maketrans({
    'A': 'T',
    'C': 'G',
    'G': 'C',
    'T': 'A',
}))
print(s_c)