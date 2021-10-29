from enum import Enum, auto

ADDPRED = SUBPRED = 1
MULPRED = DIVPRED = 2
EXPPRED = 3
FUNCPRED = 4

class Assoc(Enum):
    NONE = auto()
    LEFT = auto()
    RIGHT = auto()

class Type(Enum):
    NUMBER = auto()
    OPERATOR = auto()
    FUNCTION = auto()
    VARIABLE = auto()
    CONSTANT = auto()
    LPAREN = auto()
    RPAREN = auto()

class Token():
    def __init__(self, type, **kwargs):
        self.type = type
        if type == Type.NUMBER:
            self.val = kwargs['val']
        elif type == Type.OPERATOR:
            self.op = kwargs['op']
            if self.op == '+':
                self.pred = ADDPRED
                self.argnum = 2
                self.assoc = Assoc.NONE
            elif self.op == '-':
                self.pred = SUBPRED
                self.argnum = 2
                self.assoc = Assoc.LEFT
            elif self.op == '*':
                self.pred = MULPRED
                self.argnum = 2
                self.assoc = Assoc.NONE
            elif self.op == '/':
                self.pred = DIVPRED
                self.argnum = 2
                self.assoc = Assoc.LEFT
            elif self.op == '^':
                self.pred = EXPPRED
                self.argnum = 2
                self.assoc = Assoc.RIGHT
            else:
                raise ValueError('Not supported operator: ' + self.op)
        elif type == Type.FUNCTION:
            raise ValueError('Functions not yet implemented.')
        elif type == Type.VARIABLE:
            self.name = kwargs['name']
        elif type == Type.CONSTANT:
            self.name = kwargs['name']
            self.val = kwargs['val']
        elif type == Type.RPAREN:
            pass
        elif type == Type.LPAREN:
            pass
        else:
            raise ValueError('Not supported token: ' + str(type))

    def tokenize(str):
        raise ValueError('Tokenize Method not implemented yet.')



def main():
    a = Token(Type.NUMBER, val=1)
    print(a.tokenize('a'))
    Token.tokenize('a')

if __name__ == '__main__':
    main()