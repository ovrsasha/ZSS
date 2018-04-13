import queue

from client import *
from gui import *


class Main(object):
    def __init__(self):

        q = queue.Queue() # Отправка из GUI
        q2 = queue.Queue() # отправка в GUI

        def client(q, q2):
            ex_client = Client(q, q2)

        def gui(q, q2):
            app = QApplication(sys.argv)
            ex = Example(q, q2)
            sys.exit(app.exec_())

        t_client = threading.Thread(target=client, name='t_client', args=(q, q2))
        t_client.start()

        t_gui = threading.Thread(target=gui, name='t_gui', args=(q, q2))
        t_gui.start()


if __name__ == '__main__':
    ex_main = Main()
