# im going to go fucking insane
from dataclasses import dataclass

@dataclass
class Token:
    type: str
    value: int | None = None

source = "1 PLUS 2"

opmodes = [
    "PLUS",
    "SUBTRACT",
    "MULTIPLY",
    "DIVIDE",
]


def tokenize(source: str):
    tokens = []
    words = source.split()

    for word in words:
        if word.isdigit():
            tokens.append(Token("NUMBER", int(word)))
        elif word in opmodes:
            tokens.append(Token(word))
        else:
            raise SyntaxError(f"Unknown token: {word}")

    return tokens

full_token = tokenize(source)

print(full_token[0])
