import tkinter as tk
from bg_get_verse import getBGVerse

verses = getBGVerse()
window = tk.Tk()
displayVerseHindi = tk.Label(
	text=verses[0],
	height=10,
	width=200,
	wraplength=1000
)#getBGVerse())
displayVerseHindi.pack()

displayVerseEng = tk.Label(
	text=verses[1],
	width=200,
	wraplength=1000,
	)
displayVerseEng.pack()

def handle_click(event):
	button.config()
	tmp = getBGVerse()
	displayVerseHindi.config(text=tmp[0])
	displayVerseEng.config(text=tmp[1])

button = tk.Button(
	text="Refresh",
	width=5,
	height=1)
button.bind("<Button-1>",handle_click)
button.pack(pady=8)
window.mainloop()