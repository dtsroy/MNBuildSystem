import tkinter as tk
from PTools import GetAdd, GetColor
from Block import *

class BlockButton:
	def __init__(self, win, bg, pos, weights):
		self.button = tk.Button(
								win,
								text = '',
								bg = bg,
								width = 3,
								height = 1,
								command = self.onclick
								)
		self.pos = pos
		self.win = win
		self.weights = weights

	def place(self, x, y):
		self.button.place(x = x, y = y)

	def onclick(self):
		self.tp = tk.Toplevel(self.win)
		self.tp.wm_attributes('-topmost', 1)
		self.tp.title(repr(self.pos))
		self.tp.geometry('400x700')
		self.BLOCKS = [Block(self.weights[9 - i], self.pos + [10 - i], self.tp) for i in range(10)]
		self.tp.resizable(0, 0)
		#tk.Label(self.tp, text = 'Weight: ' + str(GetAdd(self.weights))).place(x = 0, y = 0)
		for k in self.BLOCKS:
			tk.Label(self.tp, text = repr(k.pos))\
					.place(x = 0, y = self.BLOCKS.index(k) * 65 + 18)
			k.scale.pack()
		tk.Button(self.tp, text = 'Save', command = self.Save).pack()
		self.tp.bind('<Control-s>', self.Save)
		self.tp.bind('<KeyPress-Up>', lambda e: self.BLOCKS[2].scale.set(self.BLOCKS[2].scale.get() + 10))
		self.tp.bind('<KeyPress-Down>', lambda e: self.BLOCKS[4].scale.set(self.BLOCKS[4].scale.get() + 10))
		self.tp.bind('<KeyPress-Left>', lambda e: self.BLOCKS[6].scale.set(self.BLOCKS[6].scale.get() + 10))
		self.tp.mainloop()

	def Save(self, event=None):
		for s in self.BLOCKS:
			w = s.scale.get()
			s.weight = w
			#print(w)
			self.weights[9 - self.BLOCKS.index(s)] = w
		self.button['bg'] = GetColor(GetAdd(self.weights) // 10)
		
