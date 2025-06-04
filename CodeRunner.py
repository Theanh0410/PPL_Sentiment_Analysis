from ASTUtils import *

class CodeRunner():
    def visitProgram(self, ctx: Prog):
        return ctx.statement.accept(self)

    def visitStatement1(self, ctx: Statement1):
        sentiment_type, verb = ctx.verb
        return {
            "type": "statement1",
            "verb": verb,
            "object": ctx.obj,
            "sentiment": sentiment_type
        }

    def visitStatement2(self, ctx: Statement2):
        sentiment_type, desc = ctx.description
        return {
            "type": "statement2",
            "noun": ctx.noun,
            "description": desc,
            "sentiment": sentiment_type
        }
