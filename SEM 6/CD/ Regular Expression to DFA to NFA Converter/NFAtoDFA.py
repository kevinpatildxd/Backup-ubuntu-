import tkinter as tk
from tkinter import scrolledtext, messagebox
from collections import deque

class NFAToDFAConverter:
    def __init__(self, master):
        self.master = master
        self.master.title("NFA to DFA Converter")
        self.master.geometry("800x600")

        # Labels and Input
        tk.Label(master, text="Enter NFA Transitions (State, Input -> Next State(s)):", font=("Arial", 12, "bold")).pack()
        self.input_text = scrolledtext.ScrolledText(master, width=80, height=10)
        self.input_text.pack()

        # Convert Button
        self.convert_btn = tk.Button(master, text="Convert to DFA", font=("Arial", 12, "bold"), command=self.convert_to_dfa)
        self.convert_btn.pack(pady=10)

        # Output Section
        tk.Label(master, text="DFA Transitions:", font=("Arial", 12, "bold")).pack()
        self.output_text = scrolledtext.ScrolledText(master, width=80, height=8)
        self.output_text.pack()

        self.nfa_transitions = {}
        self.dfa_transitions = {}

    def parse_nfa(self, nfa_input):
        """ Parses user input to extract NFA transitions. """
        transitions = {}
        for line in nfa_input.strip().split("\n"):
            parts = line.split("->")
            if len(parts) != 2:
                continue
            state_input = parts[0].strip().split(",")
            next_states = parts[1].strip().split(",")

            if len(state_input) != 2:
                continue
            state, symbol = state_input[0].strip(), state_input[1].strip()
            
            if state not in transitions:
                transitions[state] = {}
            if symbol not in transitions[state]:
                transitions[state][symbol] = set()
            transitions[state][symbol].update(next_states)
        return transitions

    def convert_to_dfa(self):
        """ Converts NFA transitions into DFA format. """
        nfa_input = self.input_text.get("1.0", tk.END).strip()
        if not nfa_input:
            messagebox.showerror("Error", "Please enter NFA transitions.")
            return

        self.nfa_transitions = self.parse_nfa(nfa_input)
        self.dfa_transitions = {}

        start_state = "A"  # Assume starting state is 'A'
        queue = deque([frozenset([start_state])])
        state_mapping = {frozenset([start_state]): "A"}

        while queue:
            current_set = queue.popleft()
            dfa_state = state_mapping[current_set]
            self.dfa_transitions[dfa_state] = {}

            for symbol in {symbol for state in current_set if state in self.nfa_transitions for symbol in self.nfa_transitions[state]}:
                next_states = set()
                for state in current_set:
                    if state in self.nfa_transitions and symbol in self.nfa_transitions[state]:
                        next_states.update(self.nfa_transitions[state][symbol])
                if next_states:
                    next_frozen = frozenset(next_states)
                    if next_frozen not in state_mapping:
                        state_mapping[next_frozen] = chr(65 + len(state_mapping))  # Assign letters A, B, C...
                        queue.append(next_frozen)
                    self.dfa_transitions[dfa_state][symbol] = state_mapping[next_frozen]

        # Display DFA Transitions
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, "DFA Transitions:\n")
        for state, trans in self.dfa_transitions.items():
            for symbol, next_state in trans.items():
                self.output_text.insert(tk.END, f"{state}, {symbol} -> {next_state}\n")

# Run Application
root = tk.Tk()
app = NFAToDFAConverter(root)
root.mainloop()













#input
# A, 0 -> A, B
# A, 1 -> A
# B, 0 -> C
# B, 1 -> C
# C, 0 -> C
# C, 1 -> A
