"""
Module Name:
    DataAccessLayer.py

Functions/Methods:
    

Class:
   DataAccessLayer
    
    

Imports:
    xml.etree.ElementTree - the python XML library    
    os - the operating system, pthon library

Purpose:
    Because the application we are writing is standalone we are not using a database, 
    instead we are going to use an XML file to store data in a defined format and 
    I shall use Xpath as a query language and the XML Dom to implement a CRUD layer.

    This class will act as a layer between the main application and the XML library.

    Because of the relationship between this clas and the XML library I shall inherit 
    from the XML library. Going along the lines of this being an IS-A relationship.
    
  
    
Author:
    Lewis Trahearn

"""
import xml.etree.ElementTree as ET
import os

class DataAccessLayer(ET):
    def __init__(self):
        super().__init__()
        
        main_dir = os.path.split(os.path.abspath(__file__))[0]
        file = os.path.join(main_dir, 'AppData', "Database.xml")
        try:
            self.load(file)
        except pygame.error:
            raise SystemExit('Could not load file "%s" %s'%(file, pygame.get_error()))

    




