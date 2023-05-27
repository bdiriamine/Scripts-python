#pip install requests
#pip install beautifulsoup4
#pip install lxml
import requests
from bs4  import BeautifulSoup
import csv
import pandas
date =input( " entre a date in this format (MM/DD/YYYY) :")
url ="https://www.yallakora.com/match-center/?date="+str(date)
page = requests.get(url)

def main(page):
    src = page.content
    soup = BeautifulSoup(src,"lxml")
    match_details = []
    championShips = soup.find_all("div",{'class':'matchCard'})
    def get_match_info(championShips):
        championTitle = championShips.contents[1].find('h2').text.strip()
        All_Matchs =  championShips.contents[3].find_all("li")
        number_of_games = len(All_Matchs)
        print(number_of_games)
        for i in range(number_of_games):
            #GET team names
            teamA = All_Matchs[i].find('div',{'class':'teamA'}).text.strip()
            teamB = All_Matchs[i].find('div',{'class':'teamB'}).text.strip()
              #GET score
            match_Result = All_Matchs[i].find('div',{'class':'MResult'}).find_all('span',{'class':'score'})
            score=f"{match_Result[0].text.strip()} - {match_Result[1].text.strip()}"
            match_time= All_Matchs[i].find('div',{'class':'MResult'}).find('span',{'class':'time'}).text.strip()
        
        match_details.append({"Name ligue :":championTitle , "Local Team ": teamA, "Away Team ": teamB ,"Match time " :match_time, "score":score})   
    for i in range(len(championShips)):
        get_match_info(championShips[i])
    
    #csv file 
    keys = match_details[0].keys()

    with open('some.csv', 'w' , encoding='utf-8-sig' ) as output_file:
        writer = csv.DictWriter(output_file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(match_details)
    df = pandas.read_csv('some.csv')
    print(df)



main(page)