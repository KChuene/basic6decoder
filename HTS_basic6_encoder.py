import sys

def bye(msg: str, show_usg: bool):
    if msg:
        print(msg)

    if show_usg:
        print("usage: \n\tprogram.py M3ss@ge2Enc0de")
        print("\n** Note ** Messages are capped at length of 14 chars.")

def enc_numeric(char: str, index: int):
    if not char.isnumeric():
        return char
    
    numeric = int(char) + index
    if numeric >= 10:
        return chr( ord(char) + index )
    else:
        return str(numeric)
    
def enc_alpha(char: str, index: int):
    if char.isnumeric():
        return char
    
    return chr( ord(char) + index )

def encode(string: str):
    result = []
    for char in string:
        if char.isnumeric():
            result.append( enc_numeric(char, string.index(char)) )
        else:
            result.append( enc_alpha(char, string.index(char)) )

    return ''.join(result)

if __name__=="__main__":
    if not (len(sys.argv) >= 2):
        bye("[!] Expected string to encrypt but none found.", True) 

    print(encode(sys.argv[1]))