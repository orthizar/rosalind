## Complementing a Strand of DNA
https://rosalind.info/problems/revc/

### Solution
We can use `str.translate` to replace each nucleobase with its complement. We can use `str.maketrans` to create a translation table for `str.translate` to use.