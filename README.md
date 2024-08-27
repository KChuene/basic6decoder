# HTS-Basic-6-Encoder
This is an encoder/decoder for the Basic 6 challenge on Hack Ths Site. Find it [here](https://www.hackthissite.org/missions/basic/)

## Analogy (RE) of Original Encoder
**Alphabetic characters**
```
love = lpxh # Still length 4

abc = ace
def = dfh 
abcde = acegi
fghij = fhjln

/* 
	Rule: For each letter in string:
			cypher = cypher + character of ( decimal of letter + index of letter )
*/
```

**Numeric characters**
```
123 = 135
123456 = 13579; # ; = 6 + 4 = 11
09 = 0: # : = 9 + 1 = 10
0129 = 024<
01234569 = 02468:<@
012345679 = 02468:<>A

/*
	Rule: For each numeric in string:
			if numeric + index of numeric >= 10 then
				# Map numerics from 10 to ASCII chars that follow 9 on the ASCII table
				cypher = cypher + character of (decimal of numeric + index of numeric)
			else
				cypher = cypher + (numeric + index of numeric)
			
*/

/* MAXIMUM ALLOWED LENTH IS 14 */
```
After a couple of test, we find that the maximum allowed length of input is 14 characters.
