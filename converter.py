import math
import numpy as np

	
print('''
Ushbu dastur yordamida dekart k.s dan sferik k.s ga va aksincha o`tish mumkin.
Kerakli raqamni tanlang:
 _________________________________________________
+                                                 +
| [1] - Dekart k.s dan sferik k.s ga o`tish uchun  |
| [2] - Sferik k.s dan Dekart k.s ga o`tish uchun  |
+_________________________________________________+ 
''')


a = int(input())

if a == 1:
	print("X, Y, Z koordinatalarni kiriting:")
	x,y,z = int(input()),int(input()), int(input())
	
	r = math.sqrt(x**2 + y**2 + z**2)
	theta = math.atan(math.sqrt(x**2 + y**2)) / z
	phi = math.atan(y / z)
	print("R = ", r, "theta = ", math.degrees(theta), "phi = ", math.degrees(phi))
	
elif a == 2:
	
	print("R radiusni  kiriting: ")
	r = int(input())
	
	print('''Burchaklarni radianlarda kiritasizmi yoki graduslardami?
	 r - radianlarda
	 g - graduslarda
	 ''')
	a = str(input())
	print("Juda yaxshi! Endi theta va phi burchaklarni kiriting:")
	theta, phi = int(input()), int(input())
	if a == 'g':
		x = r * np.sin(math.radians(theta)) * np.cos(math.radians(phi))
		y = r * np.sin(math.radians(theta)) * np.sin(math.radians(phi))
		z = r * np.cos(math.radians(phi))
		print("X = ", x, "Y = ", y, "Z = ", z)
	elif a == 'r':
		x = r * np.sin(theta) * np.cos(phi)
		y = r * np.sin(theta) * np.sin(phi)
		z = r * np.cos(phi)
		print("X = ", x, "Y = ", y, "Z = ", z)	
	
	
else:
	print("Noto`gri son kiritdingiz!")
