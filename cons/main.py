# arguments = """
# >Rosalind_1
# ATCCAGCT
# >Rosalind_2
# GGGCAACT
# >Rosalind_3
# ATGGATCT
# >Rosalind_4
# AAGCAACC
# >Rosalind_5
# TTGGAACT
# >Rosalind_6
# ATGCCATT
# >Rosalind_7
# ATGGCACT
# """.strip()
arguments = open("rosalind_cons.txt").read().strip()
dna_strings = {
    x: y
    for x, y in [
        (x.split("\n")[0], "".join(x.split("\n")[1:])) for x in arguments.split(">")[1:]
    ]
}
c = ""
profile = []
for nucleobases in zip(*dna_strings.values()):
    profile.append(
        {nucleobase: nucleobases.count(nucleobase) for nucleobase in "ACGT"}
    )
    c += max(profile[-1].items(), key=lambda x: x[1])[0]
print(c)
for nucleobase in "ACGT":
    print(
        nucleobase
        + ": "
        + " ".join(str(occurence[nucleobase]) for occurence in profile)
    )
