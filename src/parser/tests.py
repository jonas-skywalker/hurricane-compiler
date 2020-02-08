import lexer
import parsing

def load_test_source():
    with open("..\\test.hc") as file:
        return file.read()

def test_lexer1():
    source = load_test_source()
    ts = lexer.token_stream(source)
    print(ts)

def test_parser1():
    source = load_test_source()
    ts = lexer.token_stream(source)
    print(parsing.parse(ts))

#test_lexer1()
test_parser1()