import sys
import threading
import time

from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit, QLineEdit, QGridLayout


class Example(QWidget):
    def initUI(self, q, q2):

        def get_text():
            while True:
                if q2.empty():
                    time.sleep(0.05)
                else:
                    text_box.insertPlainText(q2.get())

        def click():
                q.put(input_line.text())
                input_line.clear()

        text_box = QTextEdit()
        text_box.setReadOnly(True)

        input_line = QLineEdit()
        input_line.returnPressed.connect(click)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(text_box, 1, 0)
        grid.addWidget(input_line, 2, 0)

        self.setLayout(grid)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Messenger v0.1')
        self.show()

        t_text = threading.Thread(target=get_text, name='t_text', )
        t_text.start()

    def __init__(self, q, q2):
        super().__init__()

        self.initUI(q, q2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
