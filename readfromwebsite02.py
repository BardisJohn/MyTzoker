import requests
from bs4 import BeautifulSoup

# Ζητάμε τη σελίδα
url = 'https://www.mytzoker.gr/klirosi/3086/4-1-2024/2697'
response = requests.get(url)

# Δημιουργούμε το αντικείμενο soup για parsing του HTML
soup = BeautifulSoup(response.text, 'html.parser')
#print('soup\n', soup.text[220:300])
#print(repr(soup.text[220:300]))
#print('soup\n', soup.text[220:300].encode('utf-8', 'ignore').decode('utf-8'))
# print('soup all\n', soup.text.encode('ascii', 'ignore').decode())
# print('soup part 500:600\n', soup.text[800:1000].encode('ascii', 'ignore').decode())
souplst = soup.text.split(' ')
print('soup len = ', len(souplst))
i = 0
for itemm in souplst:
    # print(i, ' : ', itemm.encode('ascii', 'ignore').decode())
    i += 1

itemm79 = souplst[79].encode('ascii', 'ignore').decode()
itemm79lst = itemm79.split()
print(itemm79lst)
# print('itemm 79 = ', souplst[79].encode('ascii', 'ignore').decode())
# Βρίσκουμε ένα στοιχείο, π.χ. το πρώτο <p>
paragraph = soup.find('strong')
#print(paragraph.text)
