from main import props
from datetime import date
import dictionaries
today = date.today()
date = "12/29/22"

tatum = 'https://www.basketball-reference.com/players/t/tatumja01/gamelog/2023'
lebron = 'https://www.basketball-reference.com/players/j/jamesle01/gamelog/2023'
doncic = 'https://www.basketball-reference.com/players/d/doncilu01/gamelog/2023'
jokic = 'https://www.basketball-reference.com/players/j/jokicni01/gamelog/2023'
giannis = 'https://www.basketball-reference.com/players/a/antetgi01/gamelog/2023'


# take name and date and retrieve player id

if date in dictionaries:
    props(tatum, dictionaries[date])



def conc(name):
    dictionaries = 'dictionaries.' + name
    print(dictionaries)

conc('tatum')