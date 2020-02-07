import lexer
import parsing

def load_test_source():
    with open("..\\test.c") as file:
        return file.read()

def test_lexer1():
    source = load_test_source()
    ts = lexer.token_stream(source)

def test_parser1():
    source = load_test_source()
    ts = lexer.token_stream(source)
    print(parsing.parse(ts))

#test_lexer1()
test_parser1()