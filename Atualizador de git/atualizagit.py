# move
import os, sys

""

def walk(path):
	lista = os.listdir(path)
	# print(lista)
	for i in lista:
		if os.path.isdir(os.path.normpath(path+'/'+i+"/")):
			# print(os.path.normpath(path+'/'+i+"/"))
			print(os.path.normpath(path+'/'+i+"/"))
			os.chdir(os.path.normpath(path+'/'+i+"/"))
			# print("\n")
			walk(os.getcwd())
		# for j in os.listdir('.'):
		# 	print(os.getcwd()+j)
			# print()
		# else:
			# print(os.listdir('.'))
		# a = os.system("mv *.png /mnt/Windows-X/Takeout/Fotos/")
		# b = os.system("mv *.jpg /mnt/Windows-X/Takeout/Fotos/")


	# print(os.listdir(os.getcwd()))
	print(os.getcwd())
	os.chdir('..')

# walk('/home/maycon/Material-Códigos/Web Development/Ruby/git/')

# print("teste")
path = '/home/maycon/.config/sublime-text-3/Packages/'


lista = os.listdir(path)
for i  in lista :
	try:
		print(os.path.abspath(i))
		os.chdir(os.path.join(path,i))
		os.system("git pull")
		os.chdir("..")
	except Exception as e:
		pass



