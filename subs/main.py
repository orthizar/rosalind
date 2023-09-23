# arguments = """
# GATATATGCATATACTT
# ATAT
# """.strip()
arguments = open("rosalind_subs.txt").read().strip()
s, t = arguments.split("\n")

last = 0
while last != -1:
    last = s.find(t, last + 1)
    if last != -1:
        print(last + 1, end=" ")
