# -*- coding: utf-8 -*-
import sys
import re
import mysql.connector
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtCore import Qt

# Импортируем UI классы
from avt import Ui_Widget as AvtUI
from glav import Ui_Widget as GlavUI
from regi import Ui_Widget as RegiUI
from cards import CardsWindow


# Функции для работы с БД
def get_connection():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            database='horizon',
            user='root',
            port=3306,
            password=''
        )
        return conn
    except Exception as e:
        print(f"Ошибка БД: {e}")
        return None


def register_user(login, password):
    # Проверка логина (только латинские буквы)
    if not re.match(r'^[a-zA-Z]+$', login):
        return False, "Логин должен содержать только латинские буквы"

    # Проверка пароля (от 6 символов, латиница и цифры)
    if not re.match(r'^[a-zA-Z0-9]{6,}$', password):
        return False, "Пароль должен содержать от 6 символов (латинские буквы и цифры)"

    conn = get_connection()
    if not conn:
        return False, "Ошибка подключения к БД. Запустите MySQL."

    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM guys WHERE login = %s', (login,))
        if cursor.fetchone():
            cursor.close()
            conn.close()
            return False, "Пользователь с таким логином уже существует"

        cursor.execute('INSERT INTO guys (login, parol) VALUES (%s, %s)', (login, password))
        conn.commit()
        cursor.close()
        conn.close()
        return True, "Регистрация успешна!"
    except Exception as e:
        return False, f"Ошибка: {e}"


def auth_user(login, password):
    conn = get_connection()
    if not conn:
        return False, "Ошибка подключения к БД. Запустите MySQL."

    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM guys WHERE login = %s AND parol = %s', (login, password))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        if user:
            return True, "Авторизация успешна!"
        else:
            return False, "Неверный логин или пароль"
    except Exception as e:
        return False, f"Ошибка: {e}"


# Класс главного окна (выбор авторизация/регистрация)
class GlavWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = GlavUI()
        self.ui.setupUi(self)
        self.setWindowTitle("Главное меню")

        # Подключаем кнопки
        self.ui.pushButton.clicked.connect(self.open_auth)
        self.ui.pushButton_2.clicked.connect(self.open_reg)
        self.ui.pushButton_3.clicked.connect(self.close_app)

    def open_auth(self):
        self.auth_window = AuthWindow()
        self.auth_window.show()
        self.hide()

    def open_reg(self):
        self.reg_window = RegWindow()
        self.reg_window.show()
        self.hide()

    def close_app(self):
        self.close()


# Класс окна авторизации
class AuthWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = AvtUI()
        self.ui.setupUi(self)
        self.setWindowTitle("Авторизация")

        # Подключаем кнопки
        self.ui.pushButton.clicked.connect(self.login)
        self.ui.pushButton_2.clicked.connect(self.back_to_glav)

    def login(self):
        login = self.ui.lineEdit_2.text()  # логин
        password = self.ui.lineEdit.text()  # пароль

        if not login or not password:
            QMessageBox.warning(self, "Ошибка", "Введите логин и пароль")
            return

        success, message = auth_user(login, password)
        if success:
            QMessageBox.information(self, "Успех", f"Добро пожаловать, {login}!")
            # Открываем окно с карточками
            self.cards_window = CardsWindow(login)
            self.cards_window.show()
            self.close()
        else:
            QMessageBox.warning(self, "Ошибка", message)

    def back_to_glav(self):
        self.glav_window = GlavWindow()
        self.glav_window.show()
        self.close()


# Класс окна регистрации
class RegWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = RegiUI()
        self.ui.setupUi(self)
        self.setWindowTitle("Регистрация")

        # Подключаем кнопки
        self.ui.pushButton.clicked.connect(self.register)
        self.ui.pushButton_2.clicked.connect(self.back_to_glav)

    def register(self):
        login = self.ui.lineEdit_2.text()  # логин
        password = self.ui.lineEdit.text()  # пароль

        if not login or not password:
            QMessageBox.warning(self, "Ошибка", "Заполните все поля")
            return

        success, message = register_user(login, password)
        if success:
            QMessageBox.information(self, "Успех", message)
            # После регистрации открываем карточки
            self.cards_window = CardsWindow(login)
            self.cards_window.show()
            self.close()
        else:
            QMessageBox.warning(self, "Ошибка", message)

    def back_to_glav(self):
        self.glav_window = GlavWindow()
        self.glav_window.show()
        self.close()


# Запуск приложения
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GlavWindow()
    window.show()
    sys.exit(app.exec_())