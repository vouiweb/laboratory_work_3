import os


file = open("products.txt", "r")
sort = []
for line in file:
	line = line.strip()
	line = line.split(";")
	sort.append(line)

max = int(sort[len(sort)-1][0])


def Work():
	global availability
	answer = input('Вы хотите продолжить? Y/N \n')
	if answer.lower() == 'n':
		availability = False


def Find():
	path = input('Введите директорию: ')
	count = str(len(next(os.walk(path))))
	print(count)


def Sort():
	global sort
	new_sort = sort
	for j in range(0, len(new_sort)):
		for i in range(0, len(new_sort)-1):
			if int(new_sort[i][3]) > int(new_sort[i+1][3]):
				stroka = new_sort[i]
				new_sort[i] = new_sort[i+1]
				new_sort[i+1] = stroka
	return new_sort


def Change_stock():
	global max
	new_sort = Sort()
	id = []
	print('Введите id товаров, у которых хотите изменить количество по одному.\n'
	'stop - остановка ввода id товаров. \n'
	'Максимальный id = ', max)

	work1 = True
	while work1:
		add = input('ID: ')
		if add.isdigit():
			add = int(add)
			if add <= max:
				id.append(add)
			else:
				print('Максимальный ID = ', max, ', Вы ввели: ', add)
		elif add.lower() == 'stop':
			work1 = False
		else:
			print('Пожалуйста, вводите числа, а не буквы и спец. символы.')

	count = int(input('Введите на сколько хотите уменьшить количество товара,' 
		'если число будет превышать количество, то количество станет равным 0: '))
	for i in range(0, len(new_sort)):
		for j in range(0, len(id)):
			if int(new_sort[i][0]) == int(id[j]):
				if int(new_sort[i][3]) - count >= 0:
					new_sort[i][3] = int(new_sort[i][3]) - count
				else:
					new_sort[i][3] = 0
	return new_sort


def SaveNew():
	new_sort = Change_stock()
	work = True
	while work:
		answer = input('Вы желаете сохранить результат как новый файл? Y/N \n')
		if answer.lower() == 'y':
			file_name = input('Тогда, введите название файла: ')
			new_file = open(file_name, 'w')
			for i in range(0, len(new_sort)):
				for j in range(0, len(new_sort[i])):
					if 0 <= j <= 2:
						new_file.write(str(new_sort[i][j]) + ";")
					else:
						new_file.write(str(new_sort[i][j]))
				new_file.write('\n')
		if answer.lower() == 'n':
			new_file = open('products.txt', 'r+')
			for i in range(0, len(new_sort)):
				for j in range(0, len(new_sort[i])):
					if 0 <= j <= 2:
						new_file.write(str(new_sort[i][j]) + ";")
					else:
						new_file.write(str(new_sort[i][j]))
				new_file.write('\n')
			work = False
			new_file.close()
		else:
			work = False


print("0 - выйти из программы \n1 - Функция номер 1 \n2 - Функция номер 2\n3 - Функция номер 3\n4 - Функция номер 4")
availability = True
while availability:
	command = input('Введите команду: ')
	if command == "0":
		something = input('Вы действительно хотите выйти из программы? Y/N \n')
		if something.lower() == 'y':
			availability = False
		elif something.lower() != 'n':
			print('Неизвестная команда!')
	if command == "1":
		Find()
	if command == "2":
		print(Sort())
	if command == "3":
		print(Change_stock())
	if command == "4":
		SaveNew()
	if not command.isdigit():
		print('Неизвестная команда')
	if not 'something' in globals() or not 'something' in locals():
		Work()