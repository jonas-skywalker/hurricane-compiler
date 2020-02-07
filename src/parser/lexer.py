import tokens

def split_surround(source, c, label):
    spl = source.split(c)
    ret = []
    for s in spl:
        ret += [(s, None), (c, label)]
    return ret[:-1]

def split_symbols(source):
    labels = [
        (" ", "space"),
        (";", "semicolon"),
        ("{", "open_bracket"),
        ("}", "closed_bracket"),
        ("(", "open_bracket"),
        (")", "closed_bracket"),
        ("<=", "smaller_equals"),
        (">=", "bigger_equals"),
        ("==", "equals"),
        ("=", "assign"),
        ("+", "plus"),
        ("-", "minus"),
        ("*", "multi"),
        ("/", "div")
    ]
    sources = [(source, None)]
    for (c, label) in labels:
        new_sources = []
        for (split_word, matched_label) in sources:
            if matched_label:
                new_sources.append((split_word, matched_label))
            else:
                new_sources += split_surround(split_word, c, label)
        sources = new_sources
    return sources

def match_keywords(tokens):
    keywords = [
        "if", "while", "print", "input", "int"
    ]
    for (index, (word, label)) in enumerate(tokens):
        if not label and word in keywords:
            tokens[index] = (word, word)
        return tokens

def match_idents_and_lits(tokens):
    for (index, (word, label)) in enumerate(tokens):
        if not label:
            new_label = None
            if word.isdigit():
                new_label = "lit"
            else:
                new_label = "ident"
            tokens[index] = (word, new_label)
    return tokens

def lex(source):
    spl = split_symbols(source)
    spl = match_keywords(spl)
    spl = match_idents_and_lits(spl)
    return spl

def token_stream(source):
    return iter(lex(source))