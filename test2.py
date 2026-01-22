from helpers.database_handling import Database
from helpers.file_crawlers import FileCrawler
from helpers.old_gui import ComicsHelperApp
from helpers.gui import ComicsHelperApp
import sys
import os
import tkinter as tk
from PyQt5.QtWidgets import QApplication

# Establising instances
# database = Database()
file_crawler = FileCrawler()

# Creating database
# print('do you want to create a database? y/n')
# answer = input()
# if answer == 'y':
#     print('creating database')
#     database.create_database()
# elif answer == 'n':
#     print('database exists')

# Specifying week folder
print('specify new week folder')
week_folder = input()
file_crawler.series_folders(week_folder)