import re

# 1. LEXICAL ANALYZER (TOKENIZER)
class Lexer:
    def __init__(self, code):
        self.code = code
        self.tokens = []
        self.tokenize()

    def tokenize(self):
        token_specification = [
            ('NUMBER', r'\d+'), ('ASSIGN', r'='), ('END', r';'),
            ('ID', r'[a-zA-Z_]\w*'), ('OP', r'[+\-*/]'),
            ('IF', r'if'), ('WHILE', r'while'), ('PRINT', r'print'),
            ('LPAREN', r'\('), ('RPAREN', r'\)'), 
            ('LBRACE', r'\{'), ('RBRACE', r'\}'), 
            ('WHITESPACE', r'\s+')
        ]
        tok_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)
        for match in re.finditer(tok_regex, self.code):
            kind = match.lastgroup
            value = match.group()
            if kind != 'WHITESPACE':  # Ignore spaces
                self.tokens.append((kind, value))

# 2. SYNTAX ANALYZER (PARSER)
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def match(self, expected_type):
        if self.pos < len(self.tokens) and self.tokens[self.pos][0] == expected_type:
            self.pos += 1
            return True
        return False

    def parse_statement(self):
        if self.match('ID') and self.match('ASSIGN'):
            return self.parse_expression()
        elif self.match('IF'):
            return self.parse_if()
        elif self.match('WHILE'):
            return self.parse_while()
        elif self.match('PRINT'):
            return self.parse_print()
        return False

    def parse_expression(self):
        if self.match('NUMBER') or self.match('ID'):
            while self.match('OP'):
                if not self.match('NUMBER') and not self.match('ID'):
                    return False
            return self.match('END')
        return False

    def parse_if(self):
        return self.match('LPAREN') and self.match('ID') and self.match('OP') and self.match('NUMBER') and self.match('RPAREN') and self.match('LBRACE') and self.match('RBRACE')

    def parse_while(self):
        return self.match('LPAREN') and self.match('ID') and self.match('OP') and self.match('NUMBER') and self.match('RPAREN') and self.match('LBRACE') and self.match('RBRACE')

    def parse_print(self):
        return self.match('LPAREN') and self.match('ID') and self.match('RPAREN') and self.match('END')

    def parse(self):
        while self.pos < len(self.tokens):
            if not self.parse_statement():
                return False
        return True

# 3. INTERMEDIATE CODE GENERATOR
class IntermediateCodeGenerator:
    def __init__(self):
        self.code = []

    def generate(self, tokens):
        for token in tokens:
            if token[0] == 'ID':
                self.code.append(f'LOAD {token[1]}')
            elif token[0] == 'NUMBER':
                self.code.append(f'PUSH {token[1]}')
            elif token[0] == 'OP':
                self.code.append(f'OP {token[1]}')
        return self.code

# 4. EXECUTOR (INTERPRETER)
class Executor:
    def __init__(self, intermediate_code):
        self.variables = {}
        self.execute(intermediate_code)

    def execute(self, code):
        for instruction in code:
            parts = instruction.split()
            if parts[0] == 'PUSH':
                self.variables['temp'] = int(parts[1])
            elif parts[0] == 'LOAD':
                self.variables['temp'] = self.variables.get(parts[1], 0)
            elif parts[0] == 'STORE':
                self.variables[parts[1]] = self.variables['temp']
            elif parts[0] == 'OP':
                if parts[1] == '+':
                    self.variables['temp'] += self.variables['temp']
            elif parts[0] == 'PRINT':
                print(self.variables[parts[1]])

# MAIN FUNCTION TO RUN THE COMPILER
def main():
    # Sample input code
    code = """
    a = 5;
    b = a + 10;
    if (b > 5) { print(b); }
    """
    
    # Step 1: Lexical Analysis
    lexer = Lexer(code)
    tokens = lexer.tokens
    print("Tokens:", tokens)

    # Step 2: Syntax Analysis
    parser = Parser(tokens)
    if not parser.parse():
        print("Syntax Error!")
        return
    
    # Step 3: Intermediate Code Generation
    icg = IntermediateCodeGenerator()
    intermediate_code = icg.generate(tokens)
    print("\nGenerated Intermediate Code:")
    for line in intermediate_code:
        print(line)

    # Step 4: Execution
    executor = Executor(intermediate_code)

if __name__ == "__main__":
    main()
