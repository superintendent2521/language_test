# im going to go fucking insane
from dataclasses import dataclass

@dataclass
class Token:
    type: str
    value: int | str | None = None

source = "1 PLUS 2"

OPMAP = {
    "PLUS": "+",
    "SUBTRACT": "-",
    "MULTIPLY": "*",
    "DIVIDE": "/",
}



def tokenize(source: str):
    tokens = []
    words = source.split()

    for word in words:
        if word.isdigit():
            tokens.append(Token("NUMBER", int(word)))

        elif word in OPMAP:
            tokens.append(Token("OPERATOR", OPMAP[word]))

        else:
            raise SyntaxError(f"Unknown token: {word}")

    return tokens



def execute():
    print(source)
    tokens = tokenize(source)
    values = [token.value for token in tokens]
    print(values)
    expression = "".join(map(str, values))
    print(expression)
    result = eval(expression)
    print(result)
execute()
