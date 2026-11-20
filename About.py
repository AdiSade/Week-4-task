from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtGui import QPixmap


class About(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('About')
        self.resize(340, 460)

        self.my_picture = QLabel(self)
        self.my_picture.setGeometry(70, 20, 200, 200)
        image = QPixmap('images.jpg').scaled(200, 200)
        self.my_picture.setPixmap(image)

        self.my_name = QLabel('YOUR NAME', self)
        self.my_name.setGeometry(20, 240, 300, 30)
        self.my_name.setObjectName("title")

        self.my_email = QLabel('your.email@gmail.com', self)
        self.my_email.setGeometry(20, 280, 300, 30)

        self.my_linkedin = QLabel('<a href="https://www.linkedin.com/in/YOUR-PROFILE/">My LinkedIn page</a>', self)
        self.my_linkedin.setGeometry(20, 320, 300, 30)
        self.my_linkedin.setOpenExternalLinks(True)

        self.my_github = QLabel('<a href="https://github.com/YOUR-USER/YOUR-REPO">GitHub repository</a>', self)
        self.my_github.setGeometry(20, 360, 300, 30)
        self.my_github.setOpenExternalLinks(True)

        with open('style.qss', 'r') as f:
            self.setStyleSheet(f.read())


if __name__ == '__main__':
    app = QApplication()
    window = About()
    window.show()
    app.exec()