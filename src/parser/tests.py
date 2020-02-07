import lexer
import parsing

def load_test_source():
    with open("..\\test.txt") as file:
        return file.read()

def test_lexer1():
    source = load_test_source()
    ts = lexer.token_stream(source)
    assert list(ts) == [('if', 'if'), ('(', 'open_bracket'), ('x', 'ident'), ('==', 'assign'), ('3', 'lit'),
                        (')', 'closed_bracket'), ('{', 'open_bracket'), ('print', 'print'), ('(', 'open_bracket'),
                        ('x', 'ident'), (')', 'closed_bracket'), (';', 'semicolon'), ('}', 'closed_bracket'),
                        ('if', 'if'), ('(', 'open_bracket'), ('x', 'ident'), ('=', 'assign'), ('4', 'lit'),
                        (')', 'closed_bracket'), ('{', 'open_bracket'), ('print', 'print'), ('(', 'open_bracket'),
                        ('x', 'ident'), (')', 'closed_bracket'), (';', 'semicolon'), ('}', 'closed_bracket')]

def test_parser1():
    source = load_test_source()
    ts = lexer.token_stream(source)
    print(parsing.parse(ts))

test_lexer1()
test_parser1()