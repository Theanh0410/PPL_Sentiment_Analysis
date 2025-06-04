# Generated from Sentiment.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\34")
        buf.write("T\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\4\17\t\17\4\20\t\20\3\2\3\2\3\3\3\3\5\3%\n\3\3\4\5")
        buf.write("\4(\n\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\6\5\6\62\n\6\3\7")
        buf.write("\3\7\3\b\3\b\3\t\3\t\3\n\7\n;\n\n\f\n\16\n>\13\n\3\13")
        buf.write("\3\13\3\13\3\f\7\fD\n\f\f\f\16\fG\13\f\3\r\3\r\3\r\5\r")
        buf.write("L\n\r\3\16\3\16\3\17\3\17\3\20\3\20\3\20\2\2\21\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\32\34\36\2\t\3\2\3\5\3\2\6\b")
        buf.write("\3\2\t\13\3\2\f\16\3\2\17\21\3\2\22\26\3\2\27\32\2L\2")
        buf.write(" \3\2\2\2\4$\3\2\2\2\6\'\3\2\2\2\b,\3\2\2\2\n\61\3\2\2")
        buf.write("\2\f\63\3\2\2\2\16\65\3\2\2\2\20\67\3\2\2\2\22<\3\2\2")
        buf.write("\2\24?\3\2\2\2\26E\3\2\2\2\30K\3\2\2\2\32M\3\2\2\2\34")
        buf.write("O\3\2\2\2\36Q\3\2\2\2 !\5\4\3\2!\3\3\2\2\2\"%\5\6\4\2")
        buf.write("#%\5\24\13\2$\"\3\2\2\2$#\3\2\2\2%\5\3\2\2\2&(\5\b\5\2")
        buf.write("\'&\3\2\2\2\'(\3\2\2\2()\3\2\2\2)*\5\n\6\2*+\5\22\n\2")
        buf.write("+\7\3\2\2\2,-\t\2\2\2-\t\3\2\2\2.\62\5\f\7\2/\62\5\16")
        buf.write("\b\2\60\62\5\20\t\2\61.\3\2\2\2\61/\3\2\2\2\61\60\3\2")
        buf.write("\2\2\62\13\3\2\2\2\63\64\t\3\2\2\64\r\3\2\2\2\65\66\t")
        buf.write("\4\2\2\66\17\3\2\2\2\678\t\5\2\28\21\3\2\2\29;\7\33\2")
        buf.write("\2:9\3\2\2\2;>\3\2\2\2<:\3\2\2\2<=\3\2\2\2=\23\3\2\2\2")
        buf.write("><\3\2\2\2?@\5\26\f\2@A\5\30\r\2A\25\3\2\2\2BD\7\33\2")
        buf.write("\2CB\3\2\2\2DG\3\2\2\2EC\3\2\2\2EF\3\2\2\2F\27\3\2\2\2")
        buf.write("GE\3\2\2\2HL\5\32\16\2IL\5\34\17\2JL\5\36\20\2KH\3\2\2")
        buf.write("\2KI\3\2\2\2KJ\3\2\2\2L\31\3\2\2\2MN\t\6\2\2N\33\3\2\2")
        buf.write("\2OP\t\7\2\2P\35\3\2\2\2QR\t\b\2\2R\37\3\2\2\2\b$\'\61")
        buf.write("<EK")
        return buf.getvalue()


class SentimentParser ( Parser ):

    grammarFileName = "Sentiment.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'i'", "'you'", "'we'", "'understand'", 
                     "'know'", "'recognize'", "'like'", "'love'", "'enjoy'", 
                     "'hate'", "'dislike'", "'despise'", "'average'", "'normal'", 
                     "'mediocre'", "'good'", "'amazing'", "'excellent'", 
                     "'wonderful'", "'fantastic'", "'bad'", "'horrible'", 
                     "'boring'", "'terrible'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "STRING", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_statement1 = 2
    RULE_subject = 3
    RULE_verb = 4
    RULE_neu_v = 5
    RULE_pos_v = 6
    RULE_neg_v = 7
    RULE_obj = 8
    RULE_statement2 = 9
    RULE_noun = 10
    RULE_description_phrase = 11
    RULE_neu_ph = 12
    RULE_pos_ph = 13
    RULE_neg_ph = 14

    ruleNames =  [ "program", "statement", "statement1", "subject", "verb", 
                   "neu_v", "pos_v", "neg_v", "obj", "statement2", "noun", 
                   "description_phrase", "neu_ph", "pos_ph", "neg_ph" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    STRING=25
    WS=26

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(SentimentParser.StatementContext,0)


        def getRuleIndex(self):
            return SentimentParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = SentimentParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement1(self):
            return self.getTypedRuleContext(SentimentParser.Statement1Context,0)


        def statement2(self):
            return self.getTypedRuleContext(SentimentParser.Statement2Context,0)


        def getRuleIndex(self):
            return SentimentParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = SentimentParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 34
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SentimentParser.T__0, SentimentParser.T__1, SentimentParser.T__2, SentimentParser.T__3, SentimentParser.T__4, SentimentParser.T__5, SentimentParser.T__6, SentimentParser.T__7, SentimentParser.T__8, SentimentParser.T__9, SentimentParser.T__10, SentimentParser.T__11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                self.statement1()
                pass
            elif token in [SentimentParser.T__12, SentimentParser.T__13, SentimentParser.T__14, SentimentParser.T__15, SentimentParser.T__16, SentimentParser.T__17, SentimentParser.T__18, SentimentParser.T__19, SentimentParser.T__20, SentimentParser.T__21, SentimentParser.T__22, SentimentParser.T__23, SentimentParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                self.statement2()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def verb(self):
            return self.getTypedRuleContext(SentimentParser.VerbContext,0)


        def obj(self):
            return self.getTypedRuleContext(SentimentParser.ObjContext,0)


        def subject(self):
            return self.getTypedRuleContext(SentimentParser.SubjectContext,0)


        def getRuleIndex(self):
            return SentimentParser.RULE_statement1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement1" ):
                return visitor.visitStatement1(self)
            else:
                return visitor.visitChildren(self)




    def statement1(self):

        localctx = SentimentParser.Statement1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SentimentParser.T__0) | (1 << SentimentParser.T__1) | (1 << SentimentParser.T__2))) != 0):
                self.state = 36
                self.subject()


            self.state = 39
            self.verb()
            self.state = 40
            self.obj()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubjectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SentimentParser.RULE_subject

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubject" ):
                return visitor.visitSubject(self)
            else:
                return visitor.visitChildren(self)




    def subject(self):

        localctx = SentimentParser.SubjectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_subject)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SentimentParser.T__0) | (1 << SentimentParser.T__1) | (1 << SentimentParser.T__2))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VerbContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def neu_v(self):
            return self.getTypedRuleContext(SentimentParser.Neu_vContext,0)


        def pos_v(self):
            return self.getTypedRuleContext(SentimentParser.Pos_vContext,0)


        def neg_v(self):
            return self.getTypedRuleContext(SentimentParser.Neg_vContext,0)


        def getRuleIndex(self):
            return SentimentParser.RULE_verb

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVerb" ):
                return visitor.visitVerb(self)
            else:
                return visitor.visitChildren(self)




    def verb(self):

        localctx = SentimentParser.VerbContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_verb)
        try:
            self.state = 47
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SentimentParser.T__3, SentimentParser.T__4, SentimentParser.T__5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 44
                self.neu_v()
                pass
            elif token in [SentimentParser.T__6, SentimentParser.T__7, SentimentParser.T__8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 45
                self.pos_v()
                pass
            elif token in [SentimentParser.T__9, SentimentParser.T__10, SentimentParser.T__11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 46
                self.neg_v()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Neu_vContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SentimentParser.RULE_neu_v

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNeu_v" ):
                return visitor.visitNeu_v(self)
            else:
                return visitor.visitChildren(self)




    def neu_v(self):

        localctx = SentimentParser.Neu_vContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_neu_v)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SentimentParser.T__3) | (1 << SentimentParser.T__4) | (1 << SentimentParser.T__5))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pos_vContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SentimentParser.RULE_pos_v

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPos_v" ):
                return visitor.visitPos_v(self)
            else:
                return visitor.visitChildren(self)




    def pos_v(self):

        localctx = SentimentParser.Pos_vContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_pos_v)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SentimentParser.T__6) | (1 << SentimentParser.T__7) | (1 << SentimentParser.T__8))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Neg_vContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SentimentParser.RULE_neg_v

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNeg_v" ):
                return visitor.visitNeg_v(self)
            else:
                return visitor.visitChildren(self)




    def neg_v(self):

        localctx = SentimentParser.Neg_vContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_neg_v)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SentimentParser.T__9) | (1 << SentimentParser.T__10) | (1 << SentimentParser.T__11))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(SentimentParser.STRING)
            else:
                return self.getToken(SentimentParser.STRING, i)

        def getRuleIndex(self):
            return SentimentParser.RULE_obj

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObj" ):
                return visitor.visitObj(self)
            else:
                return visitor.visitChildren(self)




    def obj(self):

        localctx = SentimentParser.ObjContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_obj)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SentimentParser.STRING:
                self.state = 55
                self.match(SentimentParser.STRING)
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def noun(self):
            return self.getTypedRuleContext(SentimentParser.NounContext,0)


        def description_phrase(self):
            return self.getTypedRuleContext(SentimentParser.Description_phraseContext,0)


        def getRuleIndex(self):
            return SentimentParser.RULE_statement2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement2" ):
                return visitor.visitStatement2(self)
            else:
                return visitor.visitChildren(self)




    def statement2(self):

        localctx = SentimentParser.Statement2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_statement2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.noun()
            self.state = 62
            self.description_phrase()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NounContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(SentimentParser.STRING)
            else:
                return self.getToken(SentimentParser.STRING, i)

        def getRuleIndex(self):
            return SentimentParser.RULE_noun

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNoun" ):
                return visitor.visitNoun(self)
            else:
                return visitor.visitChildren(self)




    def noun(self):

        localctx = SentimentParser.NounContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_noun)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SentimentParser.STRING:
                self.state = 64
                self.match(SentimentParser.STRING)
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Description_phraseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def neu_ph(self):
            return self.getTypedRuleContext(SentimentParser.Neu_phContext,0)


        def pos_ph(self):
            return self.getTypedRuleContext(SentimentParser.Pos_phContext,0)


        def neg_ph(self):
            return self.getTypedRuleContext(SentimentParser.Neg_phContext,0)


        def getRuleIndex(self):
            return SentimentParser.RULE_description_phrase

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDescription_phrase" ):
                return visitor.visitDescription_phrase(self)
            else:
                return visitor.visitChildren(self)




    def description_phrase(self):

        localctx = SentimentParser.Description_phraseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_description_phrase)
        try:
            self.state = 73
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SentimentParser.T__12, SentimentParser.T__13, SentimentParser.T__14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self.neu_ph()
                pass
            elif token in [SentimentParser.T__15, SentimentParser.T__16, SentimentParser.T__17, SentimentParser.T__18, SentimentParser.T__19]:
                self.enterOuterAlt(localctx, 2)
                self.state = 71
                self.pos_ph()
                pass
            elif token in [SentimentParser.T__20, SentimentParser.T__21, SentimentParser.T__22, SentimentParser.T__23]:
                self.enterOuterAlt(localctx, 3)
                self.state = 72
                self.neg_ph()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Neu_phContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SentimentParser.RULE_neu_ph

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNeu_ph" ):
                return visitor.visitNeu_ph(self)
            else:
                return visitor.visitChildren(self)




    def neu_ph(self):

        localctx = SentimentParser.Neu_phContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_neu_ph)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SentimentParser.T__12) | (1 << SentimentParser.T__13) | (1 << SentimentParser.T__14))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pos_phContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SentimentParser.RULE_pos_ph

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPos_ph" ):
                return visitor.visitPos_ph(self)
            else:
                return visitor.visitChildren(self)




    def pos_ph(self):

        localctx = SentimentParser.Pos_phContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_pos_ph)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SentimentParser.T__15) | (1 << SentimentParser.T__16) | (1 << SentimentParser.T__17) | (1 << SentimentParser.T__18) | (1 << SentimentParser.T__19))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Neg_phContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SentimentParser.RULE_neg_ph

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNeg_ph" ):
                return visitor.visitNeg_ph(self)
            else:
                return visitor.visitChildren(self)




    def neg_ph(self):

        localctx = SentimentParser.Neg_phContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_neg_ph)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SentimentParser.T__20) | (1 << SentimentParser.T__21) | (1 << SentimentParser.T__22) | (1 << SentimentParser.T__23))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





