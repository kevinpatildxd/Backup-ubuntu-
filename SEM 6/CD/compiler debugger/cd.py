import tkinter as tk
from tkinter import scrolledtext, messagebox
import re

# Token Types
TOKEN_TYPES = {
    "KEYWORD": r"\b(if|else|while|return|int|float|print)\b",
    "IDENTIFIER": r"\b[a-zA-Z_][a-zA-Z0-9_]*\b",
    "NUMBER": r"\b\d+(\.\d+)?\b",
    "OPERATOR": r"[\+\-\*/=<>!]+",
    "PUNCTUATION": r"[(){},;]"
}

# Sample grammar rules 
GRAMMAR_RULES = [
    (r"^int\s+[a-zA-Z_][a-zA-Z0-9_]*\s*=\s*\d+\s*;$", "Variable Declaration"),
    (r"^if\s*\(.*\)\s*{", "If Statement"),
    (r"^while\s*\(.*\)\s*{", "While Loop"),
    (r"^print\s*\(.*\)\s*;$", "Print Statement"),
    (r"^}$", "Closing Brace")  
]


def lexical_analysis(code):
    """ Tokenizes the input code """
    tokens = []
    for token_type, pattern in TOKEN_TYPES.items():
        for match in re.finditer(pattern, code):
            tokens.append((match.group(), token_type))
    return tokens

def syntax_analysis(code_lines):
    """ Checks for syntax errors based on basic rules """
    errors = []
    for i, line in enumerate(code_lines, start=1):
        line = line.strip()
        if not line:
            continue  # Skip empty lines
        if not any(re.match(rule, line) for rule, _ in GRAMMAR_RULES):
            errors.append(f"Syntax Error on Line {i}: {line}")
    return errors

def analyze_code():
    """ Performs lexical and syntax analysis """
    code = input_text.get("1.0", tk.END).strip()
    
    if not code:
        messagebox.showerror("Error", "Please enter some code.")
        return

    # Perform lexical analysis
    tokens = lexical_analysis(code)
    
    # Display tokens
    token_output.delete("1.0", tk.END)
    token_output.insert(tk.END, "Lexical Analysis:\n")
    for token, token_type in tokens:
        token_output.insert(tk.END, f"{token}: {token_type}\n")

    # Perform syntax analysis
    errors = syntax_analysis(code.split("\n"))
    
    # Display syntax results
    syntax_output.delete("1.0", tk.END)
    if errors:
        syntax_output.insert(tk.END, "Syntax Errors:\n")
        for error in errors:
            syntax_output.insert(tk.END, error + "\n")
    else:
        syntax_output.insert(tk.END, "No Syntax Errors Found. ✅")

# Creating Tkinter GUI
root = tk.Tk()
root.title("Compiler Debugger")
root.geometry("800x600")

# Input Section
tk.Label(root, text="Enter Source Code:", font=("Arial", 12, "bold")).pack()
input_text = scrolledtext.ScrolledText(root, width=80, height=10)
input_text.pack()

# Analyze Button
analyze_btn = tk.Button(root, text="Analyze Code", font=("Arial", 12, "bold"), command=analyze_code)
analyze_btn.pack(pady=10)

# Lexical Analysis Output
tk.Label(root, text="Lexical Analysis (Tokens):", font=("Arial", 12, "bold")).pack()
token_output = scrolledtext.ScrolledText(root, width=80, height=8)
token_output.pack()

# Syntax Analysis Output
tk.Label(root, text="Syntax Analysis (Errors):", font=("Arial", 12, "bold")).pack()
syntax_output = scrolledtext.ScrolledText(root, width=80, height=8)
syntax_output.pack()

# Run Tkinter Application
root.mainloop()
