from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QGridLayout
from PyQt6.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Sigma Chislovod")
        self.setFixedSize(300, 400)

        self.display = QLineEdit(self)
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setStyleSheet("""
            font-size: 24px;
            padding: 10px;
            border: 2px solid #ccc;
            border-radius: 5px;
            background-color: #f9f9f9;
        """)

        buttons = [
            'C', '←', 'CE', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '.', '=', '%'
        ]

        grid = QGridLayout()
        grid.addWidget(self.display, 0, 0, 1, 4)

        positions = [(i // 4 + 1, i % 4) for i in range(len(buttons))]
        for position, button_text in zip(positions, buttons):
            button = QPushButton(button_text)
            button.setStyleSheet("""
                QPushButton {
                    font-size: 18px;
                    padding: 15px;
                    border: 2px solid #ccc;
                    border-radius: 5px;
                    background-color: #e0e0e0;
                }
                QPushButton:hover {
                    background-color: #d0d0d0;
                }
                QPushButton:pressed {
                    background-color: #b0b0b0;
                }
            """)
            if button_text == 'C' or button_text == 'CE':
                button.clicked.connect(self.clear_display)
            elif button_text == '←':
                button.clicked.connect(self.backspace)
            elif button_text == '=':
                button.clicked.connect(self.calculate)
            else:
                button.clicked.connect(self.on_button_click)
            grid.addWidget(button, *position)

        self.setLayout(grid)

    def on_button_click(self):
        button = self.sender()
        text = button.text()
        self.display.setText(self.display.text() + text)

    def clear_display(self):
        self.display.clear()

    def backspace(self):
        current_text = self.display.text()
        self.display.setText(current_text[:-1])

    def calculate(self):
        try:
            result = str(eval(self.display.text()))
            self.display.setText(result)
        except ZeroDivisionError:
            self.display.setText("Ошибка: деление на ноль")
        except Exception:
            self.display.setText("Ошибка")

app = QApplication([])
calc = Calculator()
calc.show()
app.exec()