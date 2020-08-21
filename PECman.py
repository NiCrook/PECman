import tkinter as tk
from tkinter import IntVar

"""
A gui that has the user input their number of outs and the likelihood they believe their villian to fold and calculates
their equity, fold equity, and total equity.
"""


class EquityWindow:
    def __init__(self, master):
        # define window
        self.master = master
        master.title('Poker Equity Calculator V1.2')
        self.frame = tk.Frame(self.master)
        self.frame.grid()

        # VARIABLES
        # predefine variables for future use
        self.entered_outs = 0
        self.entered_folds = 0
        self.natural_equity = 0
        self.fold_equity = 0
        self.total_equity = 0

        # set variables to integer types and set their values
        self.entered_outs_text = IntVar()
        self.entered_folds_text = IntVar()
        self.natural_equity_text = IntVar()
        self.fold_equity_text = IntVar()
        self.total_equity_text = IntVar()

        self.entered_outs_text.set(self.entered_outs)
        self.entered_folds_text.set(self.entered_folds)
        self.natural_equity_text.set(self.natural_equity)
        self.fold_equity_text.set(self.fold_equity)
        self.total_equity_text.set(self.total_equity)

        # define validate command variables
        self.vcmd1 = self.master.register(self.validate1)
        self.vcmd2 = self.master.register(self.validate2)

        # WIDGETS
        self.labels = {
            'outs_question': tk.Label(self.frame, text='How many outs do you have?'),
            'outs_text': tk.Label(self.frame, text='Outs: '),
            'entered_outs': tk.Label(self.frame, textvariable=self.entered_outs_text),
            'equity_text': tk.Label(self.frame, text='Equity: '),
            'equity_percent': tk.Label(self.frame, textvariable=self.natural_equity_text),
            'fold_question': tk.Label(self.frame, text='How likely are they to fold?'),
            'F%_text': tk.Label(self.frame, text='F%: '),
            'entered_folds': tk.Label(self.frame, textvariable=self.entered_folds_text),
            'fold_equity_text': tk.Label(self.frame, text='FE: '),
            'fold_equity': tk.Label(self.frame, textvariable=self.fold_equity_text),
            'total_equity_text': tk.Label(self.frame, text='Total: '),
            'total_equity': tk.Label(self.frame, textvariable=self.total_equity_text)
        }

        self.entries = {
            'outs_entry': tk.Entry(self.frame, validate='key', validatecommand=(self.vcmd1, '%P')),
            'folds_entry': tk.Entry(self.frame, validate='key', validatecommand=(self.vcmd2, '%P'))
        }

        self.buttons = {
            'flop_button': tk.Button(self.frame, text='Flop', command=lambda: self.button_push('flop')),
            'turn_button': tk.Button(self.frame, text='Turn', command=lambda: self.button_push('turn')),
            'calculate_button': tk.Button(self.frame, text='Calculate', command=lambda: self.button_push('calculate'))
        }

        # LAYOUT
        self.labels['outs_question'].grid(row=0, column=0, columnspan=4)
        self.labels['outs_text'].grid(row=0, column=4, sticky=tk.W)
        self.labels['entered_outs'].grid(row=0, column=5, sticky=tk.E)
        self.entries['outs_entry'].grid(row=1, column=0, columnspan=4, sticky=tk.W + tk.E)
        self.buttons['flop_button'].grid(row=2, column=0, columnspan=2, sticky=tk.W)
        self.buttons['turn_button'].grid(row=2, column=2, columnspan=2, sticky=tk.E)
        self.labels['equity_text'].grid(row=2, column=4, sticky=tk.W)
        self.labels['equity_percent'].grid(row=2, column=5, sticky=tk.E)

    # METHODS
    def validate1(self, new_char):
        if not new_char:
            self.entered_outs = 0
            return True

        try:
            self.entered_outs = int(new_char)
            return True
        except ValueError:
            return False

    def validate2(self, new_char):
        if not new_char:
            self.entered_folds = 0
            return True

        try:
            self.entered_folds = int(new_char)
            return True
        except ValueError:
            return False

    def button_push(self, method):
        if method == "flop":
            self.natural_equity = str(round(((self.entered_outs / 47) + (self.entered_outs / 46)) * 100))
            self.labels['fold_question'].grid(row=3, column=0, columnspan=4, sticky=tk.W)
            self.labels['F%_text'].grid(row=3, column=4, sticky=tk.W)
            self.labels['entered_folds'].grid(row=3, column=5, sticky=tk.E)
            self.entries['folds_entry'].grid(row=4, column=0, columnspan=4, sticky=tk.W + tk.E)
            self.labels['fold_equity_text'].grid(row=4, column=4, sticky=tk.W)
            self.labels['fold_equity'].grid(row=4, column=5, sticky=tk.E)
            self.buttons['calculate_button'].grid(row=5, column=0, sticky=tk.W)
        elif method == "turn":
            self.natural_equity = str(round((self.entered_outs / 46) * 100))
            self.labels['fold_question'].grid(row=3, column=0, columnspan=4, sticky=tk.W)
            self.labels['F%_text'].grid(row=3, column=4, sticky=tk.W)
            self.labels['entered_folds'].grid(row=3, column=5, sticky=tk.E)
            self.entries['folds_entry'].grid(row=4, column=0, columnspan=4, sticky=tk.W + tk.E)
            self.labels['fold_equity_text'].grid(row=4, column=4, sticky=tk.W)
            self.labels['fold_equity'].grid(row=4, column=5, sticky=tk.E)
            self.buttons['calculate_button'].grid(row=5, column=0, sticky=tk.W)
        elif method == 'calculate':
            equity_gain = 100 - int(self.natural_equity)
            self.fold_equity = round((((self.entered_folds / 100) * (equity_gain / 100)) * 100), 2)
            self.total_equity = round((int(self.natural_equity) + self.fold_equity), 2)
            self.labels['total_equity_text'].grid(row=5, column=4, sticky=tk.W)
            self.labels['total_equity'].grid(row=5, column=5, sticky=tk.E)
        else:
            self.entered_outs = 0
            self.entered_folds = 0
            self.natural_equity = 0
            self.fold_equity = 0
            self.total_equity = 0

        self.entered_outs_text.set(self.entered_outs)
        self.entered_folds_text.set(self.entered_folds)
        self.natural_equity_text.set(self.natural_equity)
        self.fold_equity_text.set(self.fold_equity)
        self.total_equity_text.set(self.total_equity)


def main():
    root = tk.Tk()
    PEC_gui = EquityWindow(root)
    root.mainloop()


if __name__ == '__main__':
    main()
