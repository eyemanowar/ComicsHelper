from PyQt6.QtCore import QSize, Qt, QDir
from PyQt6 import QtGui
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
import sys


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        

        self.setWindowTitle("My App")
        self.button = QPushButton("Press Me!")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.the_button_was_clicked)
        # button.clicked.connect(self.the_button_was_toggled)
        
        self.setFixedSize(QSize(600, 600))

        # Set the central widget of the Window.
        self.button.clicked.connect(self.getfiles)
        self.setCentralWidget(self.button)
    
    def the_button_was_clicked(self):
        print("clicked")
        self.button.setText("you clicked med already")
        self.button.setCheckable(False)
        
        self.setWindowTitle("my oneshot app")
        
    # def the_button_was_toggled(self, checked):
    #     print("checked", checked)
    
    def getfiles(self):
        fileName, _ = QFileDialog.getOpenFileName(self, 'Single File', QDir.rootPath() , '*.xlsm')
        testtt = QFileDialog.
        self.ui.lineEdit.setText(fileName)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

# Start the event loop.
app.exec()