from tkinter.filedialog import askopenfilename, asksaveasfilename
import re
import tkinter as tk
from BlockButton import BlockButton
from json import loads
from PTools import pload, XposW, YposW
from tkinter.font import Font
from PTools import XOYBPOS, GetPos, GetDeg
from PTools import psave
import os

class mn:
	def __init__(self, weights, filename='UnDefineFile'):
		self.weights = weights
		self.filename = filename
		self.colors = pload('../Data/Colors.pan')
		self.root = tk.Tk()
		self.root.wm_attributes('-topmost', 1)
		self.root.title('Mn Bulid System(%s)' % self.filename)
		self.root.geometry('500x400')
		self.root.resizable(0, 0)
		self.build()
		self.root.bind('<KeyPress-F5>', self.update)
		self.root.bind('<KeyPress-b>', self.XOYB[13].button['command'])		
		self.root.bind('<Control-s>', self.Save)
		self.root.bind('<Control-S>', self.Save)
		self.root.bind('<Control-Shift-s>', self.SaveAs)
		self.root.bind('<Control-Shift-S>', self.SaveAs)
		self.root.bind('<Control-o>', self.Open)
		self.root.bind('<Control-O>', self.Open)

	def build(self):
		#tk.Label(self.root, text = 'WorkSpace').place(x = 0, y = 0)
		self.XOYB = []
		self.XOYBPOS = XOYBPOS()
		tmp = 0
		for i in range(10):
			for j in range(10):
				self.XOYB.append(
					BlockButton(self.root,
						bg = self.colors[0],
						pos = [i + 1, 10 - j],
						weights = self.weights[tmp])
					)
				tmp += 1
		index = 0
		for i in self.XOYB:
			i.place(x = self.XOYBPOS[index][0], y = self.XOYBPOS[index][1])
			index += 1
		bianc = 130
		tk.Label(self.root, text = 'B       F',
			font = Font(family = 'Lucida Grande', size = 20)).\
		place(x = 360, y = 0)
		tk.Label(self.root, text = 'L       R',
			font = Font(family = 'Lucida Grande', size = 20)).\
		place(x = 360, y = 180)
		self.canvasx = tk.Canvas(self.root, bg = 'black', width = bianc, height= bianc)
		self.canvasx.place(x = 360, y = 30)
		self.canvasy = tk.Canvas(self.root, bg = 'black', width = bianc, height= bianc)
		self.canvasy.place(x = 360, y = 210)
		self.Creat_W_Line()
		tk.Button(self.root, text = 'Save', command = self.Save, height = 1, width = 7, font = Font(family = 'Lucida Grande', size = 18)).place(x = 10, y = 350)
		tk.Button(self.root, text = 'SaveAs', command = self.SaveAs, height = 1, width = 8, font = Font(family = 'Lucida Grande', size = 18)).place(x = 135, y = 350)
		tk.Button(self.root, text = 'Open', command = self.Open, height = 1, width = 6, font = Font(family = 'Lucida Grande', size = 18)).place(x = 280, y = 350)
		tk.Button(self.root, text = 'Quit', command = self.root.quit, height = 1, width = 6, font = Font(family = 'Lucida Grande', size = 18)).place(x = 410, y = 350)

	def Creat_W_Line(self):
		self.canvasx.create_line(0, 65, 130, 65, fill = 'white', width = 3)
		self.canvasy.create_line(0, 65, 130, 65, fill = 'white', width = 3)

	def Delete_All_Line(self):
		self.canvasx.delete(tk.ALL)
		self.canvasy.delete(tk.ALL)

	def Draw_New_Line(self, x, y):
		self.canvasx.create_line(*GetPos(GetDeg(XposW(x))), fill = 'red', width = 5)
		self.canvasy.create_line(*GetPos(GetDeg(YposW(y))), fill = 'red', width = 5)

	def update(self, e=None):
		xtmp = ([o.pos, o.weights] for o in self.XOYB)
		ytmp = ([o.pos, o.weights] for o in self.XOYB)
		self.Delete_All_Line()
		self.Creat_W_Line()
		self.Draw_New_Line(xtmp, ytmp)
		self.weights = [l.weights for l in self.XOYB]

	def Save(self, e=None):
		if not re.match(r'.*\.pan', self.filename):
			self.filename = asksaveasfilename(title = 'Save As...', filetypes = [('PAN File', '*.pan')])
		self.weights = [l.weights for l in self.XOYB]
		self.root.title('Mn Bulid System(%s)' % os.path.abspath(self.filename))
		psave(self.filename, repr(self.weights))

	def SaveAs(self, e=None):
		self.weights = [l.weights for l in self.XOYB]
		self.filename = asksaveasfilename(title = 'Save As...', filetypes = [('PAN File', '*.pan')])
		self.root.title('Mn Bulid System(%s)' % os.path.abspath(self.filename))
		psave(self.filename, repr(self.weights))

	@classmethod
	def Open(cls, e=None):
		f = askopenfilename(title = 'Choose File', filetypes = [('PAN File', '*.pan')])
		#self.filename = f
		newcls = cls(pload(f))
		newcls.root.title('Mn Bulid System(%s)' % os.path.abspath(f))
		newcls._main()

	def _main(self):
		self.root.mainloop()

def main():
	ltp = [[0 for k in range(10)] for k in range(100)]
	n = mn(ltp)
	n._main()

