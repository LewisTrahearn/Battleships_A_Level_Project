"""
Module Name:
    DataAccessLayer.py

Functions/Methods:
    _username                 - the username of the player
    _forename                 - the forenmame of the player
    _surname                  - the surname of the player
    _email                    - the users email address
    _password                 - the password of the player
    _get_logged_user_player_1 - checks the login status of player 1
    _get_logged_user_player_2 - checks the login status of player 2
    _write_database           - writes the inputted data to the database
    _is_user_valid            - validates the input of the user
    _get_next_db_id           - gives the next database id for a new user so they are saved with different ID's

Class:
   DataAccessLayer
    
    

Imports:
    xml.etree.ElementTree - the python XML library    
    os - the operating system, pthon library
    xml.dom
    minidom

Purpose:
    Because the application we are writing is standalone we are not using a database, 
    instead we are going to use an XML file to store data in a defined format and 
    I shall use Xpath as a query language and the XML Dom to implement a CRUD layer.

    This class will act as a layer between the main application and the XML library.

    Because of the relationship between this clas and the XML library I shall inherit 
    from the XML library. Going along the lines of this being an IS-A relationship.
    
    However this particular module is written in C programming language and in this instance
    means that inheritance is not working
    
    therefore I will now implement this as an aggregate class instead. this is an example
    of a HAS-A relationship.
    
Author:
    Lewis Trahearn

"""

import xml.etree.ElementTree as ET
import os
from xml.dom import minidom

class loggedInUser(object):
    """ """
    def __init__(self, id="", forename="", surname="", username="", email="", password=""):
        self._id = id
        self._forename = forename
        self._surname = surname
        self._username = username
        self._email = email
        self._password = password

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self,value):
        self._id = value

    @property
    def forename(self):
        return self._forename
    
    @forename.setter
    def forename(self,value):
        self._forename = value

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self,value):
        self._surname = value

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self,value):
        self._username = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self,value):
        self._email = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self,value):
        self._password = value

class DataAccessLayer():
    def __init__(self):
        main_dir = os.path.split(os.path.abspath(__file__))[0]
        self._file = os.path.join(main_dir, 'AppData', "database.xml")

        self._tree = ET.parse(self._file)
        self._root = self._tree.getroot()
        self._logged_in_user_player_1 = None
        self._logged_in_user_player_2 = None

    def get_logged_user_player_1(self):
        return self._logged_in_user_player_1

    def get_logged_user_player_2(self):
        return self._logged_in_user_player_2
    def is_player_two_logged_in(self):
        if self._logged_in_user_player_2 != None:
            return True
        else:
            return False

    def is_user_valid(self, username, password, player=1):
        return_value = False

        users = self._root.find("users")
        for user in users:
            db_username = user.find("username").text
            db_password = user.find("password").text
            if (username == db_username) and (password == db_password):
                return_value = True
                db_forename = user.find("forename").text
                db_surname = user.find("surname").text
                db_email = user.find("email").text
                db_id = user.attrib
                db_user = loggedInUser(db_id, db_forename, db_surname, db_username, db_email, db_password)
                if player == 1:
                    self._logged_in_user_player_1 = db_user
                else:
                    self._logged_in_user_player_2 = db_user
                break

        return return_value

    def _get_next_db_id(self):
        try:
            id = self._root.get("nextuserid")
            next_id = int(id) + 1
            self._root.set("nextuserid",str(next_id))
        except:
            id = -1 
        
        return id


    def create_user(self, forename, surname, username, email, password):
        
        return_value = False

        users = self._root.find("users")
        new_element = ET.SubElement(users, "user")
        new_id = self._get_next_db_id()
        new_element.set('id',new_id)
        new_forename = ET.SubElement(new_element,"forename")
        new_forename.text = forename

        new_surname = ET.SubElement(new_element,"surname")
        new_surname.text = surname

        new_username = ET.SubElement(new_element,"username")
        new_username.text = username

        new_email = ET.SubElement(new_element,"email")
        new_email.text = email

        new_password = ET.SubElement(new_element,"password")
        new_password.text = password

        new_stats = ET.SubElement(new_element,"stats")

        self._write_database()
        return return_value
        
        
        
    def _write_database(self):
        strXML = ET.tostring(self._root,encoding="unicode", method="xml", short_empty_elements=True)
        

        xmlstr = minidom.parseString(strXML).toprettyxml(indent="    ", newl='\n')
        

        # this is to fix the bug with prettyxml that adds additional lines
        output = ""
        lines = xmlstr.split('\n')
        for line in lines:
            tmp_line = line.strip()
            if len(tmp_line) > 0:
                output = output + (line+ '\n')

        with open(self._file, "w") as f:
            f.write(output)


    def update_logged_in_player_1(self, logged_in_user):
        return_value = None
        # check that the updated user is player 1 only
        if logged_in_user._id["id"] == self._logged_in_user_player_1._id["id"]:
            id = logged_in_user._id["id"]
            xpath = xpath_search_string = "users/user[@id=\"{}\"]".format(id) 
            
            xml_node_list = self._root.findall(xpath)
            # findall returns a list of elements and in this
            # case we are only interested in the first 1.

            if xml_node_list[0] != None:
        #        strforename = xml_node_list[0].find("forename").text
                xml_node_list[0].find("forename").text = logged_in_user.forename
                xml_node_list[0].find("surname").text = logged_in_user.surname
                xml_node_list[0].find("username").text = logged_in_user.username
                xml_node_list[0].find("email").text = logged_in_user.email
                xml_node_list[0].find("password").text = logged_in_user.password
                self._write_database()

