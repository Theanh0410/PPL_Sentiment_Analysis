from CompiledFiles.SentimentVisitor import SentimentVisitor
from CompiledFiles.SentimentParser import SentimentParser
from ASTUtils import *

class ASTGeneration(SentimentVisitor):

    def visitProgram(self, ctx: SentimentParser.ProgramContext):
        return ctx.statement().accept(self)

    def visitStatement(self, ctx: SentimentParser.StatementContext):
        if ctx.statement1():
            return ctx.statement1().accept(self)
        else:
            return ctx.statement2().accept(self)

    def visitStatement1(self, ctx: SentimentParser.Statement1Context):
        verb = ctx.verb().accept(self)
        obj = ctx.obj().accept(self)
        return Statement1(verb, obj)

    def visitVerb(self, ctx: SentimentParser.VerbContext):
        if ctx.pos_v():
            return ("postive", ctx.pos_v().getText())
        elif ctx.neg_v():
            return ("negative", ctx.neg_v().getText())
        elif ctx.neu_v():
            return ("neutral", ctx.neu_v().getText())

    def visitObj(self, ctx: SentimentParser.ObjContext):
        words = [token.getText() for token in ctx.children]
        return " ".join(words)

    def visitStatement2(self, ctx: SentimentParser.Statement2Context):
        noun = ctx.noun().accept(self)
        desc = ctx.description_phrase().accept(self)
        return Statement2(noun, desc)


    def visitNoun(self, ctx: SentimentParser.NounContext):
            words = [token.getText() for token in ctx.children]
            return " ".join(words)

    def visitDescription_phrase(self, ctx: SentimentParser.Description_phraseContext):
        if ctx.pos_ph():
            return ("postive", ctx.pos_ph().getText())
        elif ctx.neg_ph():
            return ("negative", ctx.neg_ph().getText())
        elif ctx.neu_ph():
            return ("neutral", ctx.neu_ph().getText())
