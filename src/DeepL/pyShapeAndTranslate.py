import tkinter as tk
import pyperclip
import re
from selenium import webdriver
import time
import chromedriver_binary

# Scraping part
load_url = "https://www.deepl.com/ja/translator"
driver = webdriver.Chrome()  #  driver = webdriver.Chrome("c:/work/chromedriver.exe")
driver.get(load_url)


# send translation request
def translate(txt):
    input_selector = "#dl_translator > div.lmt__sides_container > div.lmt__side_container.lmt__side_container--source > div.lmt__textarea_container > div > textarea"
    driver.find_element_by_css_selector(input_selector).send_keys(txt)
    while 1:
        Output_selector = "#dl_translator > div.lmt__sides_container > div.lmt__side_container.lmt__side_container--target > div.lmt__textarea_container > div.lmt__translations_as_text > p > button.lmt__translations_as_text__text_btn"
        Outputtext = driver.find_element_by_css_selector(Output_selector).get_attribute("textContent")
        if Outputtext != "" :
            break
        time.sleep(1)
    print(Outputtext)
    pyperclip.copy(Outputtext)


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

def copyandtranslate():
    retrieve_input()
    translate(pyperclip.paste())

# delete box
def deletebox():
    textBox.delete(1.0, tk.END)

# Create GUI
textBox=tk.Text(root, height=40, width=40)
textBox.pack()
buttonCopy=tk.Button(root, height=1, width=10, text="Translate", 
                    command=lambda: copyandtranslate())
buttonClear=tk.Button(root, height=1, width=10, text="Clear", 
                    command=lambda: deletebox())

#command=lambda: retrieve_input() >>> just means do this when i press the button
buttonCopy.pack()
buttonClear.pack()

tk.mainloop()