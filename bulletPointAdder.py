#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.
import pyperclip

text_copy = pyperclip.paste()
if text_copy.isspace():
    print("There is nothing copied in your clipboard.  Please select the text and copy it.")
else:
    # # TODO: Separate lines and add stars.
    # temp_text = text_copy.split('\n')
    # temp_list = []
    # # print(temp_text)
    # for i in temp_text:
    #     new_string = "* " + i
    #     print(new_string)
    #     temp_list.append(new_string)
    # print(temp_list)
    # new_text = '\n'.join(temp_list)
    # pyperclip.copy(new_text)
    lines = text_copy.split('\n')
    for i in range(len(lines)):
        lines[i] = "* " + lines[i]
    new_text = '\n'.join(lines)
    pyperclip.copy(new_text)
