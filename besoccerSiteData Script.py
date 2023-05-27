#pip install requests
#pip install beautifulsoup4
#pip install lxml
import pandas
import requests
from bs4  import BeautifulSoup
import csv
date = input("Entre date Format YYYY-MM-DD : ")
url = "https://fr.besoccer.com/resultats/"+str(date)
page = requests.get(url)
print("Your website is : ",url)

def main(page):
    src = page.content
    soup = BeautifulSoup(src,'lxml')
    match_details = []
    championShips = soup.find_all("div",{'id':'mod_panel'})
    def matchTimebol():
        matchTimesBol = input("Do you Want  Time of Matchs ?  Please Tape (True or False ) : ")
        if matchTimesBol == "True":
            return True
        if matchTimesBol == "False":
            return False
    matchTime = matchTimebol()
    def get_match_info(championShips  ):
        championTitle = championShips.contents[1].find('span',{'class':'va-m'}).text.strip()
        All_Matchs =  championShips.contents[1].find_all('a' ,{'class':'match-link'} )
        number_of_games = len(All_Matchs)
        for i in range(number_of_games):
                #GET team names
                team_left  = All_Matchs[i].find('div',{'class':'team_left'}).find('div',{'class':'name'}).text.strip()
                team_right  = All_Matchs[i].find('div',{'class':'team_right'}).text.strip()
                journée  = All_Matchs[i].find('div',{'class':'middle-info'}).text.strip()
                match_time= All_Matchs[i].find('div',{'class':'marker'}).text.strip()
                match_details.append({"Name ligue :":championTitle , 'Journée / Group':journée, "Local Team ": team_left , "Away Team ": team_right  ,"Match time " :match_time })
                #GET score
               
 
    if(matchTime == True ) :
                      
            for i in range(len(championShips)):
                
        
                get_match_info(championShips[i] )
                
    else : 
             
            for i in range(len(championShips)-1):
                i+=1
                get_match_info(championShips[i], )
   
    
    #csv file 
    
    keys = match_details[0].keys()

    with open('bescore.csv', 'w' ,  encoding='utf-8-sig' ) as output_file:
        writer = csv.DictWriter(output_file,delimiter=",", quotechar='"', fieldnames=keys)
        writer.writeheader()
        writer.writerows(match_details)
    df = pandas.read_csv('bescore.csv')
    print(df)
    



main(page)