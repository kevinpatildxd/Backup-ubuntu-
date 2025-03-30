import tkinter as tk
from tkinter import messagebox
import re

# Define keywords, operators, and symbols
KEYWORDS = {"if", "else", "while", "return", "int", "float", "char", "for", "void"}
OPERATORS = {"+", "-", "*", "/", "=", "==", "!=", ">=", "<=", "&&", "||"}
SYMBOLS = {"(", ")", "{", "}", "[", "]", ";", ","}

def is_identifier(token):
    """Check if token is a valid identifier (variable name)"""
    return re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', token) and token not in KEYWORDS

def is_number(token):
    """Check if token is a number (integer or float)"""
    return re.match(r'^\d+(\.\d+)?$', token)

def analyze_lexical(input_code):
    """Perform lexical analysis on the input code"""
    tokens = re.findall(r'[a-zA-Z_]\w*|\d+\.\d+|\d+|==|!=|>=|<=|&&|\|\||[+\-*/=;(){}[\],]', input_code)
    
    result = []
    for token in tokens:
        if token in KEYWORDS:
            result.append(f"KEYWORD      ➝ {token}")
        elif token in OPERATORS:
            result.append(f"OPERATOR     ➝ {token}")
        elif token in SYMBOLS:
            result.append(f"SYMBOL       ➝ {token}")
        elif is_number(token):
            result.append(f"NUMBER       ➝ {token}")
        elif is_identifier(token):
            result.append(f"IDENTIFIER   ➝ {token}")
        else:
            result.append(f"ERROR        ➝ {token} (Unrecognized token)")
    
    return result

class LexicalAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lexical Analyzer")
        self.root.geometry("500x400")

        # Label
        self.label = tk.Label(root, text="Enter Code:", font=("Arial", 12))
        self.label.pack(pady=10)

        # Text Entry for Code
        self.code_input = tk.Text(root, height=5, width=50, font=("Arial", 12))
        self.code_input.pack(pady=5)

        # Analyze Button
        self.analyze_button = tk.Button(root, text="Analyze", command=self.analyze, font=("Arial", 12))
        self.analyze_button.pack(pady=10)

        # Result Label
        self.result_label = tk.Label(root, text="Tokens:", font=("Arial", 12))
        self.result_label.pack(pady=10)

        # Result Display
        self.result_text = tk.Text(root, height=10, width=50, font=("Arial", 12))
        self.result_text.pack(pady=5)

    def analyze(self):
        """Trigger lexical analysis and display results"""
        input_code = self.code_input.get("1.0", tk.END).strip()
        if not input_code:
            messagebox.showerror("Error", "Please enter some code!")
            return

        tokens = analyze_lexical(input_code)

        self.result_text.delete(1.0, tk.END)
        for token in tokens:
            self.result_text.insert(tk.END, token + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = LexicalAnalyzerApp(root)
    root.mainloop()
