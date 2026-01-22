import os
import shutil
from helpers.text_parser import TextParser
from helpers.database_handling import Database
import pdb



class FileCrawler(object):
    
    def __init__(self):
        self.parser = TextParser()
        self.database = Database()
        self.week_folder = ''
        self.proccessed_comics = []
        self.standalone_issues_folder = None
        self.first_issues_folder = None
        self.week_folder = None
    
    def move_comic_to_folder(self, origin_folder, target_folder):
        shutil.move(origin_folder, target_folder)
            
    
    def extracted_comics_from_folder(self, origin_folder):
        self.comic_folders = sorted(os.listdir(origin_folder))
        self.origin_folder_conatins = sorted([i for i in self.comic_folders if not i.startswith('.')])
        # pdb.set_trace()
        
        if '.cb' not in self.origin_folder_conatins[0]:
            
            for folder in self.origin_folder_conatins:
                if folder.startswith('.'):
                    continue
                else:
                    folder_path = f'{origin_folder}/{folder}'
                    self.extracted_comics_from_folder(origin_folder=folder_path)
                
        else:
              
            for comic in self.origin_folder_conatins:
                
                if comic == '.icomics-group-id':
                    continue
                
                if comic == '.DS_Store':
                    continue
                
                if '.pdf' in comic:
                    continue

                if 'metadata' in comic:
                    continue

                comic_path = f'{origin_folder}/{comic}'
                self.proccessed_comics.append((comic, comic_path))
                
        return self.proccessed_comics
    
    def sorted_comics(self, origin_folder):

        self.all_comics = self.extracted_comics_from_folder(origin_folder)
        self.week = self.parser.find_week_date(origin_folder)
        
        self.week_folder = f'{origin_folder}/week {self.week}'
        os.mkdir(self.week_folder)
        
        self.first_issues_folder = f'{origin_folder}/first issues'
        os.mkdir(self.first_issues_folder)
        
        self.standalone_issues_folder = f'{origin_folder}/stand alone issues'
        os.mkdir(self.standalone_issues_folder)

        # pdb.set_trace()
        
        for comic in self.all_comics:
            
            # print(self.all_comics)
            
            # print(f'working on {comic[1]}')
            # pdb.set_trace()
                    
            if self.database.check_database(comic[0]):
                target_folder = f'{self.week_folder}/{comic[0]}'
                # pdb.set_trace()
                self.move_comic_to_folder(origin_folder=comic[1], target_folder=target_folder)
                continue
            
            
            if self.parser.check_if_first_issue(comic[0]):
                target_folder = f'{self.first_issues_folder}/{comic[0]}'
                self.move_comic_to_folder(origin_folder=comic[1], target_folder=target_folder)
                continue
            
            # pdb.set_trace()
                
            if self.parser.check_if_stand_alone(comic[0]):
                target_folder = f'{self.standalone_issues_folder}/{comic[0]}'
                self.move_comic_to_folder(origin_folder=comic[1], target_folder=target_folder)
    
    def add_new_comics_to_reading_list(self):
        
        self.proccessed_comics = []
        
        self.new_comics_to_read = self.extracted_comics_from_folder(self.week_folder)
        # pdb.set_trace()
        
        for comic in self.new_comics_to_read:
            try:
                comic_name = self.parser.find_comic_name(comic[0])
                comic_name_number = self.parser.find_comic_series_number(comic[0])
                self.database.write_database(comic_name=comic_name, comic_name_number=comic_name_number)
            except AttributeError:
                print(f"impposible to parse this comic -- {comic}")

        self.proccessed_comics = []

    def series_folders(self, origin_folder):

        self.all_comics = self.extracted_comics_from_folder(origin_folder)

        for comic in self.all_comics:
            print(comic)

            comic_name = self.parser.find_comic_name(comic[0])
            comic_folder = f'/Users/oleksiikol/Desktop/series/{comic_name}'
            # pdb.set_trace()

            if not os.path.exists(comic_folder):
                os.makedirs(comic_folder)

            # if os.path.exists(comic_folder):
            self.move_comic_to_folder(origin_folder=comic[1],target_folder=comic_folder)
