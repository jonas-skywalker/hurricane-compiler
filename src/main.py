def parse_file(filename):
    c_code = get_source(filename)
    print(c_code)


def get_source(filename):
    with open(filename, "r") as infile:
        c_code = infile.read().replace('\n', '')
    #c_code = c_code.replace(" ", "")
    return c_code


if __name__ == '__main__':
    filename = "src/test.txt"
    parse_file(filename)
