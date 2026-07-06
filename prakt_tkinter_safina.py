from tkinter import*

root = Tk()
root.geometry("300x300")

Label(root,text='Ваш адрес: ').pack()
adres=Entry(root) # Entry это поле куда можно писать текст
adres.pack() # адрес

Label(root,text='Комментарий: ').pack()
commentariy=Entry(root)
commentariy.pack() # комментарий

# Функция чтобы программа напечатала то что мы ввели

def get():
    print('Адрес: ', adres.get())
    print('Коммент: ', commentariy.get())

# кнопка отправки и что она делает
Button(root, text='Отправить', command=get).pack()

# выход и уничтожение
Button(root, text='Выход', command=root.destroy).pack()

# оформляю со своими любимыми цветами со скрытым смыслом
# фрейм это рамка внутри которой мб чет ещё, bg это цвет, padx and pady это отступы
# Создаём внешний фрейм (фиолетовый)
# Чтобы их обоих видеть надо падкс чтобы отодвинуло на 5 пикселей и т.д. они будут меньше дркг друга на 5 пикслей
frame_violet = Frame(root, bg='pink', padx=5, pady=5)
frame_violet.pack(expand=YES, fill=BOTH)

# Внутри него синий фрейм
frame_blue = Frame(frame_violet, bg='white', padx=5, pady=5)
frame_blue.pack(expand=YES, fill=BOTH)
# expand=YES значит разрешить фрейму расширяться если есть свободное место
# fill=BOTH заполняет всё доступное пространство

# Внутри него голубой
frame_cyan = Frame(frame_blue, bg='purple', padx=5, pady=5)
frame_cyan.pack(expand=YES, fill=BOTH)

# Внутри него зелёный
frame_green = Frame(frame_cyan, bg='black', padx=5, pady=5)
frame_green.pack(expand=YES, fill=BOTH)

# Внутри него жёлтый
frame_yellow = Frame(frame_green, bg='blue', padx=5, pady=5)
frame_yellow.pack(expand=YES, fill=BOTH)


t = StringVar()
# переменная которая хранит текст
t.set('Я кст Хорайзон всем хао')
label = Label(frame_green, textvariable=t, width=20, height=5, bg='white')

label.pack()
root.mainloop()

# второй скрипт для того чтобы после выхода и3 1-го окна сразу открылось 2-ое
from tkinter import *

def show():
    print("Количество:", qty.get())
    print("Красный:", red.get())
    print("Синий:", blue.get())
    print("Зелёный:", green.get())
    print("Жёлтый:", yellow.get())

root = Tk()
root.title("Выбор")
root.geometry("300x400")

# Количество (радиокнопки)
Label(text="Сколько штук?").pack()
qty = StringVar(value="0-10")
# Переменная которая хранит строку и автоматически связывается с виджетами

# Все такие радиокнопки связаны с переменной qty
Radiobutton(text="0-10", variable=qty, value="0-10").pack()
Radiobutton(text="11-20", variable=qty, value="11-20").pack()
Radiobutton(text="21-30", variable=qty, value="21-30").pack()
Radiobutton(text="31-40", variable=qty, value="31-40").pack()

# переменные хранят true или false (выбран флажок или нет)
Label(text="Какого цвета?").pack(pady=10)
red = BooleanVar()
blue = BooleanVar()
green = BooleanVar()
yellow = BooleanVar()

# и сами флажки
Checkbutton(text="RED", variable=red).pack()
Checkbutton(text="BLUE", variable=blue).pack()
Checkbutton(text="GREEN", variable=green).pack()
Checkbutton(text="YELLOW", variable=yellow).pack()
Button(text="Показать выбор", command=show).pack(pady=10)
Button(text="Выход", command=root.destroy).pack()

frame_violet = Frame(root, bg='red', padx=5, pady=5)
frame_violet.pack(expand=YES, fill=BOTH)

frame_blue = Frame(frame_violet, bg='blue', padx=5, pady=5)
frame_blue.pack(expand=YES, fill=BOTH)

frame_cyan = Frame(frame_blue, bg='green', padx=5, pady=5)
frame_cyan.pack(expand=YES, fill=BOTH)

frame_green = Frame(frame_cyan, bg='yellow', padx=5, pady=5)
frame_green.pack(expand=YES, fill=BOTH)

root.mainloop()

