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
import StatsContainer as StatsCon
import NumberOfGamesContainer as Wins

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
        self._Stats = []
        self._game_count_stats = []


    def get_logged_user_player_1(self):
        return self._logged_in_user_player_1

    def get_logged_user_player_2(self):
        return self._logged_in_user_player_2
    
    def is_player2_cpu(self):
        return_value = False
        if self._logged_in_user_player_2 != None:
            if self._logged_in_user_player_2.username == "CPU":
                return_value = True
        return return_value
    
    def get_logged_in_player_1_stats(self):
        return_value = None
        # check that the updated user is player 1 only
        tmpArray = []
        id = self._logged_in_user_player_1._id["id"]
        xpath = xpath_search_string = "users/user[@id=\"{}\"]".format(id) 
        
        xml_node_list = self._root.findall(xpath)
            # findall returns a list of elements and in this
            # case we are only interested in the first 1.
        try:

            if xml_node_list[0] != None:
                user = xml_node_list[0]
                list_of_stats = user.findall("stats/stat")
                gamecount = 0
                win_count = 0
                lowest_number_of_hits = 9999
                for stat in list_of_stats:
                    win = False
                    tmp = stat.attrib["win"]
                    number_of_shots = int(stat.attrib["number_of_shots"])

                    if number_of_shots < lowest_number_of_hits:
                        lowest_number_of_hits = number_of_shots

                    gametime = stat.attrib["gametime"]
                    tmpArray.append(gametime)
                    gamecount = gamecount + 1
                    if tmp == "true":
                        win_count = win_count + 1

            result = sorted(tmpArray )
            lowest_time = result[0]
        except:
            gamecount = 0
            win_count = 0
            lowest_number_of_hits = 999
            lowest_time = "00:00:00"

        return   gamecount,  win_count,  lowest_number_of_hits, lowest_time

    def is_player_two_logged_in(self):
        if self._logged_in_user_player_2 != None:
            return True
        else:
            return False

    def load_number_of_games_stats(self):
        users = self._root.find("users")
        for user in users:
            db_username = user.find("username").text
            list_of_stats = user.findall("stats/stat")
            gamecount = 0
            win_count = 0
            try:
                for stat in list_of_stats:
                    win = False
                    tmp = stat.attrib["win"]
                    gamecount = gamecount + 1
                    if tmp == "true":
                        win_count = win_count + 1

                if gamecount > 0:
                    objStat = Wins.NumberOfGamesContainer(db_username, gamecount, win_count)
                    if objStat.win_count != 0:
                        self._game_count_stats.append(objStat)
            except:
                continue

    def sort_by_number_of_wins(self):
        result = sorted(self._game_count_stats,key=lambda NumberOfGamesContainer: NumberOfGamesContainer.win_count,reverse=True )
        return result


    def load_game_stats(self):
        users = self._root.find("users")
        for user in users:
            db_username = user.find("username").text
            list_of_stats = user.findall("stats/stat")
 
            for stat in list_of_stats:
                gametime = stat.attrib["gametime"]
                number_of_shots = int(stat.attrib["number_of_shots"])
                opponent = stat.attrib["opponent"]
                win = False
                tmp = stat.attrib["win"]
                if tmp == "true":
                    win = True
                    objStat = StatsCon.StatsContainer(db_username, gametime, number_of_shots, opponent, win)
                    self._Stats.append(objStat)


    def sort_by_number_of_shots(self):
        result = sorted(self._Stats,key=lambda StatsContainer: StatsContainer.number_of_shots )
        return result

    def get_position_in_crew_based_upon_shots(self, shots):
        result = self.sort_by_number_of_shots()
        count = 0
        for stat in result:
            count = count + 1
            if stat.number_of_shots >= shots:
                break
        return self.get_ordinal(count)

    def get_position_in_crew_based_upon_gametime(self, time):
        result = self.sort_by_gametime()
        count = 0
        for stat in result:
            count = count + 1
            if stat.gametime == time:
                break
        return self.get_ordinal(count)


    def sort_by_gametime(self):
        result = sorted(self._Stats,key=lambda StatsContainer: StatsContainer.gametime )
        return result  


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


    def add_stat_to_player(self, player, gametime, number_of_shots, win):
        if player == 1:
            user = self._logged_in_user_player_1
            opponent = self._logged_in_user_player_2
        else:
            user = self._logged_in_user_player_2
            opponent = self._logged_in_user_player_1            
        
        #  <stat gametime="20:33:0123" number_of_shots="144" opponent="computer" win="true"/>
        xpath = 'users/user[@id="{}"]'.format(user.id['id']) 
            
        xml_node_list = self._root.findall(xpath)
        # findall returns a list of elements and in this it should be only 1 based upon the id

        if xml_node_list[0] != None:
            current_user = xml_node_list[0]

        stats = current_user.find("stats")
        new_element = ET.SubElement(stats, "stat")
        new_element.set('gametime',gametime)
        new_element.set('number_of_shots',number_of_shots)
        new_element.set('opponent',opponent.username)
        new_element.set('win',win)

        self._write_database()


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


    def get_ordinal(self, pos):
        return_value = "out of range"
        ordinal = [ "", "1st","2nd","3rd","4th","5th","6th","7th","8th","9th","10th",
                    "11th","12th","13th","14th","15th","16th","17th","18th","19th","20th",
                    "21st","22nd","23rd","24th","25th","26th","27th","28th","29th","30th",
                    "31st","32nd","33rd","34th","35th","36th","37th","38th","39th","40th",
                    "41st","42nd","43rd","44th","45th","46th","47th","48th","49th","50th",
                    "51st","52nd","53rd","54th","55th","56th","57th","58th","59th","60th",
                    "61st","62nd","63rd","64th","65th","66th","67th","68th","69th","70th",
                    "71st","72nd","73rd","74th","75th","76th","77th","78th","79th","80th",
                    "81st","82nd","83rd","84th","85th","86th","87th","88th","89th","90th",
                    "91st","92nd","93rd","94th","95th","96th","97th","98th","99th","100th",
                    "101st","102nd","103rd","104th","105th","106th","107th","108th","109th",
                    "110th","111th","112th","113th","114th","115th","116th","117th","118th","119th",
                    "120th","121st","122nd","123rd","124th","125th","126th","127th","128th","129th",
                    "130th","131st","132nd","133rd","134th","135th","136th","137th","138th","139th",
                    "140th","141st","142nd","143rd","144th","145th","146th","147th","148th","149th",
                    "150th","151st","152nd","153rd","154th","155th","156th","157th","158th","159th",
                    "160th","161st","162nd","163rd","164th","165th","166th","167th","168th","169th",
                    "170th","171st","172nd","173rd","174th","175th","176th","177th","178th","179th",
                    "180th","181st","182nd","183rd","184th","185th","186th","187th","188th","189th",
                    "190th","191st","192nd","193rd","194th","195th","196th","197th","198th","199th",
                    "200th","201st","202nd","203rd","204th","205th","206th","207th","208th","209th",
                    "210th","211th","212th","213th","214th","215th","216th","217th","218th","219th",
                    "220th","221st","222nd","223rd","224th","225th","226th","227th","228th","229th",
                    "230th","231st","232nd","233rd","234th","235th","236th","237th","238th","239th",
                    "240th","241st","242nd","243rd","244th","245th","246th","247th","248th","249th",
                    "250th","251st","252nd","253rd","254th","255th","256th","257th","258th","259th",
                    "260th","261st","262nd","263rd","264th","265th","266th","267th","268th","269th",
                    "270th","271st","272nd","273rd","274th","275th","276th","277th","278th","279th",
                    "280th","281st","282nd","283rd","284th","285th","286th","287th","288th","289th",
                    "290th","291st","292nd","293rd","294th","295th","296th","297th","298th","299th",
                    "300th","301st","302nd","303rd","304th","305th","306th","307th","308th","309th",
                    "310th","311th","312th","313th","314th","315th","316th","317th","318th","319th",
                    "320th","321st" ]
        if pos >=0 and pos <=321:
            return_value = ordinal[pos]
        
        return return_value