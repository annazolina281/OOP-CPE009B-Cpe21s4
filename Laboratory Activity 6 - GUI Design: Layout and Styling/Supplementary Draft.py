import sys
import math
from PyQt5.QtWidgets import (
    QGridLayout, QLineEdit, QPushButton, QWidget, QApplication,
    QMenuBar, QAction, QMessageBox
)


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.filename = 'calculator_history.txt'

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        self.textLine = QLineEdit(self)
        grid.addWidget(self.textLine, 0, 0, 1, 5)

        names = [
            '7', '8', '9', '/', 'C',
            '4', '5', '6', '*', 'sin',
            '1', '2', '3', '-', 'cos',
            '0', '.', '=', '+', '**'
        ]

        positions = [(i, j) for i in range(1, 5) for j in range(5)]
        for position, name in zip(positions, names):
            button = QPushButton(name)
            grid.addWidget(button, *position)
            button.clicked.connect(self.on_button_click)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Calculator')

        self.create_menu()
        self.show()

    def create_menu(self):
        menubar = QMenuBar(self)
        file_menu = menubar.addMenu('File')

        exit_action = QAction('Exit', self)
        exit_action.triggered.connect(self.close)
        exit_action.setShortcut('Ctrl+Q')
        file_menu.addAction(exit_action)

        self.layout().setMenuBar(menubar)

    def on_button_click(self):
        sender = self.sender()
        text = sender.text()

        if text == 'C':
            self.textLine.clear()
        elif text == '=':
            self.calculate_result()
        elif text in ['sin', 'cos']:
            self.perform_function(text)
        else:
            self.textLine.setText(self.textLine.text() + text)

    def calculate_result(self):
        try:
            expression = self.textLine.text()
            result = eval(expression)
            self.textLine.setText(str(result))
            self.save_to_file(f"{expression} = {result}")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def perform_function(self, func):
        try:
            value = float(self.textLine.text())
            if func == 'sin':
                result = math.sin(math.radians(value))
            elif func == 'cos':
                result = math.cos(math.radians(value))
            self.textLine.setText(str(result))
            self.save_to_file(f"{func}({value}) = {result}")
        except ValueError:
            QMessageBox.critical(self, "Error", "Invalid input for function.")

    def save_to_file(self, operation):
        with open(self.filename, 'a') as file:
            file.write(operation + '\n')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    sys.exit(app.exec_())
