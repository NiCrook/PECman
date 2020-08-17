import tkinter as tk
from tkinter import IntVar

"""
Creates frame which asks the user to input their number of outs. Once the user enters their number of outs
and clicks either the "flop" or "turn" button, they will find their equity percentage displayed along with
the number of outs they entered.
"""


class EquityWindow(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        master.title("Poker Equity Calculator v1.01")

        # placeholders to define for future use
        self.entered_outs = 0
        self.entered_folds = 0
        self.natural_equity = 0
        self.fold_equity = 0
        self.total_equity = 0

        # first row widgets
        self.outs_question_label = tk.Label(self.master, text="How many outs do you have?")
        self.outs_label = tk.Label(self.master, text="Outs: ")
        self.entered_outs_text = IntVar()
        self.entered_outs_text.set(self.entered_outs)
        self.entered_outs_label = tk.Label(self.master, textvariable=self.entered_outs_text)

        # second row widgets
        self.vcmd = self.master.register(self.validate)
        self.outs_entry = tk.Entry(self.master, validate="key", validatecommand=(self.vcmd, '%P'))
        self.equity_label = tk.Label(self.master, text="Equity: ")
        self.natural_equity_label_text = IntVar()
        self.natural_equity_label_text.set(self.natural_equity)
        self.equity_percent_label = tk.Label(self.master, textvariable=self.natural_equity_label_text)

        # third row widgets
        self.flop_button = tk.Button(self.master, text='flop', command=lambda: self.update("flop"))
        self.turn_button = tk.Button(self.master, text='turn', command=lambda: self.update("turn"))

        # layout
        self.outs_question_label.grid(row=0, column=0, columnspan=2)
        self.outs_label.grid(row=0, column=2)
        self.entered_outs_label.grid(row=0, column=3)
        self.outs_entry.grid(row=1, column=0, columnspan=2, sticky=tk.W + tk.E)
        self.equity_label.grid(row=1, column=2)
        self.equity_percent_label.grid(row=1, column=3)
        self.flop_button.grid(row=2, column=0, sticky=tk.W)
        self.turn_button.grid(row=2, column=0)

    # for entry field use
    def validate(self, new_text):
        if not new_text:
            self.entered_outs = 0
            return True

        try:
            self.entered_outs = int(new_text)
            return True
        except ValueError:
            return False

    # for button execution
    def update(self, method):
        if method == "flop":
            self.natural_equity = str(round(((self.entered_outs / 47) + (self.entered_outs / 46)) * 100))
        elif method == "turn":
            self.natural_equity = str(round((self.entered_outs / 46) * 100))
        else:
            self.natural_equity = 0

        self.entered_outs_text.set(self.entered_outs)
        self.natural_equity_label_text.set(str(self.natural_equity) + '%')
        self.outs_entry.delete(0, tk.END)


if __name__ == '__main__':
    root = tk.Tk()
    pec_gui = EquityWindow(root)
    root.mainloop()
