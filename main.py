from helpers.database_handling import Database
from helpers.file_crawlers import FileCrawler
# from helpers.old_gui import ComicsHelperApp
from helpers.gui import ComicsHelperApp
import sys
import os
import tkinter as tk
from PyQt5.QtWidgets import QApplication

os.environ['TK_SILENCE_DEPRECATION'] = '1'
os.environ['NO_MAINMENU'] = '1'

if __name__ == '__main__':
    sys.stderr = open("error.log", "w")
    sys.stdout = open("output.log", "w")
    # Establising instances
    # database = Database()
    # file_crawler = FileCrawler()

    # Creating database
    # print('do you want to create a database? y/n')
    # answer = input()
    # if answer == 'y':
    #     print('creating database')
    #     database.create_database()
    # elif answer == 'n':
    #     print('database exists')

    # Specifying week folder
    # print('specify new week folder')
    # week_folder = input()
    # file_crawler.sorted_comics(week_folder[1:-1])

    # working with sorted comics
    # print('have you checked standalone and first issues? y/n')
    # answer = input().lower()
    # while answer != 'y':
    #     print("your new answer")
    #     answer = input().lower()
    # file_crawler.add_new_comics_to_reading_list()
    # print("this week's done")


    app = QApplication(sys.argv)
    window = ComicsHelperApp()
    window.show()
    sys.exit(app.exec_())