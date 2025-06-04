import sys, os
import subprocess
import unittest
from antlr4 import *
from TextCleaner import clean_text

# Define your variables
DIR = os.path.dirname(__file__)
ANTLR_JAR = 'C:/antlr/antlr4-4.9.2-complete.jar' # your location is going here
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
    subprocess.run(['java', '-jar', ANTLR_JAR, '-o', CPL_Dest, '-no-listener', '-visitor', '-Dlanguage=Python3', SRC])    
    print('Generate successfully')

def runCode(astTree):    
    from CodeRunner import CodeRunner
    code_runner = CodeRunner()
    result = astTree.accept(code_runner)
    
    print("Result:", result)


def runTest():
    print('Running testcases...')
       
    from CompiledFiles.SentimentLexer import SentimentLexer
    from CompiledFiles.SentimentParser import SentimentParser
    from antlr4.error.ErrorListener import ErrorListener

    class CustomErrorListener(ErrorListener):
        def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
            print(f"Input rejected: {msg}")
            exit(1)  # Exit the program with an error

    filename = 'testcase.txt'
    inputFile = os.path.join(DIR, './tests', filename)        

    with open(inputFile, 'r', encoding='utf-8') as f:
        raw_text = f.read()
    cleaned_tokens = clean_text(raw_text)
    print("Cleaned tokens:", cleaned_tokens)

    # Parse the cleaned text instead of the raw file
    input_stream = InputStream(" ".join(cleaned_tokens))
    lexer = SentimentLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SentimentParser(stream)   
    parser.removeErrorListeners()
    parser.addErrorListener(CustomErrorListener())    

    try:
        tree = parser.program()
        print("Input accepted")
    except SystemExit:        
        return

    printBreak()
    print('Run tests completely')

    from ASTGeneration import ASTGeneration
    ast_generator = ASTGeneration()
    asttree = tree.accept(ast_generator)
    print('This is ast string: ', asttree)

    runCode(asttree)

class Sentiment:
    def sentiment(self, text):
        from CompiledFiles.SentimentLexer import SentimentLexer
        from CompiledFiles.SentimentParser import SentimentParser
        from ASTGeneration import ASTGeneration
        from CodeRunner import CodeRunner
        from TextCleaner import clean_text

        # Clean and prepare text
        cleaned_tokens = clean_text(text)
        input_stream = InputStream(" ".join(cleaned_tokens))

        # ANTLR parsing
        lexer = SentimentLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = SentimentParser(token_stream)

        try:
            tree = parser.program()
            ast = tree.accept(ASTGeneration())
            result = ast.accept(CodeRunner())
            return result.get("sentiment", "unknown")
        except Exception as e:
            return f"Error parsing input: {e}"

    def chat(self):
        print("Enter a sentence (or type 'exit' to quit):")
        while True:
            user_input = input("Input: ")
            if user_input.lower() in ['exit', 'quit']:
                print("Goodbye!")
                break
            sentiment = self.sentiment(user_input)
            print("AI: that feels", sentiment)


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

    
    
    