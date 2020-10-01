# imports
import tkinter as tk
from tkinter import IntVar
from tkinter import StringVar
import random


# CONTAINER FRAME TO HOLD OTHER FRAMES
class ContainerFrame(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # define container frame
        container = tk.Frame(self)
        self.title("Poker Equity Calculator v1.22")
        # define container frame size and layout
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # define frame list as list of frame names
        frame_list = [StartFrame, EquityFrame, RNGFrame]
        self.frames = {}

        # create each frame in frame_list
        for F in frame_list:
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # start with selected frame
        self.show_frame("StartFrame")

    # def show_frame(self, page_name):
    #     frame = self.frames[page_name]
    #     frame.tkraise()

    # method to raise a selected frame
    def show_frame(self, page_name):
        for frame in self.frames.values():
            frame.grid_remove()
            frame = self.frames[page_name]
            frame.grid()


# SPLASH FRAME
class StartFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # LABELS
        self.start_splash_text = tk.Label(self, text="PECman v2")

        # BUTTONS
        self.pec_button = tk.Button(self, text="PEC", command=lambda: controller.show_frame("EquityFrame"))
        self.rng_button = tk.Button(self, text="RNG", command=lambda: controller.show_frame("RNGFrame"))

        # LAYOUT
        self.widgets()

    def widgets(self):
        self.start_splash_text.grid(row=0, column=0)
        self.pec_button.grid(row=1, column=0)
        self.rng_button.grid(row=1, column=1)


# EQUITY CALCULATOR FRAME
class EquityFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # VARIABLES
        # predefine variables for future use
        self.entered_outs = 0
        self.entered_folds = 0
        self.natural_equity = 0
        self.fold_equity = 0
        self.total_equity = 0

        # set variables to integer types and set contents
        self.entered_outs_text = IntVar()
        self.entered_folds_text = IntVar()
        self.natural_equity_text = IntVar()
        self.fold_equity_text = IntVar()
        self.total_equity_text = IntVar()

        # create variables of different object type than set values
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
            'outs_question': tk.Label(self, text='How many outs do you have?'),
            'outs_text': tk.Label(self, text='Outs: '),
            'entered_outs': tk.Label(self, textvariable=self.entered_outs_text),
            'equity_text': tk.Label(self, text='Equity: '),
            'equity_percent': tk.Label(self, textvariable=self.natural_equity_text),
            'fold_question': tk.Label(self, text='How likely are they to fold?'),
            'F%_text': tk.Label(self, text='F%: '),
            'entered_folds': tk.Label(self, textvariable=self.entered_folds_text),
            'fold_equity_text': tk.Label(self, text='FE: '),
            'fold_equity': tk.Label(self, textvariable=self.fold_equity_text),
            'total_equity_text': tk.Label(self, text='Total: '),
            'total_equity': tk.Label(self, textvariable=self.total_equity_text)
        }

        self.entries = {
            'outs_entry': tk.Entry(self, validate='key', validatecommand=(self.vcmd1, '%P')),
            'folds_entry': tk.Entry(self, validate='key', validatecommand=(self.vcmd2, '%P'))
        }

        self.buttons = {
            'flop_button': tk.Button(self, text='Flop', command=lambda: self.button_push('flop')),
            'turn_button': tk.Button(self, text='Turn', command=lambda: self.button_push('turn')),
            'calculate_button': tk.Button(self, text='Calculate', command=lambda: self.button_push('calculate')),
            'back_button': tk.Button(self, text='Back', command=lambda: self.button_push('back'))
        }

        self.widgets()
        self.widget_layout()

    # WIDGETS
    def widgets(self):
        self.labels = {
            'outs_question': tk.Label(self, text='How many outs do you have?'),
            'outs_text': tk.Label(self, text='Outs: '),
            'entered_outs': tk.Label(self, textvariable=self.entered_outs_text),
            'equity_text': tk.Label(self, text='Equity: '),
            'equity_percent': tk.Label(self, textvariable=self.natural_equity_text),
            'fold_question': tk.Label(self, text='How likely are they to fold?'),
            'F%_text': tk.Label(self, text='F%: '),
            'entered_folds': tk.Label(self, textvariable=self.entered_folds_text),
            'fold_equity_text': tk.Label(self, text='FE: '),
            'fold_equity': tk.Label(self, textvariable=self.fold_equity_text),
            'total_equity_text': tk.Label(self, text='Total: '),
            'total_equity': tk.Label(self, textvariable=self.total_equity_text)
        }

        self.entries = {
            'outs_entry': tk.Entry(self, validate='key', validatecommand=(self.vcmd1, '%P')),
            'folds_entry': tk.Entry(self, validate='key', validatecommand=(self.vcmd2, '%P'))
        }

        self.buttons = {
            'flop_button': tk.Button(self, text='Flop', command=lambda: self.button_push('flop')),
            'turn_button': tk.Button(self, text='Turn', command=lambda: self.button_push('turn')),
            'calculate_button': tk.Button(self, text='Calculate', command=lambda: self.button_push('calculate')),
            'back_button': tk.Button(self, text='Back', command=lambda: self.button_push('back'))
        }

    # LAYOUT
    def widget_layout(self):
        self.labels['outs_question'].grid(row=0, column=0, columnspan=4)
        self.labels['outs_text'].grid(row=0, column=4, sticky=tk.W)
        self.labels['entered_outs'].grid(row=0, column=5, sticky=tk.E)
        self.entries['outs_entry'].grid(row=1, column=0, columnspan=4, sticky=tk.W + tk.E)
        self.buttons['flop_button'].grid(row=2, column=0, columnspan=1, sticky=tk.W)
        self.buttons['turn_button'].grid(row=2, column=1, columnspan=1, sticky=tk.W)
        self.buttons['back_button'].grid(row=2, column=2, columnspan=1, sticky=tk.W)
        self.labels['equity_text'].grid(row=2, column=4, sticky=tk.W)
        self.labels['equity_percent'].grid(row=2, column=5, sticky=tk.E)

    # METHODS
    # method to validate entered character in selected entry field
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

    # method to execute operations when selected button is clicked
    def button_push(self, method):
        # operations if "flop" button is pushed
        # define natural equity and further set layout
        if method == "flop":
            self.natural_equity = str(round(((self.entered_outs / 47) + (self.entered_outs / 46)) * 100))
            self.labels['fold_question'].grid(row=3, column=0, columnspan=4, sticky=tk.W)
            self.labels['F%_text'].grid(row=3, column=4, sticky=tk.W)
            self.labels['entered_folds'].grid(row=3, column=5, sticky=tk.E)
            self.entries['folds_entry'].grid(row=4, column=0, columnspan=4, sticky=tk.W + tk.E)
            self.labels['fold_equity_text'].grid(row=4, column=4, sticky=tk.W)
            self.labels['fold_equity'].grid(row=4, column=5, sticky=tk.E)
            self.buttons['calculate_button'].grid(row=5, column=0, sticky=tk.W)
        # operations if "turn" button is pushed
        # define natural equity and further set layout
        elif method == "turn":
            self.natural_equity = str(round((self.entered_outs / 46) * 100))
            self.labels['fold_question'].grid(row=3, column=0, columnspan=4, sticky=tk.W)
            self.labels['F%_text'].grid(row=3, column=4, sticky=tk.W)
            self.labels['entered_folds'].grid(row=3, column=5, sticky=tk.E)
            self.entries['folds_entry'].grid(row=4, column=0, columnspan=4, sticky=tk.W + tk.E)
            self.labels['fold_equity_text'].grid(row=4, column=4, sticky=tk.W)
            self.labels['fold_equity'].grid(row=4, column=5, sticky=tk.E)
            self.buttons['calculate_button'].grid(row=5, column=0, sticky=tk.W)
        # operations if "calculate" button is pushed
        # defines equity gain, fold equity, and total equity
        # further set layout
        elif method == 'calculate':
            equity_gain = 100 - int(self.natural_equity)
            self.fold_equity = round((((self.entered_folds / 100) * (equity_gain / 100)) * 100), 2)
            self.total_equity = round((int(self.natural_equity) + self.fold_equity), 2)
            self.labels['total_equity_text'].grid(row=5, column=4, sticky=tk.W)
            self.labels['total_equity'].grid(row=5, column=5, sticky=tk.E)
        # operations if "back" button is pushed
        # destroys all widgets
        # resets all mutable values to 0
        # redefines widgets and resets layout
        elif method == 'back':
            children = self.winfo_children()
            for child in children:
                child.destroy()
            self.entered_outs = 0
            self.entered_folds = 0
            self.natural_equity = 0
            self.fold_equity = 0
            self.total_equity = 0
            self.widgets()
            self.widget_layout()
            self.controller.show_frame("StartFrame")
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


# RANDOM NUMBER GENERATOR FRAME
class RNGFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # VARIABLES
        # predefine variables for future use
        self.outcome_text = None
        self.entered_fold = 0
        self.entered_call = 0
        self.entered_bet = 0
        self.entered_raise = 0

        # set variable to string type and set contents
        self.outcome_label_text = StringVar()
        self.entered_fold = IntVar()
        self.outcome_label_text.set(self.outcome_text)

        # define validate command variable
        self.vcmd1 = self.master.register(self.validate)

        # WIDGETS
        generate_button = tk.Button(self, text="Generate", command=lambda: self.generate('generate'))

        entries = {
            "fold_entry": tk.Entry(self, validate='key', validatecommand=(self.vcmd1, '%P')),
            "call_entry": tk.Entry(self, validate='key', validatecommand=(self.vcmd1, '%P')),
            "bet_entry": tk.Entry(self, validate='key', validatecommand=(self.vcmd1, '%P')),
            "raise_entry": tk.Entry(self, validate='key', validatecommand=(self.vcmd1, '%P'))
        }

        self.labels = {
            "RNG_label": tk.Label(self, text="Random Number Generator"),
            "freq_label": tk.Label(self, text="Entered desired frequencies..."),
            "fold_label": tk.Label(self, text="Fold: "),
            "call_label": tk.Label(self, text="Call: "),
            "bet_label": tk.Label(self, text="Bet: "),
            "raise_label": tk.Label(self, text="Raise"),
            "outcome_label": tk.Label(self, text="Outcome: "),
            "outcome_result_label": tk.Label(self, textvariable=self.outcome_label_text)
        }

        # LAYOUT
        self.labels['RNG_label'].grid(row=0, column=0, columnspan=5)
        self.labels['freq_label'].grid(row=2, column=0, columnspan=4)
        self.labels['fold_label'].grid(row=5, column=0, columnspan=1)
        entries['fold_entry'].grid(row=5, column=1, columnspan=1)
        self.labels['call_label'].grid(row=5, column=2, columnspan=1)
        entries['call_entry'].grid(row=5, column=3, columnspan=1)
        self.labels['bet_label'].grid(row=6, column=0, columnspan=1)
        entries['bet_entry'].grid(row=6, column=1, columnspan=1)
        self.labels['raise_label'].grid(row=6, column=2, columnspan=1)
        entries['raise_entry'].grid(row=6, column=3, columnspan=1)
        generate_button.grid(row=7, column=0, columnspan=1)
        self.labels['outcome_label'].grid(row=7, column=2, columnspan=1)
        # labels['outcome_result_label'].grid(row=7, column=3, columnspan=1)

    # METHODS
    def validate(self, new_char):
        if not new_char:
            self.entered_fold = 0
            self.entered_call = 0
            self.entered_bet = 0
            self.entered_raise = 0
            return True

        try:
            self.entered_fold = int(new_char)
            self.entered_call = int(new_char)
            self.entered_bet = int(new_char)
            self.entered_raise = int(new_char)
            return True
        except ValueError:
            return False

    # method to create a list of inputs at desired frequency
    # shuffles input and grabs top result
    def generate(self, method):
        # if method == "generate":
        action_list = []
        action_dict = {
            "fold": str("Fold"),
            "call": str("Call"),
            "bet": str("Bet"),
            "rraise": str("Raise")
        }

        if method == "generate":
            for i in range(self.entered_fold):
                action_list.append(action_dict['fold'])
            for i in range(self.entered_call):
                action_list.append(action_dict['call'])
            for i in range(self.entered_bet):
                action_list.append(action_dict['bet'])
            for i in range(self.entered_raise):
                action_list.append(action_dict['rraise'])

            random.shuffle(action_list)
            print(action_list)
            self.outcome_text = action_list[0]
            self.labels['outcome_result_label'].grid(row=7, column=3, columnspan=1)
            # self.outcome_label_text.set(self.outcome_text)
        else:
            self.outcome_text = None

        self.outcome_label_text.set(self.outcome_text)


def main():
    PEC_gui = ContainerFrame()
    PEC_gui.mainloop()


if __name__ == '__main__':
    main()
