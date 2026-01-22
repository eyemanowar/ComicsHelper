from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QPushButton, QFileDialog, QMessageBox, QWidget, QHBoxLayout
)
import os
from helpers.file_crawlers import FileCrawler


class ComicsHelperApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Comics Helper")
        self.file_crawler = FileCrawler()
        self.week_folder = None

        # Main layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Folder selection
        self.select_folder_button = QPushButton("Select Folder")
        self.select_folder_button.clicked.connect(self.select_folder)
        self.layout.addWidget(self.select_folder_button)

        # Sort comics button
        self.sort_button = QPushButton("Sort Comics")
        self.sort_button.setEnabled(False)
        self.sort_button.clicked.connect(self.sort_comics)
        self.layout.addWidget(self.sort_button)

        # Folder buttons (hidden initially)
        self.folder_buttons_layout = QHBoxLayout()
        self.standalone_button = QPushButton("Open Standalone Folder")
        self.standalone_button.clicked.connect(self.open_standalone_folder)
        self.first_issues_button = QPushButton("Open First Issues Folder")
        self.first_issues_button.clicked.connect(self.open_first_issues_folder)
        self.sorted_button = QPushButton("Open Sorted Folder")
        self.sorted_button.clicked.connect(self.open_sorted_folder)

        self.folder_buttons_layout.addWidget(self.standalone_button)
        self.folder_buttons_layout.addWidget(self.first_issues_button)
        self.folder_buttons_layout.addWidget(self.sorted_button)
        self.layout.addLayout(self.folder_buttons_layout)

        # Hide folder buttons initially
        self.standalone_button.hide()
        self.first_issues_button.hide()
        self.sorted_button.hide()

    def select_folder(self):
        self.week_folder = QFileDialog.getExistingDirectory(self, "Select Week Folder")
        if self.week_folder:
            if not os.access(self.week_folder, os.R_OK | os.W_OK):
                QMessageBox.critical(self, "Permission Denied",
                                     f"Cannot access the folder: {self.week_folder}. Please grant the necessary permissions.")
                self.week_folder = None
                return
            QMessageBox.information(self, "Folder Selected", f"Selected folder: {self.week_folder}")
            self.sort_button.setEnabled(True)

    def sort_comics(self):
        if not self.week_folder:
            QMessageBox.critical(self, "Error", "Please select a folder first.")
            return

        if not os.path.exists(self.week_folder):
            QMessageBox.critical(self, "Error", f"The folder '{self.week_folder}' does not exist.")
            return

        try:
            # Attempt to sort comics
            self.file_crawler.sorted_comics(self.week_folder)

            # Check access to sorted folder
            sorted_folder = self.file_crawler.week_folder
            if not os.access(sorted_folder, os.R_OK | os.W_OK):
                QMessageBox.critical(self, "Permission Denied", f"Cannot access the sorted folder: {sorted_folder}.")
                return

            QMessageBox.information(self, "Success", "Comics sorted successfully!")

            # Show folder buttons
            self.standalone_button.show()
            self.first_issues_button.show()
            self.sorted_button.show()

            # Enable confirmation step
            self.confirm_button = QPushButton("Confirm and Add to Database")
            self.confirm_button.clicked.connect(self.confirm_and_restart)
            self.layout.addWidget(self.confirm_button)

        except Exception as e:
            print(f"Error during sorting: {e}")
            QMessageBox.critical(self, "Error", f"An error occurred while sorting comics: {e}")

    def confirm_and_restart(self):
        answer = QMessageBox.question(
            self, "Confirmation", "Have you checked standalone and first issues?",
            QMessageBox.Yes | QMessageBox.No
        )
        if answer == QMessageBox.Yes:
            self.file_crawler.add_new_comics_to_reading_list()
            QMessageBox.information(self, "Done", "This week's comics are added to the database!")
            restart = QMessageBox.question(self, "Restart", "Do you want to start again?", QMessageBox.Yes | QMessageBox.No)
            if restart == QMessageBox.Yes:
                self.reset_app()
            else:
                self.close()
        else:
            QMessageBox.warning(self, "Warning", "Please check standalone and first issues first.")

    def reset_app(self):
        self.week_folder = None
        self.sort_button.setEnabled(False)
        self.standalone_button.hide()
        self.first_issues_button.hide()
        self.sorted_button.hide()
        if hasattr(self, "confirm_button"):
            self.confirm_button.deleteLater()

    def open_standalone_folder(self):
        self.open_folder(self.file_crawler.standalone_issues_folder)

    def open_first_issues_folder(self):
        self.open_folder(self.file_crawler.first_issues_folder)

    def open_sorted_folder(self):
        self.open_folder(self.file_crawler.week_folder)

    def open_folder(self, folder_path):
        if not os.path.exists(folder_path):
            QMessageBox.critical(self, "Error", f"The folder '{folder_path}' does not exist.")
            return

        if not os.access(folder_path, os.R_OK | os.W_OK):
            QMessageBox.critical(self, "Permission Denied", f"Cannot access the folder: {folder_path}.")
            return

        os.system(f'open "{folder_path}"')  # macOS-specific


