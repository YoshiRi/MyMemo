import tkinter as tk
import pyperclip
import re

# 行末のハイフンと改行を削除
def shaping(txt):
    lines = re.split("\n\r",txt)
    output = ""
    for line in lines:
        if line:
            if line[-1] == "-":
                output += line[:-1] + " "
            else:
                output += line + " "
    return output

root = tk.Tk()
# 入力を取得
def retrieve_input():
    inputValue=textBox.get("1.0","end-1c")
    shaped = shaping(inputValue)
    # copy to clip board
    pyperclip.copy(shaped)
    print("Copied ",len(shaped),"charactors!")


# delete box
def deletebox():
    textBox.delete(1.0, tk.END)

# Create GUI
textBox=tk.Text(root, height=40, width=40,title = "Shaping")
textBox.pack()
buttonCopy=tk.Button(root, height=1, width=10, text="Copy", 
                    command=lambda: retrieve_input())
buttonClear=tk.Button(root, height=1, width=10, text="Clear", 
                    command=lambda: deletebox())

#command=lambda: retrieve_input() >>> just means do this when i press the button
buttonCopy.pack()
buttonClear.pack()

tk.mainloop()