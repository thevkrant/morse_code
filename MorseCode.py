# Created by Vikrant

def convert_morse(code):
    code = code.replace("a", ".-")
    code = code.replace("b", "-...")
    code = code.replace("c", "-.-.")
    code = code.replace("d", "-..")
    code = code.replace("e", ".")
    code = code.replace("f", "..-.")
    code = code.replace("g", "--.")
    code = code.replace("h", "....")
    code = code.replace("i", "..")
    code = code.replace("j", ".---")
    code = code.replace("k", "-.-")
    code = code.replace("l", ".-..")
    code = code.replace("m", "--")
    code = code.replace("n", "-.")
    code = code.replace("o", "---")
    code = code.replace("p", ".--.")
    code = code.replace("q", "--.-")
    code = code.replace("r", ".-.")
    code = code.replace("s", "...")
    code = code.replace("t", "-")
    code = code.replace("u", "..-")
    code = code.replace("v", "...-")
    code = code.replace("w", ".--")
    code = code.replace("x", "-..-")
    code = code.replace("y", "-.--")
    code = code.replace("z", "--..")

    return code


msg = input("Enter any message: ")
print(f"Initial code :{msg}")
morse = convert_morse(msg)
print(f"Morse code: {morse}")
