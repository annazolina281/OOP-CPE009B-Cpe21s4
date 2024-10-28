import sys
import math
from PyQt5.QtWidgets import (QMainWindow, QWidget, QGridLayout,
                             QLineEdit, QPushButton, QApplication,
                             QAction, QFileDialog, QMessageBox)


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(300, 300, 400, 400)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.grid = QGridLayout(self.central_widget)
        self.display = QLineEdit(self)
        self.grid.addWidget(self.display, 0, 0, 1, 4)

        self.create_buttons()
        self.create_menu()

    def create_buttons(self):
        names = [
            '7', '8', '9', '/', '',
            '4', '5', '6', '*', '',
            '1', '2', '3', '-', '',
            '0', '.', '=', '+', '',
            'C', 'sin', 'cos', 'tan', ''
        ]

        positions = [(i, j) for i in range(1, 6) for j in range(5)]

        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton(name)
            button.clicked.connect(lambda checked, n=name: self.on_button_click(n))
            self.grid.addWidget(button, *position)

    def create_menu(self):
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('File')

        save_action = QAction('Save', self)
        save_action.triggered.connect(self.save_to_file)
        file_menu.addAction(save_action)

        load_action = QAction('Load', self)
        load_action.triggered.connect(self.load_from_file)
        file_menu.addAction(load_action)

        exit_action = QAction('Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

    def on_button_click(self, button_text):
        if button_text == '=':
            try:
                # Evaluate arithmetic expressions
                result = eval(self.display.text())
                self.display.setText(str(result))
                self.save_operation(f"{self.display.text()} = {result}")
            except Exception:
                QMessageBox.warning(self, "Error", "Invalid Input!")
        elif button_text == 'C':
            self.display.clear()
        elif button_text in ('sin', 'cos', 'tan'):
            try:
                angle = float(self.display.text())
                if button_text == 'sin':
                    result = math.sin(math.radians(angle))
                elif button_text == 'cos':
                    result = math.cos(math.radians(angle))
                elif button_text == 'tan':
                    result = math.tan(math.radians(angle))
                self.display.setText(f"{button_text}({angle}) = {result:.2f}")
                self.save_operation(f"{button_text}({angle}) = {result:.2f}")
            except ValueError:
                QMessageBox.warning(self, "Error", "Invalid Input for Trigonometric Function!")
        else:
            current_text = self.display.text()
            self.display.setText(current_text + button_text)

    def save_to_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);; All Files (*)",
                                                   options=options)
        if file_name:
            with open(file_name, 'w') as f:
                f.write(self.display.text())

    def load_from_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);; All Files (*)",
                                                   options=options)
        if file_name:
            with open(file_name, 'r') as f:
                data = f.read()
                self.display.setText(data)

    def save_operation(self, operation):
        with open("operations.txt", 'a') as f:
            f.write(operation + '\n')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
