from bs4 import BeautifulSoup
import requests

req = requests.get("https://www.nytimes.com/")
data = req.text
soup = BeautifulSoup(data, "html.parser")

count = 0
for article in soup.find_all('h2'):
    if len(article.attrs) == 1:
        if 'class' in article.attrs:
            if article.get('class')[0] == 'story-heading':
                if article.findChildren('i'):
                    continue
                else:
                    print(article.contents[0].text)
                    count += 1
    if count == 7:
        break

        # output:
        # Trump, in Poland, Asks if West Has the ‘Will to Survive’
        # U.S. Retreats on Trade. The World Isn’t Following.
        # No Signs of ‘Trump Bump’ in U.S. Growth Forecasts
        # Official Watchdog Who Clashed With Trump Is Resigning
        # Interruptions Help a New Senator Get Her Voice Heard
        # Blue Cities Make Laws. Red States Block Them.
        # Opioid Prescriptions Fall, but Addiction Crisis Persists
