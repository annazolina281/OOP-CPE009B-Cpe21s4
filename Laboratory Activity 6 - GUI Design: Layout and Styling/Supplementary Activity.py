import sys
from PyQt5.QtWidgets import (
    QWidget, QGridLayout, QLineEdit, QPushButton, QVBoxLayout, QApplication,
    QMainWindow, QAction, QFileDialog, QTextEdit, QMenuBar
)
from PyQt5.QtGui import QIcon
import math

class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(300, 300, 400, 400)
        self.initUI()

    def initUI(self):
        mainWidget = QWidget(self)
        mainLayout = QVBoxLayout()

        # Display
        self.textLine = QLineEdit(self)
        mainLayout.addWidget(self.textLine)

        # Grid Layout for buttons
        grid = QGridLayout()
        mainLayout.addLayout(grid)

        # Button names
        names = [
            '7', '8', '9', '/', 'sin',
            '4', '5', '6', '*', 'cos',
            '1', '2', '3', '-', '^',
            '0', '.', '=', '+', 'C'
        ]

        # Add buttons to grid
        positions = [(i, j) for i in range(5) for j in range(5)]
        for position, name in zip(positions, names):
            button = QPushButton(name)
            button.clicked.connect(self.onButtonClick)
            grid.addWidget(button, *position)

        # Text area for calculations
        self.calculations = QTextEdit()
        mainLayout.addWidget(self.calculations)

        # Set main layout
        mainWidget.setLayout(mainLayout)
        self.setCentralWidget(mainWidget)

        # Menu
        self.createMenu()

    def createMenu(self):
        mainMenu = QMenuBar(self)

        # File menu
        fileMenu = mainMenu.addMenu('File')

        # Save action
        saveAction = QAction('Save Calculations', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.triggered.connect(self.saveCalculations)
        fileMenu.addAction(saveAction)

        # Open action
        openAction = QAction('Open Calculations', self)
        openAction.setShortcut('Ctrl+O')
        openAction.triggered.connect(self.openCalculations)
        fileMenu.addAction(openAction)

        # Clear action
        clearAction = QAction('Clear Calculations', self)
        clearAction.setShortcut('Ctrl+M')
        clearAction.triggered.connect(self.clearCalculations)
        fileMenu.addAction(clearAction)

        # Exit action
        exitAction = QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(self.close)
        fileMenu.addAction(exitAction)

        self.setMenuBar(mainMenu)

    def keyPressEvent(self, event):
        key = event.text()
        if key in '0123456789.+-*/':
            self.textLine.setText(self.textLine.text() + key)
        elif key == '=':
            self.evaluateExpression()
        elif key.lower() == 'c':
            self.clearCalculations()  # Calls the clear function
        elif key == '^':
            self.textLine.setText(self.textLine.text() + '**')

    def onButtonClick(self):
        sender = self.sender()
        button_text = sender.text()

        if button_text == 'C':
            # Clear the input field
            self.clearCalculations()  # Calls the clear function
        elif button_text == '=':
            self.evaluateExpression()
        elif button_text == 'sin':
            self.calculateTrig('sin')
        elif button_text == 'cos':
            self.calculateTrig('cos')
        elif button_text == '^':
            # Append exponentiation symbol for power operation
            current_text = self.textLine.text()
            self.textLine.setText(current_text + '**')
        else:
            # Append the button text to the current input
            current_text = self.textLine.text()
            self.textLine.setText(current_text + button_text)

    def evaluateExpression(self):
        # Calculate and display result
        expression = self.textLine.text()
        expression = expression.replace("^", "**")
        try:
            result = str(eval(expression))  # Direct calculation
            self.textLine.setText(result)
            self.calculations.append(f"{expression} = {result}")
        except:
            self.textLine.setText("Error")  # Display error for invalid expressions

    def calculateTrig(self, func):
        # Calculate trigonometric function in degrees
        expression = self.textLine.text()
        try:
            value = float(expression)
            if func == 'sin':
                result = str(math.sin(math.radians(value)))
                self.calculations.append(f"sin({expression}) = {result}")
            elif func == 'cos':
                result = str(math.cos(math.radians(value)))
                self.calculations.append(f"cos({expression}) = {result}")
            self.textLine.setText(result)
        except ValueError:
            self.textLine.setText("Error")  # Handle invalid input for trig functions

    def saveCalculations(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self, "Save Calculations", "", "Text Files (*.txt)", options=options)
        if fileName:
            with open(fileName, 'w') as file:
                file.write(self.calculations.toPlainText())

    def openCalculations(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Calculations", "", "Text Files (*.txt)", options=options)
        if fileName:
            with open(fileName, 'r') as file:
                data = file.read()
                self.calculations.setText(data)

    def clearCalculations(self):
        self.textLine.clear()  # Clear the input field
        self.calculations.clear()  # Clear the calculations text area

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = CalculatorApp()
    calculator.show()
    sys.exit(app.exec_())
