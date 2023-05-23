#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
    
    def set_size(self):
        return self._size
    
    def set_brand(self):
        return self._brand
    
    def get_size(self, size):
        try:
            if(type(size) == int):
                self._size = size
            else:
                raise TypeError
        except TypeError:
            print("size must be an integer")
 
    def get_brand(self, brand):
        self._brand = brand
    
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"
        
    brand = property(set_brand, get_brand)
    size = property(set_size, get_size)
