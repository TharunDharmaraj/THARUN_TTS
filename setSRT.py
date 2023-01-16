text = ""
i = 1

with open('believe.srt', 'r') as f:
   for line in f:
    if line.replace("\n", '', 1).isdigit():
        text += str(i) + "\n"
        i += 1
    else:
        text += line

with open("modified.srt", "w") as f1:
    f1.write(text)
