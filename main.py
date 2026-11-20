import os
import sys
import subprocess
from PySide6.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit,
                               QTableWidget, QTableWidgetItem, QFileDialog)
from PySide6.QtGui import QIntValidator
from About import About


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.about_window = About()
        self.setWindowTitle("Grades Fixer")
        self.resize(520, 510)

        self.student_ids = []
        self.original_grades = []
        self.corrected_grades = []
        self.selected_file = ''

        self.load_button = QPushButton("Load File", self)
        self.load_button.setGeometry(20, 20, 150, 30)
        self.load_button.clicked.connect(self.load_file)

        self.table = QTableWidget(50, 3, self)
        self.table.setGeometry(20, 70, 480, 360)
        self.table.setHorizontalHeaderLabels(["ID", "Grades Original", "Corrected Grades"])
        self.table.setColumnWidth(0, 130)
        self.table.setColumnWidth(1, 130)
        self.table.setColumnWidth(2, 130)
        self.bonus_label = QLabel("Bonus points:", self)
        self.bonus_label.setGeometry(20, 450, 100, 30)

        self.bonus_input = QLineEdit("", self)
        self.bonus_input.setGeometry(130, 450, 100, 30)
        self.bonus_input.setValidator(QIntValidator())
        self.bonus_input.returnPressed.connect(self.add_bonus)
        self.update_button = QPushButton("File Update", self)
        self.update_button.setGeometry(250, 450, 120, 30)
        self.update_button.clicked.connect(self.update_file)
        self.about_button = QPushButton("About", self)
        self.about_button.setGeometry(380, 450, 120, 30)
        self.about_button.clicked.connect(self.show_about_window)    

        with open("style.qss", "r") as f:
            self.setStyleSheet(f.read())

    def load_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Choose students file", "", "CSV files (*.csv)")
        if file_name == "":
            return
        self.selected_file = file_name
        with open(self.selected_file, 'r') as f:
            header = next(f)
            for student in f:
                student = student.strip()
                if student == '':
                    return
                data = student.split(',')
                id = data[0]
                grade = int(data[1])
                self.student_ids.append(id)
                self.original_grades.append(grade)
                self.corrected_grades.append(grade)
        self.update_table()

    def update_table(self):
        for row in range(len(self.student_ids)):
            self.table.setItem(row, 0, QTableWidgetItem(str(self.student_ids[row])))
            self.table.setItem(row, 1, QTableWidgetItem(str(self.original_grades[row])))
            self.table.setItem(row, 2, QTableWidgetItem(str(self.corrected_grades[row])))

    def add_bonus(self):
        # TODO: read the number from self.bonus_input
        # TODO: corrected grade = original + bonus, but not more than 100
        # TODO: call self.update_table()
        pass

    def update_file(self):
        # TODO: overwrite self.selected_file with the corrected grades
        #       (keep the original headers and format)
        # TODO: at the end call self.open_file(self.selected_file)
        pass
        
        
    def open_file(self, path):
        # opens the file with the default program, works on Windows / Mac / Linux
        if sys.platform.startswith("win"):
            os.startfile(path)
        elif sys.platform == "darwin":
            subprocess.run(["open", path])
        else:
            subprocess.run(["xdg-open", path])

    def show_about_window(self):
        self.about_window.show()

if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()