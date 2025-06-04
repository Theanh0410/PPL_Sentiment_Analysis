from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Tuple, Union

def printlist(lst, f=str, start="[", sepa=",", end="]"):
    return start + sepa.join(f(i) for i in lst) + end


class AST(ABC):
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    @abstractmethod
    def accept(self, v):
        pass

# Root node 
@dataclass
class Prog(AST):
    statement: AST

    def __str__(self):
        return f"Prog({str(self.statement)})"

    def accept(self, v):
        return v.visitProgram(self)

# For statement1
@dataclass
class Statement1(AST):
    verb: str
    obj: str

    def __str__(self):
        return f"Statement1(verb={self.verb}, obj={self.obj})"

    def accept(self, v):
        return v.visitStatement1(self)

# For statement2
@dataclass
class Statement2(AST):
    noun: str;
    description: str

    def __str__(self):
        return f"Statement2(noun={self.noun}, description={self.description})"

    def accept(self, v):
        return v.visitStatement2(self)
