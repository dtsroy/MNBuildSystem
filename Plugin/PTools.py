import math
from threading import Thread
from base64 import b64encode, b64decode
import json

class error(Exception):
	def __init__(self):
		pass

S_TO_Bytes = {
				'a': b'\x04\xef', 'b': b'\x05\x81',
				'c': b'\x06\xc4', 'd': b'\x04\xe5',
				'e': b'\x07O', 'f': b'\x04\xfb',
				'g': b'\x06W', 'h': b'\x06q',
				'i': b'\x06M', 'j': b'\x04`',
				'k': b'\x06\x8c', 'l': b'\x04\x8a',
				'm': b'\x06\xc3', 'n': b'\x05X',
				'o': b'\x04\xf1', 'p': b'\x07j',
				'q': b'\x05G', 'r': b'\x05\xd1',
				's': b'\x07\x8f', 't': b'\x06\n',
				'u': b'\x05\xf5', 'v': b'\x077',
				'w': b'\x04w', 'x': b'\x06\x89',
				'y': b'\x04\xd8', 'z': b'\x05;',
				'A': b'\x05\xb8', 'B': b'\x067',
				'C': b'\x05\xee', 'D': b'\x05I',
				'E': b'\x06\xa3', 'F': b'\x06\x0f',
				'G': b'\x04\xa8', 'H': b'\x07p',
				'I': b'\x07`', 'J': b'\x05j',
				'K': b'\x04\x8c', 'L': b'\x06\xa2',
				'M': b'\x06\x83', 'N': b'\x07\x0b',
				'O': b'\x066', 'P': b'\x07\xab',
				'Q': b'\x05H', 'R': b'\x04\xe1',
				'S': b'\x07-', 'T': b'\x05 ',
				'U': b'\x07h', 'V': b'\x04\xd5',
				'W': b'\x05\x98', 'X': b'\x04\xed',
				'Y': b'\x04j', 'Z': b'\x07\x08',
				'+': b'\x04c', '=': b'\x06\xb4',
				'/': b'\x05\xdc', '0': b'\xad\x33',
				'1': b'\xad\x32', '2': b'\xad\x12',
				'3': b'\xad\x45', '4': b'\xad\x46',
				'5': b'\xad\x47', '6': b'\xad\x48',
				'7': b'\xad\x49', '8': b'\xad\x99',
				'9': b'\xad\x55'
			 }

Bytes_TO_S = {
				b'\x04\xef': 'a', b'\x05\x81': 'b',
				b'\x06\xc4': 'c', b'\x04\xe5': 'd',
				b'\x07O': 'e', b'\x04\xfb': 'f',
				b'\x06W': 'g', b'\x06q': 'h',
				b'\x06M': 'i', b'\x04`': 'j',
				b'\x06\x8c': 'k', b'\x04\x8a': 'l',
				b'\x06\xc3': 'm', b'\x05X': 'n',
				b'\x04\xf1': 'o', b'\x07j': 'p',
				b'\x05G': 'q', b'\x05\xd1': 'r',
				b'\x07\x8f': 's', b'\x06\n': 't',
				b'\x05\xf5': 'u', b'\x077': 'v',
				b'\x04w': 'w', b'\x06\x89': 'x',
				b'\x04\xd8': 'y', b'\x05;': 'z',
				b'\x05\xb8': 'A', b'\x067': 'B',
				b'\x05\xee': 'C', b'\x05I': 'D',
				b'\x06\xa3': 'E', b'\x06\x0f': 'F',
				b'\x04\xa8': 'G', b'\x07p': 'H',
				b'\x07`': 'I', b'\x05j': 'J',
				b'\x04\x8c': 'K', b'\x06\xa2': 'L',
				b'\x06\x83': 'M', b'\x07\x0b': 'N',
				b'\x066': 'O', b'\x07\xab': 'P',
				b'\x05H': 'Q', b'\x04\xe1': 'R',
				b'\x07-': 'S', b'\x05 ': 'T',
				b'\x07h': 'U', b'\x04\xd5': 'V',
				b'\x05\x98': 'W', b'\x04\xed': 'X',
				b'\x04j': 'Y', b'\x07\x08': 'Z',
				b'\x04c': '+', b'\x06\xb4': '=',
				b'\x05\xdc': '/', b'\xad\x33': '0',
				b'\xad\x32': '1', b'\xad\x12': '2',
				b'\xad\x45': '3', b'\xad\x46': '4',
				b'\xad\x47': '5', b'\xad\x48': '6',
				b'\xad\x49': '7', b'\xad\x99': '8',
				b'\xad\x55': '9'
			 }

def split_with_num(num, s):
	li = []
	if len(s) % num != 0:
		raise error
	for k in range(len(s) // num):
		li.append(s[k * num:(k + 1) * num])
	# print(li)
	return li

def panencode(instr):
	body = b''
	instr2 = b64encode(instr.encode('utf-8')).decode('utf-8')
	# print(instr2)
	for k in instr2:
		body += S_TO_Bytes[k]
	return body

def pandecode(inbytes):
	body = ''
	bl = split_with_num(2, inbytes)
	for k in bl:
		body += Bytes_TO_S[k]
	b2 = b64decode(body.encode('utf-8'))
	return b2.decode('utf-8')

def psave(file, instr, flag=True):
	with open(file, 'wb+') as f:
		f.write(panencode(instr))

def pload(file, flag=True):
	with open(file, 'rb') as f:
		con = pandecode(f.read())
	return con if not flag else json.loads(con)

def GetAdd(list_):
	k = 0
	for m in list_:
		k += m
	return k

def GetColor(w):
	colors = pload('../Data/Colors.pan')
	if w >= 0 and w < 11:
		return colors[0]
	elif w >= 11 and w < 21:
		return colors[1]
	elif w >= 21 and w < 31:
		return colors[2]
	elif w >= 31 and w < 41:
		return colors[3]
	else:
		return colors[4]

def StartThread(func):
	Thread(target = func, args = ()).start()

def YposW(posweilist):
	WeightIndex = pload('../Data/POSTRAIN.pan')
	left = 0
	right = 0
	for k in posweilist:
		#print(k)
		if k[0][0] < 6:
			left += WeightIndex[k[0][0] - 1] * GetAdd(k[1])
		else:
			right += WeightIndex[k[0][0] - 1] * GetAdd(k[1])
	return [right, left]


def XposW(posweilist):
	WeightIndex = pload('../Data/POSTRAIN.pan')
	down = 0
	up = 0
	for k in posweilist:
		#print(k)
		if k[0][1] < 6:
			for i in k[1]:
				down += WeightIndex[k[0][1] - 1] * i
		else:
			for i in k[1]:
				up += WeightIndex[k[0][1] - 1] * i
	return [up, down]

def GetDeg(wpro):
	if len(wpro) != 2:
		raise error
	cm = wpro[1] - wpro[0]
	print(cm * 0.18)
	return cm * 0.18

#print(GetDeg([1, 3]))

def XOYBPOS():
	li = []
	for i in range(10):
		for j in range(10):
			li.append([35 * (i + 2)- 65, 35 * (j + 2) - 68])
	return li

def GetPos(dg):
	dp = math.fabs(dg)
	xp = 65 - (math.cos(math.radians(dp)) * 65)
	yp = 65 + (math.sin(math.radians(dp)) * 65)
	if dg > 0:
		return [xp, yp, 130 - xp, 130 - yp]
	elif dg == 0:
		return [0, 65, 130, 65]
	else:
		return [130 - xp, yp, xp, 130 - yp]

#print(GetPos(60))