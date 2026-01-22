import os
from helpers.text_parser import TextParser
import pdb
import json

class Database(object):
    
    def __init__(self):
        self.parser = TextParser()
            
    def write_database(self, comic_name, comic_name_number=None):
        
        with open(r'/Users/oleksiikol/Documents/ComicsHelper/database/database.json', 'r+') as f:
            try: 
                self.comic_data = json.load(f)
                f.seek(0)
            except:
                json.dump({}, f, indent = 4)
                f.seek(0)
                self.comic_data = json.load(f)
                f.seek(0)
            
            if comic_name_number == None:
                self.comic_data[comic_name] = [comic_name]
            
            try:
                
                if  comic_name_number not in self.comic_data[comic_name]:
                    self.comic_data[comic_name].append(comic_name_number)
            except:
                 
                self.comic_data[comic_name] = [comic_name_number]
            
            json.dump(self.comic_data, f, indent = 4)
            f.seek(0)
            return self.comic_data
            
                

    def create_database(self, main_path=None):
        
        if main_path == None:
            self.main_path = '/Users/oleksiikol/Desktop/temp current comics/'
        else:
            self.main_path = main_path
        
        self.main_comics_folder = os.listdir(self.main_path)
        self.comic_folders = sorted([i for i in self.main_comics_folder if i != '.DS_Store'])

        for comic_folder in self.comic_folders:
            self.comics = sorted(os.listdir(self.main_path + comic_folder))
            
            for comic in self.comics:
                
                if comic == '.icomics-group-id':
                    continue
                
                if comic == '.DS_Store':
                    continue
                
                try:
                    comic_name = self.parser.find_comic_name(comic)
                    comic_name_number = self.parser.find_comic_series_number(comic)
                    self.write_database(comic_name=comic_name, comic_name_number=comic_name_number)
                    # print(self.comic_data)
                    # print(f'{comic_name}, {comic_name_number}') 
                except AttributeError:
                    comic_name = self.parser.find_comic_bad_name(comic)
                    self.write_database(comic_name=comic_name)
                    # print(comic_name)
                # except: 
                #     print(f'bad comic names {comic}')
                
    def check_database(self, comic_title):
        
        with open(r'/Users/oleksiikol/Documents/ComicsHelper/database/database.json', 'r+') as f:
            self.comic_data = json.load(f)
            f.seek(0)
        # pdb.set_trace()

        try:
            comic_name = self.parser.find_comic_name(comic_title)
            comic_name_number = self.parser.find_comic_series_number(comic_title)
            if comic_name.lower() in [i.lower() for i in self.comic_data.keys()]:
                self.write_database(comic_name=comic_name, comic_name_number=comic_name_number)
                return True
            else:
                return False
            # print(self.comic_data)
            # print(f'{comic_name}, {comic_name_number}') 
        except AttributeError:
            return False
            # print(comic_name)
            