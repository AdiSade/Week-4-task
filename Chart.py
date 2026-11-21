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

        self.draw_chart(0, 0)

    def draw_chart(self, pass_before, pass_after):
        self.ax.clear()
        self.ax.bar(["passed before update", "passed after update"], [pass_before, pass_after], color=["yellow", "green"])
        self.ax.set_title("passed graph")
        self.ax.set_ylabel("chart for numbers")
        self.canvas.draw() 
        


if __name__ == '__main__':
    app = QApplication()
    window = Chart()
    window.show()
    app.exec()