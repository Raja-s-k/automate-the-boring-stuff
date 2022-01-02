<pre>

mport pyperclip, re

text = pyperclip.paste()
strip = re.sub(r'^\s+|\s+$', '', text)
pyperclip.copy(strip)    
print(strip)

<\pre>