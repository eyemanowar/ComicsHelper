import re


class TextParser(object):
    
    # comic_title_with_number = '^(.*?)(?=\(of)|^(.*?)(?=\(20)'
    # comic_title = '^(.*?)(?=\d{2,4} \(of)|^(.*?)(?=\d{2,4} \(20)'
        
    def __init__(self):
        self.comic_title = re.compile(r'^(.*)(?= \d{2,4} \(of)|^(.*)(?= \d{3,4} \(20)|^(.*?)(?= \(\d{4})|^(.*)(?= \d{3,4})')
        # self.comic_title = re.compile(r'^(.*?)(?= \d{1,4}(?: \(|$))')
        self.comic_title_with_number = re.compile(r'^(.*?)(?= \(of)|^(.*?)(?= \(20)|^(.*?)(?= \(\d{4})')
        self.bad_comic_title = re.compile(r'^(.*?)(?=\.cb)')
        self.week_date = re.compile(r'\d{4}.\d{2}.\d{2}')
        self.first_issue = re.compile(r'.*001|(.*01)(?= \(of)')
        self.stand_alone = re.compile(r'\(of \d{2}|\d{3,4} \(20')
        
    def find_comic_name(self, string):
        return re.search(self.comic_title, string).group()
    
    def find_comic_series_number(self, string):
        return re.search(self.comic_title_with_number, string).group()
    
    def find_comic_bad_name(self, string):
        return re.search(self.bad_comic_title, string).group()
    
    def find_week_date(self, string):
        
        self.matched_string = re.search(self.week_date, string).group()
        
        self.formatted = ''
        for char in self.matched_string:
            if char == '.':
                char = ' '
            self.formatted += char
        return self.formatted
    
    def check_if_first_issue(self, string):
        try:
            re.search(self.first_issue, string).group()
            return True
        except:
            return False
    
    def check_if_stand_alone(self, string):
        try:
            re.search(self.stand_alone, string).group()
            return False
        except:
            return True
        
    
    