import tkinter as tk
from tkinter import scrolledtext, messagebox
import re

# Keywords, Operators, and Symbols for Lexical Analysis
keywords = {"if", "else", "while", "return", "int", "float", "char", "void"}
operators = {"+", "-", "*", "/", "=", "==", "!=", "<", ">", "<=", ">="}
symbols = {";", "(", ")", "{", "}"}

# Lexical Analyzer Function
def lexical_analysis(code):
    tokens = []
    lines = code.split("\n")

    for line in lines:
        words = re.findall(r'\w+|[^\w\s]', line)  # Tokenizing words and symbols
        for word in words:
            if word in keywords:
                tokens.append((word, "Keyword"))
            elif word in operators:
                tokens.append((word, "Operator"))
            elif word in symbols:
                tokens.append((word, "Symbol"))
            elif word.isdigit():
                tokens.append((word, "Number"))
            elif re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', word):
                tokens.append((word, "Identifier"))
            else:
                tokens.append((word, "Unknown"))

    return tokens

# Syntax Analyzer Function (Displays simple parsing rules)
def syntax_analysis(tokens):
    syntax_rules = []
    for token, token_type in tokens:
        if token_type == "Keyword":
            syntax_rules.append(f"{token} starts a new statement.")
        elif token_type == "Operator":
            syntax_rules.append(f"{token} is used for operation.")
        elif token_type == "Identifier":
            syntax_rules.append(f"{token} is a variable or function name.")
        elif token_type == "Symbol":
            syntax_rules.append(f"{token} is a symbol used in syntax.")
    
    return syntax_rules

# GUI Functions
def analyze_code():
    code = code_input.get("1.0", tk.END).strip()

    if not code:
        messagebox.showerror("Error", "Please enter some code.")
        return

    # Lexical Analysis
    tokens = lexical_analysis(code)
    token_output.delete("1.0", tk.END)
    for token, token_type in tokens:
        token_output.insert(tk.END, f"{token} -> {token_type}\n")



# Creating Tkinter GUI
root = tk.Tk()
root.title("Compiler Visualization Tool")
root.geometry("600x500")

# Code Input Section
tk.Label(root, text="Enter Code:", font=("Arial", 12, "bold")).pack()
code_input = scrolledtext.ScrolledText(root, width=70, height=6)
code_input.pack()

# Analyze Button
analyze_btn = tk.Button(root, text="Analyze Code", font=("Arial", 12, "bold"), command=analyze_code)
analyze_btn.pack(pady=10)

# Lexical Analysis Output
tk.Label(root, text="Tokens:", font=("Arial", 12, "bold")).pack()
token_output = scrolledtext.ScrolledText(root, width=70, height=10)
token_output.pack()



# Run Tkinter Application
root.mainloop()
