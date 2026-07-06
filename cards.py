# -*- coding: utf-8 -*-
import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QSize


class CardsWindow(QWidget):
    def __init__(self, login, parent=None):
        super().__init__(parent)
        self.login = login
        self.setWindowTitle(f"Карточки товаров - {login}")
        self.setGeometry(100, 100, 900, 700)

        # Виджеты
        self.list_widget = QListWidget()
        self.search_field = QLineEdit()
        self.search_field.setPlaceholderText("Поиск товаров...")

        self.back_button = QPushButton("Назад в главное меню")
        self.close_button = QPushButton("Закрыть")

        # Область прокрутки
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidget(self.list_widget)
        self.scroll_area.setWidgetResizable(True)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.scroll_area)
        layout.addWidget(self.search_field)
        layout.addWidget(self.back_button)
        layout.addWidget(self.close_button)
        self.setLayout(layout)

        # Подключаем сигналы
        self.search_field.textChanged.connect(self.filter_items)
        self.back_button.clicked.connect(self.back_to_glav)
        self.close_button.clicked.connect(self.close)

        # Создаём данные и карточки
        self.create_products()
        self.create_card()

    def create_products(self):
        self.products = [
            ("Ноутбук Lenovo", "Мощный ноутбук для работы", "images/lenovo.png"),
            ("Смартфон iPhone", "Новейший iPhone", "images/iphone.png"),
            ("Наушники Sony", "Беспроводные наушники", "images/sony.png"),
            ("Мышь Logitech", "Игровая мышь", "images/logitech.png"),
            ("Клавиатура", "Механическая клавиатура", "images/keyboard.png"),
            ("Монитор Samsung", "4K монитор", "images/samsung.png"),
            ("Внешний диск", "1TB SSD", "images/ssd.png"),
            ("Веб-камера", "4K веб-камера", "images/camera.png"),
            ("Планшет iPad", "10 дюймов", "images/ipad.png"),
            ("Принтер HP", "Лазерный принтер", "images/printer.png"),
        ]

    def create_card(self):
        for name, desc, img in self.products:
            # Проверяем, существует ли картинка
            if os.path.exists(img):
                pixmap = QPixmap(img)
                icon = QIcon(pixmap) if not pixmap.isNull() else QIcon()
            else:
                icon = QIcon()
                print(f"Картинка не найдена: {img}")

            item = QListWidgetItem(icon, f"{name}\n{desc}")
            self.list_widget.addItem(item)

        self.list_widget.setIconSize(QSize(80, 80))
        self.list_widget.setResizeMode(QListWidget.Adjust)

    def filter_items(self, text):
        """Фильтрация карточек по тексту поиска"""
        if not text:
            for i in range(self.list_widget.count()):
                self.list_widget.item(i).setHidden(False)
            return

        search_text = text.lower()
        for i in range(self.list_widget.count()):
            item = self.list_widget.item(i)
            item_text = item.text().lower()
            item.setHidden(search_text not in item_text)

    def back_to_glav(self):
        """Возврат в главное меню"""
        from glav import Ui_Widget as GlavUI
        self.glav_window = QWidget()
        self.glav_window.setWindowTitle("Главное меню")
        self.glav_window.resize(800, 600)
        self.glav_window.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CardsWindow("guest")
    window.show()
    sys.exit(app.exec_())