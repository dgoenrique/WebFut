from bs4 import BeautifulSoup 
import cloudscraper
import pandas as pd

scrapper = cloudscraper.create_scraper()

all_items_data = []

# Extração das camisetas 

for i in range(1,39):
    url = f"https://www.recordsports.net/produtos/page/{i}/"
    resp = scrapper.get(url)

    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text, 'html.parser')

        item_link = soup.find_all('a', class_='item-link')

        

        for item_link in item_link:
            item_name_tag = item_link.find('div', class_='item-name')
            item_name = item_name_tag.text.strip()

            item_price_tag = item_link.find('span', class_='item-price')
            item_price = item_price_tag.text.strip()

            all_items_data.append({
                'nome': item_name,
                'preço': item_price
            })

for item in all_items_data:
    print(f"Nome: {item['nome']}, Preço: {item['preço']}")

df = pd.DataFrame(all_items_data)
df.to_csv('../dashboard_camisetas/data/raw_data.csv', index=False)



