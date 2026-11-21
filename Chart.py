from PySide6.QtWidgets import QApplication, QWidget
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class Chart(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pass / Fail Chart")
        self.resize(600, 480)

        self.figure = Figure()
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.canvas.setParent(self)
        self.canvas.setGeometry(20, 20, 560, 440)

        with open('style.qss', 'r') as f:
            self.setStyleSheet(f.read())

        self.draw_chart(0, 0, 0, 0)

    def draw_chart(self, pass_before, pass_after, fail_before, fail_after):
        # temporary chart - you will replace the content of this method
        self.ax.clear()
        self.ax.bar(["a", "b"], [1, 2])
        self.canvas.draw()


if __name__ == '__main__':
    app = QApplication()
    window = Chart()
    window.show()
    app.exec()