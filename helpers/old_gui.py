import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout,
    QWidget, QFileDialog, QMessageBox, QHBoxLayout
)
from helpers.file_crawlers import FileCrawler


class ComicsHelperApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Comics Helper")
        self.setFixedSize(500, 250)
        self.file_crawler = FileCrawler()
        self.week_folder = None

        self.layout = QVBoxLayout()

        self.folder_label = QLabel("Select a folder for this week's comics:")
        self.layout.addWidget(self.folder_label)

        self.select_folder_button = QPushButton("Select Folder")
        self.select_folder_button.clicked.connect(self.select_folder)
        self.layout.addWidget(self.select_folder_button)

        self.sort_button = QPushButton("Sort Comics")
        self.sort_button.setEnabled(False)
        self.sort_button.clicked.connect(self.sort_comics)
        self.layout.addWidget(self.sort_button)

        self.open_buttons_layout = QHBoxLayout()
        self.standalone_button = QPushButton("Open Standalone Folder")
        self.standalone_button.clicked.connect(self.open_standalone_folder)

        self.first_issues_button = QPushButton("Open First Issues Folder")
        self.first_issues_button.clicked.connect(self.open_first_issues_folder)

        self.sorted_button = QPushButton("Open Sorted Folder")
        self.sorted_button.clicked.connect(self.open_sorted_folder)

        self.open_buttons_layout.addWidget(self.standalone_button)
        self.open_buttons_layout.addWidget(self.first_issues_button)
        self.open_buttons_layout.addWidget(self.sorted_button)

        self.open_buttons_widget = QWidget()
        self.open_buttons_widget.setLayout(self.open_buttons_layout)
        self.open_buttons_widget.setVisible(False)
        self.layout.addWidget(self.open_buttons_widget)

        self.confirm_button = QPushButton("Confirm and Add to Database")
        self.confirm_button.clicked.connect(self.confirm_and_restart)
        self.confirm_button.setVisible(False)
        self.layout.addWidget(self.confirm_button)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Week Folder")
        if folder:
            self.week_folder = folder
            QMessageBox.information(self, "Folder Selected", f"Selected folder: {self.week_folder}")
            self.sort_button.setEnabled(True)

    def sort_comics(self):
        if not self.week_folder:
            QMessageBox.critical(self, "Error", "Please select a folder first.")
            return
        self.file_crawler.sorted_comics(self.week_folder)
        QMessageBox.information(self, "Success", "Comics sorted successfully!")

        self.open_buttons_widget.setVisible(True)
        self.confirm_button.setVisible(True)

    def confirm_and_restart(self):
        reply = QMessageBox.question(
            self,
            "Confirmation",
            "Have you checked standalone and first issues?",
            QMessageBox.Yes | QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            self.file_crawler.add_new_comics_to_reading_list()
            QMessageBox.information(self, "Done", "This week's comics are added to the database!")

            restart_reply = QMessageBox.question(
                self,
                "Restart",
                "Do you want to start again?",
                QMessageBox.Yes | QMessageBox.No
            )
            if restart_reply == QMessageBox.Yes:
                self.reset_app()
            else:
                self.close()
        else:
            QMessageBox.warning(self, "Warning", "Please check standalone and first issues first.")

    def reset_app(self):
        self.week_folder = None
        self.sort_button.setEnabled(False)
        self.open_buttons_widget.setVisible(False)
        self.confirm_button.setVisible(False)

    def open_standalone_folder(self):
        self.open_folder(self.file_crawler.standalone_issues_folder)

    def open_first_issues_folder(self):
        self.open_folder(self.file_crawler.first_issues_folder)

    def open_sorted_folder(self):
        self.open_folder(self.file_crawler.week_folder)

    def open_folder(self, folder_path):
        if os.path.exists(folder_path):
            os.system(f'open "{folder_path}"')  # macOS-specific
        else:
            QMessageBox.critical(self, "Error", f"The folder '{folder_path}' does not exist.")


def run():
    app = QApplication(sys.argv)
    window = ComicsHelperApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    run()