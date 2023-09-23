## Computing GC Content
https://rosalind.info/problems/gc/

### Solution
We decode the FASTA format to a dictionary of names and dna strings.
Then we evaluate iteratively whether the GC-content `(C + G) / (C + G + A + T)` of the current dna string is greater than all previous evaluated dna strings. The result is the name and GC-content of the dna string with the highest GC-content.