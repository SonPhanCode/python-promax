import pyfiglet
while True:
	try:
		name = input("chữ: ")
		name = str(name)
		style = input("nhập loại chữ: ")
		style = str(style)
		word = pyfiglet.figlet_format(name , font= style)
		print(word)
	except Exception as e:
		print("error")
		style = input("nhập loại chữ: ")
		style = str(style)
		word = pyfiglet.figlet_format(name , font= style)
		print(word)
