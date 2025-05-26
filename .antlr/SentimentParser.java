// Generated from d:/OneDrive/IU/Sem 6/PPL/Project/PPL_Sentiment_Analysis/Sentiment.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class SentimentParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, T__28=29, T__29=30, T__30=31, 
		T__31=32, T__32=33, T__33=34, T__34=35, T__35=36, T__36=37, T__37=38, 
		T__38=39, STRING=40, WS=41;
	public static final int
		RULE_program = 0, RULE_statement = 1, RULE_statement1 = 2, RULE_subj = 3, 
		RULE_verb = 4, RULE_neu_v = 5, RULE_pos_v = 6, RULE_neg_v = 7, RULE_article = 8, 
		RULE_pronoun = 9, RULE_obj = 10, RULE_statement2 = 11, RULE_noun = 12, 
		RULE_state_verb = 13, RULE_description_phrase = 14, RULE_neu_ph = 15, 
		RULE_pos_ph = 16, RULE_neg_ph = 17;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "statement", "statement1", "subj", "verb", "neu_v", "pos_v", 
			"neg_v", "article", "pronoun", "obj", "statement2", "noun", "state_verb", 
			"description_phrase", "neu_ph", "pos_ph", "neg_ph"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'i'", "'you'", "'we'", "'understand'", "'know'", "'recognize'", 
			"'like'", "'love'", "'enjoy'", "'good'", "'hate'", "'dislike'", "'despise'", 
			"'the'", "'an'", "'a'", "'this'", "'that'", "'there'", "'those'", "'is'", 
			"'are'", "'seems'", "'look'", "'feels'", "'seem'", "'feel'", "'looks'", 
			"'average'", "'normal'", "'mediocre'", "'amazing'", "'excellent'", "'wonderful'", 
			"'fantastic'", "'bad'", "'horrible'", "'boring'", "'terrible'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, "STRING", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Sentiment.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public SentimentParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(36);
			statement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public Statement1Context statement1() {
			return getRuleContext(Statement1Context.class,0);
		}
		public Statement2Context statement2() {
			return getRuleContext(Statement2Context.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_statement);
		try {
			setState(40);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
			case T__1:
			case T__2:
			case T__3:
			case T__4:
			case T__5:
			case T__6:
			case T__7:
			case T__8:
			case T__9:
			case T__10:
			case T__11:
			case T__12:
				enterOuterAlt(_localctx, 1);
				{
				setState(38);
				statement1();
				}
				break;
			case T__13:
			case T__14:
			case T__15:
			case T__16:
			case T__17:
			case T__18:
			case T__19:
			case STRING:
				enterOuterAlt(_localctx, 2);
				{
				setState(39);
				statement2();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Statement1Context extends ParserRuleContext {
		public VerbContext verb() {
			return getRuleContext(VerbContext.class,0);
		}
		public ObjContext obj() {
			return getRuleContext(ObjContext.class,0);
		}
		public SubjContext subj() {
			return getRuleContext(SubjContext.class,0);
		}
		public Statement1Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement1; }
	}

	public final Statement1Context statement1() throws RecognitionException {
		Statement1Context _localctx = new Statement1Context(_ctx, getState());
		enterRule(_localctx, 4, RULE_statement1);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(43);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 14L) != 0)) {
				{
				setState(42);
				subj();
				}
			}

			setState(45);
			verb();
			setState(46);
			obj();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SubjContext extends ParserRuleContext {
		public SubjContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_subj; }
	}

	public final SubjContext subj() throws RecognitionException {
		SubjContext _localctx = new SubjContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_subj);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(48);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 14L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VerbContext extends ParserRuleContext {
		public Neu_vContext neu_v() {
			return getRuleContext(Neu_vContext.class,0);
		}
		public Pos_vContext pos_v() {
			return getRuleContext(Pos_vContext.class,0);
		}
		public Neg_vContext neg_v() {
			return getRuleContext(Neg_vContext.class,0);
		}
		public VerbContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_verb; }
	}

	public final VerbContext verb() throws RecognitionException {
		VerbContext _localctx = new VerbContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_verb);
		try {
			setState(53);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__3:
			case T__4:
			case T__5:
				enterOuterAlt(_localctx, 1);
				{
				setState(50);
				neu_v();
				}
				break;
			case T__6:
			case T__7:
			case T__8:
			case T__9:
				enterOuterAlt(_localctx, 2);
				{
				setState(51);
				pos_v();
				}
				break;
			case T__10:
			case T__11:
			case T__12:
				enterOuterAlt(_localctx, 3);
				{
				setState(52);
				neg_v();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Neu_vContext extends ParserRuleContext {
		public Neu_vContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_neu_v; }
	}

	public final Neu_vContext neu_v() throws RecognitionException {
		Neu_vContext _localctx = new Neu_vContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_neu_v);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(55);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 112L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Pos_vContext extends ParserRuleContext {
		public Pos_vContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_pos_v; }
	}

	public final Pos_vContext pos_v() throws RecognitionException {
		Pos_vContext _localctx = new Pos_vContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_pos_v);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(57);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 1920L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Neg_vContext extends ParserRuleContext {
		public Neg_vContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_neg_v; }
	}

	public final Neg_vContext neg_v() throws RecognitionException {
		Neg_vContext _localctx = new Neg_vContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_neg_v);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(59);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 14336L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ArticleContext extends ParserRuleContext {
		public ArticleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_article; }
	}

	public final ArticleContext article() throws RecognitionException {
		ArticleContext _localctx = new ArticleContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_article);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(61);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 114688L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PronounContext extends ParserRuleContext {
		public PronounContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_pronoun; }
	}

	public final PronounContext pronoun() throws RecognitionException {
		PronounContext _localctx = new PronounContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_pronoun);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(63);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 1966080L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ObjContext extends ParserRuleContext {
		public ArticleContext article() {
			return getRuleContext(ArticleContext.class,0);
		}
		public List<PronounContext> pronoun() {
			return getRuleContexts(PronounContext.class);
		}
		public PronounContext pronoun(int i) {
			return getRuleContext(PronounContext.class,i);
		}
		public List<TerminalNode> STRING() { return getTokens(SentimentParser.STRING); }
		public TerminalNode STRING(int i) {
			return getToken(SentimentParser.STRING, i);
		}
		public ObjContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_obj; }
	}

	public final ObjContext obj() throws RecognitionException {
		ObjContext _localctx = new ObjContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_obj);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(66);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 114688L) != 0)) {
				{
				setState(65);
				article();
				}
			}

			setState(70); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				setState(70);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__16:
				case T__17:
				case T__18:
				case T__19:
					{
					setState(68);
					pronoun();
					}
					break;
				case STRING:
					{
					setState(69);
					match(STRING);
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(72); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 1099513593856L) != 0) );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Statement2Context extends ParserRuleContext {
		public NounContext noun() {
			return getRuleContext(NounContext.class,0);
		}
		public State_verbContext state_verb() {
			return getRuleContext(State_verbContext.class,0);
		}
		public Description_phraseContext description_phrase() {
			return getRuleContext(Description_phraseContext.class,0);
		}
		public Statement2Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement2; }
	}

	public final Statement2Context statement2() throws RecognitionException {
		Statement2Context _localctx = new Statement2Context(_ctx, getState());
		enterRule(_localctx, 22, RULE_statement2);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(74);
			noun();
			setState(75);
			state_verb();
			setState(76);
			description_phrase();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class NounContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(SentimentParser.STRING, 0); }
		public ArticleContext article() {
			return getRuleContext(ArticleContext.class,0);
		}
		public PronounContext pronoun() {
			return getRuleContext(PronounContext.class,0);
		}
		public NounContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_noun; }
	}

	public final NounContext noun() throws RecognitionException {
		NounContext _localctx = new NounContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_noun);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(80);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__13:
			case T__14:
			case T__15:
				{
				setState(78);
				article();
				}
				break;
			case T__16:
			case T__17:
			case T__18:
			case T__19:
				{
				setState(79);
				pronoun();
				}
				break;
			case STRING:
				break;
			default:
				break;
			}
			setState(82);
			match(STRING);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class State_verbContext extends ParserRuleContext {
		public State_verbContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_state_verb; }
	}

	public final State_verbContext state_verb() throws RecognitionException {
		State_verbContext _localctx = new State_verbContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_state_verb);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(84);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 534773760L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Description_phraseContext extends ParserRuleContext {
		public Neu_phContext neu_ph() {
			return getRuleContext(Neu_phContext.class,0);
		}
		public Pos_phContext pos_ph() {
			return getRuleContext(Pos_phContext.class,0);
		}
		public Neg_phContext neg_ph() {
			return getRuleContext(Neg_phContext.class,0);
		}
		public Description_phraseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_description_phrase; }
	}

	public final Description_phraseContext description_phrase() throws RecognitionException {
		Description_phraseContext _localctx = new Description_phraseContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_description_phrase);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(89);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__28:
			case T__29:
			case T__30:
				{
				setState(86);
				neu_ph();
				}
				break;
			case T__9:
			case T__31:
			case T__32:
			case T__33:
			case T__34:
				{
				setState(87);
				pos_ph();
				}
				break;
			case T__35:
			case T__36:
			case T__37:
			case T__38:
				{
				setState(88);
				neg_ph();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Neu_phContext extends ParserRuleContext {
		public Neu_phContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_neu_ph; }
	}

	public final Neu_phContext neu_ph() throws RecognitionException {
		Neu_phContext _localctx = new Neu_phContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_neu_ph);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(91);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 3758096384L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Pos_phContext extends ParserRuleContext {
		public Pos_phContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_pos_ph; }
	}

	public final Pos_phContext pos_ph() throws RecognitionException {
		Pos_phContext _localctx = new Pos_phContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_pos_ph);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(93);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 64424510464L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Neg_phContext extends ParserRuleContext {
		public Neg_phContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_neg_ph; }
	}

	public final Neg_phContext neg_ph() throws RecognitionException {
		Neg_phContext _localctx = new Neg_phContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_neg_ph);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(95);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 1030792151040L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001)b\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002\u0002"+
		"\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002\u0005"+
		"\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002\b\u0007"+
		"\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002\f\u0007"+
		"\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f\u0002"+
		"\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0001\u0000\u0001\u0000\u0001"+
		"\u0001\u0001\u0001\u0003\u0001)\b\u0001\u0001\u0002\u0003\u0002,\b\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0003\u00046\b\u0004\u0001\u0005\u0001\u0005"+
		"\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001"+
		"\t\u0001\t\u0001\n\u0003\nC\b\n\u0001\n\u0001\n\u0004\nG\b\n\u000b\n\f"+
		"\nH\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0003"+
		"\fQ\b\f\u0001\f\u0001\f\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001"+
		"\u000e\u0003\u000eZ\b\u000e\u0001\u000f\u0001\u000f\u0001\u0010\u0001"+
		"\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0000\u0000\u0012\u0000\u0002"+
		"\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e"+
		" \"\u0000\n\u0001\u0000\u0001\u0003\u0001\u0000\u0004\u0006\u0001\u0000"+
		"\u0007\n\u0001\u0000\u000b\r\u0001\u0000\u000e\u0010\u0001\u0000\u0011"+
		"\u0014\u0001\u0000\u0015\u001c\u0001\u0000\u001d\u001f\u0002\u0000\n\n"+
		" #\u0001\u0000$\'Z\u0000$\u0001\u0000\u0000\u0000\u0002(\u0001\u0000\u0000"+
		"\u0000\u0004+\u0001\u0000\u0000\u0000\u00060\u0001\u0000\u0000\u0000\b"+
		"5\u0001\u0000\u0000\u0000\n7\u0001\u0000\u0000\u0000\f9\u0001\u0000\u0000"+
		"\u0000\u000e;\u0001\u0000\u0000\u0000\u0010=\u0001\u0000\u0000\u0000\u0012"+
		"?\u0001\u0000\u0000\u0000\u0014B\u0001\u0000\u0000\u0000\u0016J\u0001"+
		"\u0000\u0000\u0000\u0018P\u0001\u0000\u0000\u0000\u001aT\u0001\u0000\u0000"+
		"\u0000\u001cY\u0001\u0000\u0000\u0000\u001e[\u0001\u0000\u0000\u0000 "+
		"]\u0001\u0000\u0000\u0000\"_\u0001\u0000\u0000\u0000$%\u0003\u0002\u0001"+
		"\u0000%\u0001\u0001\u0000\u0000\u0000&)\u0003\u0004\u0002\u0000\')\u0003"+
		"\u0016\u000b\u0000(&\u0001\u0000\u0000\u0000(\'\u0001\u0000\u0000\u0000"+
		")\u0003\u0001\u0000\u0000\u0000*,\u0003\u0006\u0003\u0000+*\u0001\u0000"+
		"\u0000\u0000+,\u0001\u0000\u0000\u0000,-\u0001\u0000\u0000\u0000-.\u0003"+
		"\b\u0004\u0000./\u0003\u0014\n\u0000/\u0005\u0001\u0000\u0000\u000001"+
		"\u0007\u0000\u0000\u00001\u0007\u0001\u0000\u0000\u000026\u0003\n\u0005"+
		"\u000036\u0003\f\u0006\u000046\u0003\u000e\u0007\u000052\u0001\u0000\u0000"+
		"\u000053\u0001\u0000\u0000\u000054\u0001\u0000\u0000\u00006\t\u0001\u0000"+
		"\u0000\u000078\u0007\u0001\u0000\u00008\u000b\u0001\u0000\u0000\u0000"+
		"9:\u0007\u0002\u0000\u0000:\r\u0001\u0000\u0000\u0000;<\u0007\u0003\u0000"+
		"\u0000<\u000f\u0001\u0000\u0000\u0000=>\u0007\u0004\u0000\u0000>\u0011"+
		"\u0001\u0000\u0000\u0000?@\u0007\u0005\u0000\u0000@\u0013\u0001\u0000"+
		"\u0000\u0000AC\u0003\u0010\b\u0000BA\u0001\u0000\u0000\u0000BC\u0001\u0000"+
		"\u0000\u0000CF\u0001\u0000\u0000\u0000DG\u0003\u0012\t\u0000EG\u0005("+
		"\u0000\u0000FD\u0001\u0000\u0000\u0000FE\u0001\u0000\u0000\u0000GH\u0001"+
		"\u0000\u0000\u0000HF\u0001\u0000\u0000\u0000HI\u0001\u0000\u0000\u0000"+
		"I\u0015\u0001\u0000\u0000\u0000JK\u0003\u0018\f\u0000KL\u0003\u001a\r"+
		"\u0000LM\u0003\u001c\u000e\u0000M\u0017\u0001\u0000\u0000\u0000NQ\u0003"+
		"\u0010\b\u0000OQ\u0003\u0012\t\u0000PN\u0001\u0000\u0000\u0000PO\u0001"+
		"\u0000\u0000\u0000PQ\u0001\u0000\u0000\u0000QR\u0001\u0000\u0000\u0000"+
		"RS\u0005(\u0000\u0000S\u0019\u0001\u0000\u0000\u0000TU\u0007\u0006\u0000"+
		"\u0000U\u001b\u0001\u0000\u0000\u0000VZ\u0003\u001e\u000f\u0000WZ\u0003"+
		" \u0010\u0000XZ\u0003\"\u0011\u0000YV\u0001\u0000\u0000\u0000YW\u0001"+
		"\u0000\u0000\u0000YX\u0001\u0000\u0000\u0000Z\u001d\u0001\u0000\u0000"+
		"\u0000[\\\u0007\u0007\u0000\u0000\\\u001f\u0001\u0000\u0000\u0000]^\u0007"+
		"\b\u0000\u0000^!\u0001\u0000\u0000\u0000_`\u0007\t\u0000\u0000`#\u0001"+
		"\u0000\u0000\u0000\b(+5BFHPY";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}