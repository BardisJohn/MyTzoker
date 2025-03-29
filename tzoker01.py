import requests
from bs4 import BeautifulSoup
import csv
import os

# os.system('clear')

#------------------------------------------------
def find_line_with_string(string_list, target):
    for line in string_list:
        if target in line:
            return line
    return None  # If no match is found

#------------------------------------------------------
def tzokerkleiroseis(url, xlsname):

    # Send GET request to the page
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Save the HTML content to a text file
        namefilelst= url.split('/')
        namefile = ''
        for n in namefilelst:
            namefile = namefile + n
        with open(namefile, "w", encoding="utf-8") as file:
            file.write(response.text)
    else:
        print(f"Failed to fetch page. Status code: {response.status_code}")

    # Βρίσκω την γραμμή με τις κληρώσεις και
    # δημιουργώ την λίστα με τα αρχεία των ημερήσιων κληρώσεων
    urllines = response.text.splitlines()
    trgt = 'Κλήρωση ΤΖΟΚΕΡ'
    kliroseis = find_line_with_string(urllines, trgt)
    kliroseislst = kliroseis.split('href=')
    kliroseislst = kliroseislst[1:-1]
    kliroseishttplst=[]     #list of http kliroseon
    for s1 in kliroseislst:
        # print('s1\n', s1)
        s1lst = s1.split('"')
        # s2 = 'view-source:https://www.mytzoker.gr'+s1lst[1].strip()
        s2 = 'https://www.mytzoker.gr'+s1lst[1].strip()
        kliroseishttplst.append(s2)
    # print('list of http')

    # Για κάθε αρχείο κλήρωσης διαβάζω τους αριθμούς
    # και δημιουργώ την λίστα με ημερομηνία και αριθμούς
    tzokerlst = [[]]
    for httpfile in kliroseishttplst:
        tzoker = []
        # print(httpfile)
        httpfilelst = httpfile.split('/')
        tzoker.append(httpfilelst[4])
        tzoker.append(httpfilelst[5])
        tzoker.append(httpfilelst[6])
        response = requests.get(httpfile)
        # Δημιουργούμε το αντικείμενο soup για parsing του HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        souplst = soup.text.split(' ')
        itemm79 = souplst[79].encode('ascii', 'ignore').decode()
        itemm79lst = itemm79.split()
        for tz in itemm79lst:tzoker.append(tz)
        tzokerlst.append(tzoker)
        # print(itemm79lst)
        # print(tzoker)

    # save tzoker as csv
    # print(tzokerlst)
    csvname = xlsname
    headers = ['Column1', 'Column2', 'Column3']
    with open(csvname, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerows(tzokerlst)
    print('save file ', csvname)

#--------------------------------------------------------------------------------------

# ανοίγω την χρονιά για να διαβάσω τις ημέρες κλήρωσης
url = 'https://www.mytzoker.gr/kliroseis/2025'
name = 'tzoker2025.csv'
tzokerkleiroseis(url, name)

url = 'https://www.mytzoker.gr/kliroseis/2024'
name = 'tzoker2024.csv'
tzokerkleiroseis(url, name)

url = 'https://www.mytzoker.gr/kliroseis/2023'
name = 'tzoker2023.csv'
tzokerkleiroseis(url, name)
