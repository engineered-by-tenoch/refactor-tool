from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Refactor Utility")

entry_frame = ttk.Frame(root)
entry_frame.pack(fill="both", expand=True)
entry_frame.config(relief="sunken")

action_frame = ttk.Frame(entry_frame)
action_frame.pack(side="right", anchor="nw", padx=10, pady=10, fill="y")
action_frame.config(relief="sunken")

input_frame = ttk.Frame(entry_frame)
input_frame.pack(side="left", anchor="ne", fill="both", expand=True)
input_frame.config(relief="sunken")

output_frame = ttk.Frame(root)
output_frame.pack(fill="x", side="bottom")
output_frame.config(relief="sunken")

entry = Text(input_frame, height=10, width=50)
entry.insert(1.0, "Type here...")
entry.pack(side="left", padx=10, pady=10, fill="both", expand=True)
entry.config(wrap='word')


output = Text(output_frame, height=8, width=50)
output.pack(side="left", padx=5, pady=5, expand=True, fill="both")
output.insert(1.0, "Output shows here...")
output.config(wrap='word')


redox_dict = {}
n_refactors = 1
refactorers = []
all_redactors = []


class Redactor:
    def __init__(self, rid):
        global refactorers
        self.rid = rid
        self.a = None
        self.b = None
        refactorers.append(self.rid)

    def generate(self):
        row_frame = ttk.Frame(action_frame)
        row_frame.pack(side="top", fill="x", padx= 2, pady=0)

        self.a = ttk.Entry(row_frame, width=8)
        self.a.pack(side="left", padx=2.5, pady=2.5)

        self.b = ttk.Entry(row_frame, width=4)
        self.b.pack(side="right", padx=2.5, pady=2.5)
        self.b.insert(0, "*")

    def redact_process(self):
        redox = self.a.get()
        refactor = self.b.get()

        if not redox:
            return

        if refactor in ("none", "","*"):
            refactor = len(redox) * "*"

        redox_dict[redox] = refactor



def generate_substitute():
    global n_refactors
    new_row = Redactor(rid=n_refactors)
    new_row.generate()
    all_redactors.append(new_row)
    n_refactors += 1


def iterate_response():
    redox_dict.clear()

    for redactor in all_redactors:
        redactor.redact_process()

    document = entry.get(1.0, END).strip()
    words = document.split(" ")


    result = ""
    for word in words:
        clean_word = word.strip(".,!?")

        if clean_word in redox_dict:
            result += redox_dict[clean_word] + " "
        else:
            result += word + " "


    output.delete(1.0, END)
    output.insert(1.0, result.strip())


add_redaction = ttk.Button(action_frame, text="New Refactor", command=generate_substitute)
add_redaction.pack(side="top", padx=5, pady=5)

process_btn = ttk.Button(action_frame, text="Process Text", command=iterate_response)
process_btn.pack(side="bottom", padx=5, pady=5)

root.mainloop()