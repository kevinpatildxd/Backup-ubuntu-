import tkinter as tk
from tkinter import messagebox
import re

class ParserSimulator:
    def __init__(self, expression):
        self.tokens = re.findall(r'[a-zA-Z]\w*|\d+|[+\-*/=();]', expression)
        self.current_token_index = 0
        self.current_token = self.tokens[self.current_token_index] if self.tokens else None

    def advance(self):
        """Move to the next token"""
        self.current_token_index += 1
        if self.current_token_index < len(self.tokens):
            self.current_token = self.tokens[self.current_token_index]
        else:
            self.current_token = None

    def match(self, expected_token):
        """Match current token with expected token"""
        if self.current_token == expected_token:
            self.advance()
        else:
            raise SyntaxError(f"Expected '{expected_token}' but found '{self.current_token}'")

    def parse(self):
        """Start parsing by calling the assignment function"""
        try:
            self.assignment()
            if self.current_token is not None:
                raise SyntaxError(f"Unexpected token '{self.current_token}' at the end")
            return "Parsing successful! No syntax errors."
        except SyntaxError as e:
            return f"Syntax Error: {e}"

    def assignment(self):
        """Parse assignment statements: `a = expr;`"""
        if re.match(r'^[a-zA-Z]\w*$', self.current_token):  # Variable name
            self.advance()
            self.match("=")
            self.expr()
            self.match(";")
        else:
            raise SyntaxError(f"Invalid assignment statement starting with '{self.current_token}'")

    def expr(self):
        """Parse expressions with `+` and `-`"""
        self.term()
        while self.current_token in ("+", "-"):
            self.advance()
            self.term()

    def term(self):
        """Parse terms with `*` and `/`"""
        self.factor()
        while self.current_token in ("*", "/"):
            self.advance()
            self.factor()

    def factor(self):
        """Parse numbers, variables, and parentheses"""
        if re.match(r'^[a-zA-Z]\w*$', self.current_token) or re.match(r'^\d+$', self.current_token):  # Variable or number
            self.advance()
        elif self.current_token == "(":
            self.advance()
            self.expr()
            self.match(")")
        else:
            raise SyntaxError(f"Unexpected token '{self.current_token}'")

class ParserGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Parser Simulator")
        self.root.geometry("500x400")

        self.label = tk.Label(root, text="Enter Expression:", font=("Arial", 12))
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, width=40, font=("Arial", 12))
        self.entry.pack(pady=5)

        self.parse_button = tk.Button(root, text="Parse Expression", command=self.parse_expression, font=("Arial", 12))
        self.parse_button.pack(pady=10)

        self.result_label = tk.Label(root, text="Parsing Result:", font=("Arial", 12))
        self.result_label.pack(pady=10)

        self.result_text = tk.Text(root, height=8, width=50, font=("Arial", 12))
        self.result_text.pack(pady=5)

    def parse_expression(self):
        expression = self.entry.get().strip()
        if not expression:
            messagebox.showerror("Error", "Please enter an expression!")
            return

        parser = ParserSimulator(expression)
        result = parser.parse()

        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = ParserGUI(root)
    root.mainloop()
