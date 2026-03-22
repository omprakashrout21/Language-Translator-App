from tkinter import *
from tkinter import ttk
from deep_translator import GoogleTranslator

root = Tk()
root.title(" Translator App")
root.geometry("520x420")
root.config(bg="grey")

def translate():
    try:
        translated = GoogleTranslator(source=src.get(), target=dest.get()).translate(input_box.get("1.0", END))
        output_box.delete("1.0", END)
        output_box.insert(END, translated)
    except:
        output_box.delete("1.0", END)
        output_box.insert(END, "Error")

langs = ['english','hindi','french','german','spanish','italian','japanese','korean','russian','arrabic']

src = StringVar(value='en')
dest = StringVar(value='hi')

Label(root, text="Here You Can Translate", font=("Arial",18,"bold"), bg="black", fg="white").pack(pady=10)

input_box = Text(root, height=5, font=("Arial",12))
input_box.pack(padx=10, pady=5)

frame = Frame(root, bg="black")
frame.pack()

ttk.Combobox(frame, textvariable=src, values=langs, width=10).grid(row=0, column=0, padx=10)
ttk.Combobox(frame, textvariable=dest, values=langs, width=10).grid(row=0, column=1, padx=10)

Button(root, text="Translate", command=translate, bg="black", fg="white").pack(pady=10)

output_box = Text(root, height=5, font=("Arial",12))
output_box.pack(padx=10, pady=5)

root.mainloop()