import tkinter as tk
from tkinter import messagebox
import re

class IntermediateCodeGenerator:
    def __init__(self):
        self.temp_count = 1
        self.code = []

    def generate_code(self, expression):
        self.temp_count = 1
        self.code = []
        
        # Remove spaces and check for a valid assignment expression
        expression = expression.replace(" ", "")
        match = re.match(r'([a-zA-Z]\w*)=([\w+\-*/()]+);?', expression)

        if not match:
            return ["Error: Invalid syntax! Please use: a = b + c * 5;"]

        var_name, expr = match.groups()
        
        # Convert infix to postfix (handling operator precedence)
        postfix_expr = self.infix_to_postfix(expr)

        if "Error" in postfix_expr:
            return [postfix_expr]  # If there's an error, return it

        # Generate three-address code (TAC)
        self._generate_tac(var_name, postfix_expr)
        return self.code

    def infix_to_postfix(self, expr):
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        output = []
        stack = []
        tokens = re.findall(r'[a-zA-Z]\w*|\d+|[+\-*/()]', expr)

        for token in tokens:
            if token.isalnum():  # Operand (variable or number)
                output.append(token)
            elif token in precedence:  # Operator
                while stack and stack[-1] != '(' and precedence[stack[-1]] >= precedence[token]:
                    output.append(stack.pop())
                stack.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                if not stack or stack[-1] != '(':
                    return "Error: Mismatched parentheses!"
                stack.pop()

        while stack:
            if stack[-1] == '(':
                return "Error: Mismatched parentheses!"
            output.append(stack.pop())

        return output

    def _generate_tac(self, var_name, postfix_expr):
        stack = []
        
        for token in postfix_expr:
            if token.isalnum():  # Operand
                stack.append(token)
            else:  # Operator
                if len(stack) < 2:
                    self.code.append("Error: Invalid Expression!")
                    return
                op2 = stack.pop()
                op1 = stack.pop()
                temp_var = f"T{self.temp_count}"
                self.temp_count += 1
                self.code.append(f"{temp_var} = {op1} {token} {op2}")
                stack.append(temp_var)

        if stack:
            self.code.append(f"{var_name} = {stack.pop()}")

class ICGApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Intermediate Code Generator")
        self.root.geometry("500x400")

        self.label = tk.Label(root, text="Enter Expression:", font=("Arial", 12))
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, width=40, font=("Arial", 12))
        self.entry.pack(pady=5)

        self.generate_button = tk.Button(root, text="Generate Code", command=self.generate_code, font=("Arial", 12))
        self.generate_button.pack(pady=10)

        self.result_label = tk.Label(root, text="Intermediate Code:", font=("Arial", 12))
        self.result_label.pack(pady=10)

        self.result_text = tk.Text(root, height=8, width=50, font=("Arial", 12))
        self.result_text.pack(pady=5)

    def generate_code(self):
        expression = self.entry.get().strip()
        if not expression:
            messagebox.showerror("Error", "Please enter an expression!")
            return

        icg = IntermediateCodeGenerator()
        intermediate_code = icg.generate_code(expression)

        self.result_text.delete(1.0, tk.END)
        for line in intermediate_code:
            self.result_text.insert(tk.END, line + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = ICGApp(root)
    root.mainloop()
