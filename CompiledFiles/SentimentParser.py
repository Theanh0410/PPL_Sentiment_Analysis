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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3+")
        buf.write("d\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\3\2\3\2\3\3\3\3\5\3+\n\3\3\4\5\4.\n\4\3\4\3\4\3\4\3\5")
        buf.write("\3\5\3\6\3\6\3\6\5\68\n\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n")
        buf.write("\3\n\3\13\3\13\3\f\5\fE\n\f\3\f\3\f\6\fI\n\f\r\f\16\f")
        buf.write("J\3\r\3\r\3\r\3\r\3\16\3\16\5\16S\n\16\3\16\3\16\3\17")
        buf.write("\3\17\3\20\3\20\3\20\5\20\\\n\20\3\21\3\21\3\22\3\22\3")
        buf.write("\23\3\23\3\23\2\2\24\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\34\36 \"$\2\f\3\2\3\5\3\2\6\b\3\2\t\f\3\2\r\17\3\2\20")
        buf.write("\22\3\2\23\26\3\2\27\36\3\2\37!\4\2\f\f\"%\3\2&)\2\\\2")
        buf.write("&\3\2\2\2\4*\3\2\2\2\6-\3\2\2\2\b\62\3\2\2\2\n\67\3\2")
        buf.write("\2\2\f9\3\2\2\2\16;\3\2\2\2\20=\3\2\2\2\22?\3\2\2\2\24")
        buf.write("A\3\2\2\2\26D\3\2\2\2\30L\3\2\2\2\32R\3\2\2\2\34V\3\2")
        buf.write("\2\2\36[\3\2\2\2 ]\3\2\2\2\"_\3\2\2\2$a\3\2\2\2&\'\5\4")
        buf.write("\3\2\'\3\3\2\2\2(+\5\6\4\2)+\5\30\r\2*(\3\2\2\2*)\3\2")
        buf.write("\2\2+\5\3\2\2\2,.\5\b\5\2-,\3\2\2\2-.\3\2\2\2./\3\2\2")
        buf.write("\2/\60\5\n\6\2\60\61\5\26\f\2\61\7\3\2\2\2\62\63\t\2\2")
        buf.write("\2\63\t\3\2\2\2\648\5\f\7\2\658\5\16\b\2\668\5\20\t\2")
        buf.write("\67\64\3\2\2\2\67\65\3\2\2\2\67\66\3\2\2\28\13\3\2\2\2")
        buf.write("9:\t\3\2\2:\r\3\2\2\2;<\t\4\2\2<\17\3\2\2\2=>\t\5\2\2")
        buf.write(">\21\3\2\2\2?@\t\6\2\2@\23\3\2\2\2AB\t\7\2\2B\25\3\2\2")
        buf.write("\2CE\5\22\n\2DC\3\2\2\2DE\3\2\2\2EH\3\2\2\2FI\5\24\13")
        buf.write("\2GI\7*\2\2HF\3\2\2\2HG\3\2\2\2IJ\3\2\2\2JH\3\2\2\2JK")
        buf.write("\3\2\2\2K\27\3\2\2\2LM\5\32\16\2MN\5\34\17\2NO\5\36\20")
        buf.write("\2O\31\3\2\2\2PS\5\22\n\2QS\5\24\13\2RP\3\2\2\2RQ\3\2")
        buf.write("\2\2RS\3\2\2\2ST\3\2\2\2TU\7*\2\2U\33\3\2\2\2VW\t\b\2")
        buf.write("\2W\35\3\2\2\2X\\\5 \21\2Y\\\5\"\22\2Z\\\5$\23\2[X\3\2")
        buf.write("\2\2[Y\3\2\2\2[Z\3\2\2\2\\\37\3\2\2\2]^\t\t\2\2^!\3\2")
        buf.write("\2\2_`\t\n\2\2`#\3\2\2\2ab\t\13\2\2b%\3\2\2\2\n*-\67D")
        buf.write("HJR[")
        return buf.getvalue()


class SentimentParser ( Parser ):

    grammarFileName = "Sentiment.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'i'", "'you'", "'we'", "'understand'", 
                     "'know'", "'recognize'", "'like'", "'love'", "'enjoy'", 
                     "'good'", "'hate'", "'dislike'", "'despise'", "'the'", 
                     "'an'", "'a'", "'this'", "'that'", "'there'", "'those'", 
                     "'is'", "'are'", "'seems'", "'look'", "'feels'", "'seem'", 
                     "'feel'", "'looks'", "'average'", "'normal'", "'mediocre'", 
                     "'amazing'", "'excellent'", "'wonderful'", "'fantastic'", 
                     "'bad'", "'horrible'", "'boring'", "'terrible'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "STRING", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_statement1 = 2
    RULE_subj = 3
    RULE_verb = 4
    RULE_neu_v = 5
    RULE_pos_v = 6
    RULE_neg_v = 7
    RULE_article = 8
    RULE_pronoun = 9
    RULE_obj = 10
    RULE_statement2 = 11
    RULE_noun = 12
    RULE_state_verb = 13
    RULE_description_phrase = 14
    RULE_neu_ph = 15
    RULE_pos_ph = 16
    RULE_neg_ph = 17

    ruleNames =  [ "program", "statement", "statement1", "subj", "verb", 
                   "neu_v", "pos_v", "neg_v", "article", "pronoun", "obj", 
                   "statement2", "noun", "state_verb", "description_phrase", 
                   "neu_ph", "pos_ph", "neg_ph" ]

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
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    STRING=40
    WS=41

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




    def program(self):

        localctx = SentimentParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
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




    def statement(self):

        localctx = SentimentParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 40
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SentimentParser.T__0, SentimentParser.T__1, SentimentParser.T__2, SentimentParser.T__3, SentimentParser.T__4, SentimentParser.T__5, SentimentParser.T__6, SentimentParser.T__7, SentimentParser.T__8, SentimentParser.T__9, SentimentParser.T__10, SentimentParser.T__11, SentimentParser.T__12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.statement1()
                pass
            elif token in [SentimentParser.T__13, SentimentParser.T__14, SentimentParser.T__15, SentimentParser.T__16, SentimentParser.T__17, SentimentParser.T__18, SentimentParser.T__19, SentimentParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
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


        def subj(self):
            return self.getTypedRuleContext(SentimentParser.SubjContext,0)


        def getRuleIndex(self):
            return SentimentParser.RULE_statement1




    def statement1(self):

        localctx = SentimentParser.Statement1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SentimentParser.T__0) | (1 << SentimentParser.T__1) | (1 << SentimentParser.T__2))) != 0):
                self.state = 42
                self.subj()


            self.state = 45
            self.verb()
            self.state = 46
            self.obj()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubjContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SentimentParser.RULE_subj




    def subj(self):

        localctx = SentimentParser.SubjContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_subj)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
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




    def verb(self):

        localctx = SentimentParser.VerbContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_verb)
        try:
            self.state = 53
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SentimentParser.T__3, SentimentParser.T__4, SentimentParser.T__5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.neu_v()
                pass
            elif token in [SentimentParser.T__6, SentimentParser.T__7, SentimentParser.T__8, SentimentParser.T__9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.pos_v()
                pass
            elif token in [SentimentParser.T__10, SentimentParser.T__11, SentimentParser.T__12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 52
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




    def neu_v(self):

        localctx = SentimentParser.Neu_vContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_neu_v)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
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




    def pos_v(self):

        localctx = SentimentParser.Pos_vContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_pos_v)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SentimentParser.T__6) | (1 << SentimentParser.T__7) | (1 << SentimentParser.T__8) | (1 << SentimentParser.T__9))) != 0)):
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




    def neg_v(self):

        localctx = SentimentParser.Neg_vContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_neg_v)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SentimentParser.T__10) | (1 << SentimentParser.T__11) | (1 << SentimentParser.T__12))) != 0)):
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


    class ArticleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SentimentParser.RULE_article




    def article(self):

        localctx = SentimentParser.ArticleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_article)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SentimentParser.T__13) | (1 << SentimentParser.T__14) | (1 << SentimentParser.T__15))) != 0)):
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


    class PronounContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SentimentParser.RULE_pronoun




    def pronoun(self):

        localctx = SentimentParser.PronounContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_pronoun)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SentimentParser.T__16) | (1 << SentimentParser.T__17) | (1 << SentimentParser.T__18) | (1 << SentimentParser.T__19))) != 0)):
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

        def article(self):
            return self.getTypedRuleContext(SentimentParser.ArticleContext,0)


        def pronoun(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SentimentParser.PronounContext)
            else:
                return self.getTypedRuleContext(SentimentParser.PronounContext,i)


        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(SentimentParser.STRING)
            else:
                return self.getToken(SentimentParser.STRING, i)

        def getRuleIndex(self):
            return SentimentParser.RULE_obj




    def obj(self):

        localctx = SentimentParser.ObjContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_obj)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SentimentParser.T__13) | (1 << SentimentParser.T__14) | (1 << SentimentParser.T__15))) != 0):
                self.state = 65
                self.article()


            self.state = 70 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 70
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SentimentParser.T__16, SentimentParser.T__17, SentimentParser.T__18, SentimentParser.T__19]:
                    self.state = 68
                    self.pronoun()
                    pass
                elif token in [SentimentParser.STRING]:
                    self.state = 69
                    self.match(SentimentParser.STRING)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 72 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SentimentParser.T__16) | (1 << SentimentParser.T__17) | (1 << SentimentParser.T__18) | (1 << SentimentParser.T__19) | (1 << SentimentParser.STRING))) != 0)):
                    break

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


        def state_verb(self):
            return self.getTypedRuleContext(SentimentParser.State_verbContext,0)


        def description_phrase(self):
            return self.getTypedRuleContext(SentimentParser.Description_phraseContext,0)


        def getRuleIndex(self):
            return SentimentParser.RULE_statement2




    def statement2(self):

        localctx = SentimentParser.Statement2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_statement2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.noun()
            self.state = 75
            self.state_verb()
            self.state = 76
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

        def STRING(self):
            return self.getToken(SentimentParser.STRING, 0)

        def article(self):
            return self.getTypedRuleContext(SentimentParser.ArticleContext,0)


        def pronoun(self):
            return self.getTypedRuleContext(SentimentParser.PronounContext,0)


        def getRuleIndex(self):
            return SentimentParser.RULE_noun




    def noun(self):

        localctx = SentimentParser.NounContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_noun)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SentimentParser.T__13, SentimentParser.T__14, SentimentParser.T__15]:
                self.state = 78
                self.article()
                pass
            elif token in [SentimentParser.T__16, SentimentParser.T__17, SentimentParser.T__18, SentimentParser.T__19]:
                self.state = 79
                self.pronoun()
                pass
            elif token in [SentimentParser.STRING]:
                pass
            else:
                pass
            self.state = 82
            self.match(SentimentParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class State_verbContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SentimentParser.RULE_state_verb




    def state_verb(self):

        localctx = SentimentParser.State_verbContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_state_verb)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SentimentParser.T__20) | (1 << SentimentParser.T__21) | (1 << SentimentParser.T__22) | (1 << SentimentParser.T__23) | (1 << SentimentParser.T__24) | (1 << SentimentParser.T__25) | (1 << SentimentParser.T__26) | (1 << SentimentParser.T__27))) != 0)):
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




    def description_phrase(self):

        localctx = SentimentParser.Description_phraseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_description_phrase)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SentimentParser.T__28, SentimentParser.T__29, SentimentParser.T__30]:
                self.state = 86
                self.neu_ph()
                pass
            elif token in [SentimentParser.T__9, SentimentParser.T__31, SentimentParser.T__32, SentimentParser.T__33, SentimentParser.T__34]:
                self.state = 87
                self.pos_ph()
                pass
            elif token in [SentimentParser.T__35, SentimentParser.T__36, SentimentParser.T__37, SentimentParser.T__38]:
                self.state = 88
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




    def neu_ph(self):

        localctx = SentimentParser.Neu_phContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_neu_ph)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SentimentParser.T__28) | (1 << SentimentParser.T__29) | (1 << SentimentParser.T__30))) != 0)):
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




    def pos_ph(self):

        localctx = SentimentParser.Pos_phContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_pos_ph)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SentimentParser.T__9) | (1 << SentimentParser.T__31) | (1 << SentimentParser.T__32) | (1 << SentimentParser.T__33) | (1 << SentimentParser.T__34))) != 0)):
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




    def neg_ph(self):

        localctx = SentimentParser.Neg_phContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_neg_ph)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SentimentParser.T__35) | (1 << SentimentParser.T__36) | (1 << SentimentParser.T__37) | (1 << SentimentParser.T__38))) != 0)):
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





