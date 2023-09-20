import tkinter as tk
from bg_get_verse import getBGVerse

window = tk.Tk()
window.title('Bhagvad Gita')

verseFrame = tk.Frame(window,height=11,width=200)
verseFrame.grid(row=0,column=0)

cur_verse = getBGVerse()

displayVerseHindi = tk.Label(
    verseFrame,
	text=cur_verse[0],
	height=10,
	width=200,
	wraplength=1000
)
displayVerseHindi.grid(row=0,column=0)#getBGVerse())
#displayVerseHindi.pack()

displayVerseEng = tk.Label(
    verseFrame,
	text=cur_verse[1],
	width=200,
	wraplength=1000,
	)
displayVerseEng.grid(row=1,column=0)
#displayVerseEng.pack()

buttonFrame = tk.Frame(window,height=2,width=6)
buttonFrame.grid(row=1,column=0)

def handle_refresh_click(event):
	refreshButton.config()
	tmp = getBGVerse()
	displayVerseHindi.config(text=tmp[0])
	displayVerseEng.config(text=tmp[1])

refreshButton = tk.Button(
    buttonFrame,
	text="Refresh",
	width=5,
	height=1)
refreshButton.grid(row=0,column=1,padx=5,pady=8)
refreshButton.bind("<Button-1>",handle_refresh_click)
#refreshButton.pack(pady=8)


window.mainloop()
