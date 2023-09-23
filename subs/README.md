## Finding a Motif in DNA
https://rosalind.info/problems/subs/

### Solution
We search for occurences of the substring `t` of the dna string `s` using `s.find(t, offset)`, where the `offset` is the last found position. The search is repeated until no more occurences are found (the `find` function returns `-1`).