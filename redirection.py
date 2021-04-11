#redirection.py
 
import sys
import tkinter as tk
 
 
class StdoutRedirector(object):
    def __init__(self, text_widget):
        self.text_widget = text_widget
 
    def write(self, s):
        self.text_widget.insert('end', s)
        self.text_widget.see('end')
 
 
class StdoutTkinter(tk.Tk):
    def __init__(self):
        super().__init__()

 
        self.title('STDOUT:')
 
        frame = tk.Frame(self, width=200, height=300)
        frame.pack()

        self.textbox = tk.Text(frame, wrap='word', fg="green", bg="black")
        self.textbox.pack()
 
        ## On pointe le sys.stdout vers le textbox
        sys.stdout = StdoutRedirector(self.textbox)