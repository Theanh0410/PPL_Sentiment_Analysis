from CompiledFiles.SentimentLexer import SentimentLexer
from CompiledFiles.SentimentParser import SentimentParser
import sys, os
import subprocess
import unittest
from antlr4 import *
import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Define your variables
DIR = os.path.dirname(__file__)
ANTLR_JAR = 'C:/antlr/antlr4-4.9.2-complete.jar' #Remember to change it according to ur computer
CPL_Dest = 'CompiledFiles'
SRC = 'Sentiment.g4'
TESTS = os.path.join(DIR, './tests')


def printUsage():
    print('python run.py gen')
    print('python run.py test')
    print('python run.py chat')    


def printBreak():
    print('-----------------------------------------------')


def generateAntlr2Python():
    print('Antlr4 is running...')
    subprocess.run(['java', '-jar', ANTLR_JAR, '-o', CPL_Dest, '-no-listener', '-Dlanguage=Python3', SRC])
    print('Generate successfully')

def runTest():
    print('Running testcases...')
    
    from CompiledFiles.SentimentLexer import SentimentLexer
    from CompiledFiles.SentimentParser import SentimentParser
    from antlr4.error.ErrorListener import ErrorListener

    class CustomErrorListener(ErrorListener):
        def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
            print(f"Input rejected: {msg}")
            exit(1)  # Exit the program with an error
    filename = '001.txt'
    inputFile = os.path.join(DIR, './tests', filename)    

    print('List of token: ')
    lexer = SentimentLexer(FileStream(inputFile))        
    tokens = []
    token = lexer.nextToken()
    while token.type != Token.EOF:
        tokens.append(token.text)
        token = lexer.nextToken()
    tokens.append('<EOF>')
    print(','.join(tokens))    

    # test
    input_stream = FileStream(inputFile)
    lexer = SentimentLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SentimentParser(stream)
    tree = parser.program()  # Start parsing at the `program` rule

    # Print the parse tree (for debugging)
    print(tree.toStringTree(recog=parser))
    # end of test

    
    # Reset the input stream for parsing and catch the error
    lexer = SentimentLexer(FileStream(inputFile))
    token_stream = CommonTokenStream(lexer)

    parser = SentimentParser(token_stream)   
    parser.removeErrorListeners()
    parser.addErrorListener(CustomErrorListener())    
    try:
        parser.program()
        print("Input accepted")
    except SystemExit:        
        pass
    
    printBreak()
    print('Run tests completely')

#v----------------------------------------------------------------------------------------------------------------------------------------------

try:
    stopwords.words('english')
except LookupError:
    nltk.download('stopwords')


try:
    word_tokenize("test")
except LookupError:
    nltk.download('punkt_tab')


def tokenize():
    def inner(text):
        return word_tokenize(text.lower())
    return inner


def remove_punctuation():
    def inner(words):
        return [w for w in words if w not in string.punctuation]
    return inner


def remove_stopwords(stopwords_set):
    def inner(words):
        return [w for w in words if w not in stopwords_set]
    return inner


def clean_text(stopwords_set):
    return lambda text: remove_stopwords(stopwords_set)(remove_punctuation()(tokenize()(text)))

pos_v = {"happy", "funny", "love", "awesome", "execellent", "great", "fantastic"}
neg_v = {"bad", "sad", "terrible", "awful",  "hate", "poor", "worst", "angry"}
stopwords_set = set(stopwords.words("english"))

def Sentiment(text,pos_v,neg_v,stopwords_set):
    cleaner = clean_text(stopwords_set=stopwords_set)

    try:
        words = cleaner(text)
        positive_score = sum(1 for w in words if w in pos_v)
        negative_score = sum(1 for w in words if w in neg_v)
        
        if positive_score > negative_score:
            return "positive"
        elif negative_score > positive_score:
            return "negative"
        else:
            return "neutral"
    except Exception as e:
        return f"Error parsing input: {e}"
    
def chat(self):
        while True:
            user_input = input("Input: ")
            sentiment = self.sentiment(user_input,pos_v,neg_v,stopwords_set)
            print("AI: that feel", sentiment)
    
#^----------------------------------------------------------------------------------------------------------------------------------------------

def main(argv):
    print('Complete jar file ANTLR  :  ' + str(ANTLR_JAR))
    print('Length of arguments      :  ' + str(len(argv)))    
    printBreak()

    if len(argv) < 1:
        printUsage()
    elif argv[0] == 'gen':
        generateAntlr2Python()    
    elif argv[0] == 'test':       
        runTest()
    elif argv[0] == 'chat':
        bot = Sentiment()
        bot.chat()
    else:
        printUsage()


if __name__ == '__main__':
    main(sys.argv[1:])     
    
