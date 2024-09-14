import sys


def main():
    if len(sys.argv) < 3:
        print("Usage: ./your_program.sh tokenize <filename>", file=sys.stderr)
        exit(1)

    command = sys.argv[1]
    filename = sys.argv[2]

    if command != "tokenize":
        print(f"Unknown command: {command}", file=sys.stderr)
        exit(1)

    with open(filename) as file:
        file_contents = file.read()

    i = 0
    error = False
    length = len(file_contents)

    while i < length:
        c = file_contents[i]
        if c == '/':
            if i + 1 < length and file_contents[i + 1] == '/':
                # Skip the rest of the line for a comment
                i += 2
                while i < length and file_contents[i] != '\n':
                    i += 1
                continue
            else:
                print("SLASH / null")
        elif c == '(':
            print("LEFT_PAREN ( null")
        elif c == ')':
            print("RIGHT_PAREN ) null")
        elif c == '{':
            print("LEFT_BRACE { null")
        elif c == '}':
            print("RIGHT_BRACE } null")
        elif c == ',':
            print("COMMA , null")
        elif c == '.':
            print("DOT . null")
        elif c == '-':
            print("MINUS - null")
        elif c == '+':
            print("PLUS + null")
        elif c == ';':
            print("SEMICOLON ; null")
        elif c == '*':
            print("STAR * null")
        elif c == '<':
            if i + 1 < length and file_contents[i + 1] == '=':
                print("LESS_EQUAL <= null")
                i += 1  # Skip the next character as it is part of the '=='
            else:
                print("LESS < null")
        elif c == '>':
            if i + 1 < length and file_contents[i + 1] == '=':
                print("GREATER_EQUAL >= null")
                i += 1  # Skip the next character as it is part of the '=='
            else:
                print("GREATER > null")
        elif c == '=':
            if i + 1 < length and file_contents[i + 1] == '=':
                print("EQUAL_EQUAL == null")
                i += 1  # Skip the next character as it is part of the '=='
            else:
                print("EQUAL = null")
        elif c == '!':
            if i + 1 < length and file_contents[i + 1] == '=':
                print("BANG_EQUAL != null")
                i += 1  # Skip the next character as it is part of the '!='
            else:
                print("BANG ! null")
        else:
            # Handle unexpected characters
            error = True
            line_number = file_contents.count("\n", 0, i) + 1
            print(f"[line {line_number}] Error: Unexpected character: {c}", file=sys.stderr)

        i += 1

    print("EOF  null")
    if error:
        exit(65)
    else:
        exit(0)


if __name__ == "__main__":
    main()
