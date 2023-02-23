import tkinter
from tkinter import *
from tkinter.messagebox import showerror, showwarning, showinfo
import openai
import pyperclip
import os


if os.path.exists("key.txt"):
  print("The file 'key.txt' exists")
  with open('key.txt', 'r') as f:
    key = f.read()
  f.close()
else:
  print("The file 'key.txt' does not exist")
  #open the file "key.txt" in write mode
  with open("key.txt", "w") as f:
    print("The file key.txt was created (but is empty)")
    key = ""
  #close the file
  f.close()

root = tkinter.Tk()
root.geometry("400x525")

label = tkinter.Label(root, text="PromptGUI", font=("Arial", 70))
label.pack()

space = tkinter.Label(root, text=" ")
space.pack()

input_label = tkinter.Label(root, text="Input:")
input_label.pack()

text_field = tkinter.Entry(root)
text_field.pack()

tkinter.Label(root, text="(character limit: 100)").pack()

def generate():
    try:
        text_fieldInput = text_field.get()
        if len(text_fieldInput) > 100:
            text_fieldInput = text_fieldInput[:100]
            showwarning(title='Warning', message=f"More than 100 Characters in text field. I've cut it to 100. 👍")

        # Doing 100% API key stuff :)
        with open('key.txt', 'r') as f:
            openai.api_key_path = "key.txt"
        f.close()
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"""Human: {text_fieldInput}
            Assistant:""",
            max_tokens=100,
            temperature=0.5,
            stop=["Human:", "Assistant:"]
        )
        output_text.config(text=response.choices[0].text)
    except:
        showwarning(title='Warning', message=f"Something went wrong. Is the API Key correct?")

button = tkinter.Button(root, text="Generate!", command=generate)
button.pack()

space = tkinter.Label(root, text=" ")
space.pack()

output_label = tkinter.Label(root, text="Output:")
output_label.pack()

output_text = tkinter.Label(root, text="There is no output yet...", font="italic", wraplength=300, justify="center")
output_text.pack()

def copy_to_clipboard():
    pyperclip.copy(str(output_text.cget("text")))

copyButton = tkinter.Button(root, text="Copy Output", command=copy_to_clipboard)
copyButton.pack()

# This is space between the actual interface and the few API-Key-Set buttons
space = tkinter.Label(root, text=" ")
space.pack()
space = tkinter.Label(root, text=" ")
space.pack()
space = tkinter.Label(root, text=" ")
space.pack()
space = tkinter.Label(root, text=" ")
space.pack()
space = tkinter.Label(root, text=" ")
space.pack()
space = tkinter.Label(root, text=" ")
space.pack()


apiKey_label = tkinter.Label(root, text="Set your API Key:")
apiKey_label.pack()

# Create input field
apiInputField = Entry(root)
apiInputField.pack()

# Check if key is not empty
if key != "":
    apiInputField.delete(0, END)
    apiInputField.insert(0, "Key was already set.")

# Create button
def apiSetButton():
    print("API set!")
    showinfo(title='Info', message=f"API Key was successfully set!")
    key = str(apiInputField.get())

    with open("key.txt", "w") as f:
        f.truncate(0)
        f.write(key)
    #close the file
    f.close()


apiSetButton = Button(root, text="Set Key", command=apiSetButton)
apiSetButton.pack()

root.mainloop()