import sys


def main():
    if len(sys.argv) < 3:
        print("Usage: ./your_program.sh tokenize <filename>", file=sys.stderr)
        exit(1)

    command = sys.argv[1]
    filename = sys.argv[2]
    error = False

    if command != "tokenize":
        print(f"Unknown command: {command}", file=sys.stderr)
        exit(1)

    with open(filename) as file:
        file_contents = file.read()

    for c in file_contents:
        if c == "(":
            print("LEFT_PAREN ( null")
            continue
        if c == ")":
            print("RIGHT_PAREN ) null")
            continue
        if c == '{':
            print("LEFT_BRACE { null")
            continue
        if c == '}':
            print("RIGHT_BRACE } null")
            continue
        if c == ",":
             print("COMMA , null")
             continue
        if c == ".":
            print("DOT . null")
            continue
        if c == "-":
             print("MINUS - null")
             continue
        if c == "+":
            print("PLUS + null")
            continue
        if c == ";":
            print("SEMICOLON ; null")
            continue
        if c == "*":
            print("STAR * null")
            continue
        else:
            error = True
            line_number = file_contents.count("\n", 0, file_contents.find(c)) + 1
            print(
                "[line %s] Error: Unexpected character: %s" % (line_number, c),
                file=sys.stderr,
            )
    print("EOF  null")
    if error:
        exit(65)
    else:
        exit(0)


if __name__ == "__main__":
    main()
