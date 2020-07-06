import tkinter as tk
import json
import PTools

class Block:
	def __init__(self, weight, pos, win):
		self.colors = PTools.pload('../Data/Colors.pan')
		self.weight = weight
		self.pos = pos
		self.win = win
		self.bg = self.colors[0]
		self.scale = tk.Scale(
								self.win,
								from_ = 0,
								to = 50,
								orient = tk.HORIZONTAL,
								tickinterval = 5,
								length = 300
							 )
		self.scale.set(self.weight)

# s1 = tk.Scale(tp, from_ = 0, to = 50, orient = tk.HORIZONTAL, tickinterval = 5, length = 300)