# Generated from Sentiment.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SentimentParser import SentimentParser
else:
    from SentimentParser import SentimentParser

# This class defines a complete generic visitor for a parse tree produced by SentimentParser.

class SentimentVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SentimentParser#program.
    def visitProgram(self, ctx:SentimentParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentimentParser#statement.
    def visitStatement(self, ctx:SentimentParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentimentParser#statement1.
    def visitStatement1(self, ctx:SentimentParser.Statement1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentimentParser#subject.
    def visitSubject(self, ctx:SentimentParser.SubjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentimentParser#verb.
    def visitVerb(self, ctx:SentimentParser.VerbContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentimentParser#neu_v.
    def visitNeu_v(self, ctx:SentimentParser.Neu_vContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentimentParser#pos_v.
    def visitPos_v(self, ctx:SentimentParser.Pos_vContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentimentParser#neg_v.
    def visitNeg_v(self, ctx:SentimentParser.Neg_vContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentimentParser#obj.
    def visitObj(self, ctx:SentimentParser.ObjContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentimentParser#statement2.
    def visitStatement2(self, ctx:SentimentParser.Statement2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentimentParser#noun.
    def visitNoun(self, ctx:SentimentParser.NounContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentimentParser#description_phrase.
    def visitDescription_phrase(self, ctx:SentimentParser.Description_phraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentimentParser#neu_ph.
    def visitNeu_ph(self, ctx:SentimentParser.Neu_phContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentimentParser#pos_ph.
    def visitPos_ph(self, ctx:SentimentParser.Pos_phContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentimentParser#neg_ph.
    def visitNeg_ph(self, ctx:SentimentParser.Neg_phContext):
        return self.visitChildren(ctx)



del SentimentParser