# HTS-Basic-6-EncoderDecoder
This is an encoder/decoder for the Basic 6 challenge on Hack Ths Site. Find it [here](https://www.hackthissite.org/missions/basic/)

## Usage
Simply run either of the following commands.

**Encoding:**
```
python3 program.py -enc My1nPut
```
**Decoding:**
```
python3 program.py -dec Mz3qTzz
```

## Analogy (RE) of Original Encoder
**Alphabetic characters**: Several encode tests are done than we identify the pattern that is consistent across every output.
```
love = lpxh # Still length 4

abc = ace
def = dfh 
abcde = acegi
fghij = fhjln
```
hence leading to the algorithm
```
For each letter in string:
	cypher = cypher + character of ( decimal of letter + index of letter )
```

**Numeric characters**: Same with encoding for alphabetic characters, there's a shift by the character's index value, except here 
when the shift yield a number greater than 10, the output is than mapped to an ASCII character on the ASCII table.
```
123 = 135
123456 = 13579; # ; = 6 + 4 = 11
09 = 0: # : = 9 + 1 = 10
0129 = 024<
01234569 = 02468:<@
012345679 = 02468:<>A
```
hence the algorithm for encoding numerics is
```
For each numeric in string:
	if numeric + index of numeric >= 10 then
		# Map numerics from 10 to ASCII chars that follow 9 on the ASCII table
		cypher = cypher + character of (decimal of numeric + index of numeric)
	else
		cypher = cypher + (numeric + index of numeric)
```
After a couple of test, we find that the maximum allowed length of input is 14 characters.
