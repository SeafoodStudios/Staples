import argparse

def run(code):
    if len(code) % 8 == 0:
        if len(code) % 2 == 0:
            oldcode = code
            code = code.replace("[", "0")
            code = code.replace("{", "1")
            midpoint = len(oldcode) // 2
            checksum = str(code)[midpoint:][::-1]
            checksum = checksum.replace("]", "[")
            checksum = checksum.replace("}", "{")
            oldcode = str(oldcode)[:midpoint]
            if str(checksum) == str(oldcode):
                executable = ""
                for i in range(0, midpoint, 8):
                    executable += chr(int(code[i:i+8], 2))
                exec(str(executable))
            else:
                return "ERR: Incorrect Checksum"
        else:
            return "ERR: Syntax"
    else:
        return "ERR: Syntax"
    
def convert(code):
    staples = ""
    for i in code:
        staples += format(ord(i), '08b')
    staples = staples.replace("0","[")
    staples = staples.replace("1","{")
    end = staples[::-1]
    end = end.replace("[","]")
    end = end.replace("{","}")
    output = staples + end
    return str(output)

parser = argparse.ArgumentParser(description="Staples Language")
parser.add_argument('command', choices=['run', 'compile'], help='Command to run')
parser.add_argument('path', help='Path string to process')

args = parser.parse_args()

if args.command == 'run':
    with open(str(args.path), "r") as f:
        to_run = f.read()
    result = run(to_run)
    if result is not None:
        print(result)
elif args.command == 'compile':
    with open(str(args.path), "r") as f:
        to_compile = f.read()
    result = convert(str(to_compile))
    with open(str(args.path) + ".staples", "w") as f:
        f.write(str(result))

