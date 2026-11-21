import os
import sys
import subprocess
from PySide6.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit,
                               QTableWidget, QTableWidgetItem, QFileDialog)
from PySide6.QtGui import QIntValidator
from About import About
from Chart import Chart


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.about_window = About()
        self.chart_window = Chart()
        self.setWindowTitle("Grades Fixer")
        self.resize(520, 510)

        self.student_ids = []
        self.original_grades = []
        self.corrected_grades = []
        self.selected_file = ''
        self.pass_grade = 60

        self.load_button = QPushButton("Load File", self)
        self.load_button.setGeometry(20, 20, 150, 30)
        self.load_button.clicked.connect(self.load_file)
        self.chart_button = QPushButton("Pass Chart", self)
        self.chart_button.setGeometry(190, 20, 150, 30)
        self.chart_button.clicked.connect(self.show_chart)

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
        self.student_ids.clear()
        self.original_grades.clear()
        self.corrected_grades.clear()
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
        bonus_val = self.bonus_input.text()
        if bonus_val == "":
            return
        bonus_val = int(bonus_val)
        if bonus_val <= 0:
            bonus_val = bonus_val*(-1)
        for i in range(len(self.original_grades)):
            new_grade = self.original_grades[i] + bonus_val
            new_grade = min(new_grade, 100)
            self.corrected_grades[i] = new_grade
        self.update_table()

    def update_file(self):
        if self.selected_file == "":
            return
        with open(self.selected_file, 'r') as f:
            header = next(f)
        backup_name = self.selected_file.replace('.csv', '_backup.csv')
        with open(backup_name, "w") as f:
            f.write(header)
            for j in range(len(self.student_ids)):
                f.write(f"{self.student_ids[j]},{self.original_grades[j]}\n")
        with open(self.selected_file, 'w') as f:
            f.write(header)
            for j in range(len(self.student_ids)):
                f.write(f"{self.student_ids[j]},{self.corrected_grades[j]}\n")
        self.open_file(self.selected_file)
        
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

    def show_chart(self):
        if self.selected_file == "":
            return
        # TODO: count how many passed / failed in the original grades
        # TODO: count how many passed / failed in the corrected grades
        # TODO: call self.chart_window.draw_chart(pass_before, pass_after, fail_before, fail_after)
        self.chart_window.show()

if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()