#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
    
    def set_title(self):
        return self._title
    
    def set_page_count(self):
        return self._page_count
    
    def get_title(self, title):
        self._title = title

    def get_page_count(self, page_count):
        try:
            if(type(page_count) == int):
                self._page_count = page_count  
            else:
                raise TypeError("")            
        except TypeError:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    title = property(set_title, get_title)
    page_count = property(set_page_count, get_page_count)
    
        