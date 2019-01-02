
import xml.etree.ElementTree as ET
import os
from xml.dom import minidom
import re

class loggedInUser(object):
    """ """
    def __init__(self, id, forename, surname, username, email, password):
        self._id = id
        self._forename = forename
        self._surname = surname
        self._username = username
        self._email = email
        self._password = password

    @property
    def forename(self):
        return self._forename

    @property
    def surname(self):
        return self._surname

    @property
    def username(self):
        return self._username

    @property
    def email(self):
        return self._email

    @property
    def password(self):
        return self.password




class testXML(object):
    """description of class"""
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
                strforename = xml_node_list[0].find("forename").text
                pass
       

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
                user = loggedInUser(db_id, db_forename, db_surname, db_username, db_email, db_password)
                if player == 1:
                    self._logged_in_user_player_1 = user
                else:
                    self._logged_in_user_player_2 = user
                break

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

    def create_user(self, forename, surname, username, email, password):
        
        return_value = False

        users = self._root.find("users")
        new_element = ET.SubElement(users, "user")
        new_element.set('id','3')
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
        ET.dump(self._root)
        return return_value

    def test(self):

        main_dir = os.path.split(os.path.abspath(__file__))[0]
        file = os.path.join(main_dir, 'AppData', "database.xml")

        tree = ET.parse(file)
        root = tree.getroot()

        for child in root:
            print(child.tag, child.attrib)

        users = root.find("users")

        b_is_element = ET.iselement(users)

        newElement = ET.SubElement(users, "user", id='8')
        newElement.set('xyz','889')

        for child in users:
            print(child.tag, child.attrib)



        
        ET.dump(root)

        ET.dump(root)

