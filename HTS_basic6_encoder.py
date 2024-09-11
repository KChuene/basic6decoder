import sys

def usage():
    print("""
    usage: 
        program.py -dec M3ss@ge2Enc0de
        program.py -enc M3ss@ge2Enc0de
    """)
    print("\n** Note ** Messages are capped at length of 14 chars.")

def bye(msg: str, show_usg: bool):
    if msg:
        print(msg)

    if show_usg:
        usage()

    sys.exit()

def enc_numeric(char: str, index: int):
    if not char.isnumeric():
        return char
    
    numeric = int(char) + index
    if numeric >= 10:
        return chr( ord(char) + index )
    else:
        return str(numeric)
    
def dec_numeric(char: str, index: int):
    if not char.isnumeric():
        return char
    #6386;k8k
    numeric = int(char) - index
    if numeric < 0:
        return char
    else:
        return str(numeric)
    
def enc_alpha(char: str, index: int):
    if char.isnumeric():
        return char
    
    return chr( ord(char) + index )

def dec_alpha(char: str, index: int):
    if char.isnumeric():
        return char
    
    convert = ord(char) - index
    if convert < 0:
        return char
    else:
        return chr( convert )

def encode(string: str) -> str:
    result = []
    for index in range(0, len(string)):
        char = string[index]
        if char.isnumeric():
            result.append( enc_numeric(char, index) )
        else:
            result.append( enc_alpha(char, index) )

    return ''.join(result)

def decode(string: str) -> str:
    result = []
    for index in range(0, len(string)):
        char = string[index]
        if char.isnumeric():
            result.append( dec_numeric(char, index) )
        else:
            result.append( dec_alpha(char, index) )

    return ''.join(result) 

if __name__=="__main__":
    if not (len(sys.argv) >= 3):
        bye("Insufficient arguments.", True)

    elif len(sys.argv[2]) > 14:
        bye("Input string is too long.", True)

    mode = sys.argv[1]
    if mode == "-enc":
        print(encode(sys.argv[2]))
    elif mode == "-dec":
        print(decode(sys.argv[2]))
    else:
        bye("Only modes -enc and -dec are applicable.", True)