import json
import requests
from bs4 import BeautifulSoup
from time import sleep


def scrap(html_content):
    soup = BeautifulSoup(html_content.content, "html.parser")

    results = soup.find(id='mf-shop-content')
    products = results.find_all("div", class_="product-inner")

    response=[]

    for product in products:
        name = product.find("h2", class_="woo-loop-product__title").text
        img = product.find('img', class_='size-woocommerce_thumbnail')['data-lazy-src']

        try:
            product_price = product.find('bdi', class_='').text
        except AttributeError:
            product_price = 'none'

        data = {
                    "product_title": name,
                    "product_price": product_price,
                    "path_to_image": img
                }
        response.append(data)

    return response


def get_html_content(page_num: int, n_secs: int):
        url = f"https://dentalstall.com/shop/page/{page_num}"
        page = requests.get(url)

        if page.status_code == 200:
           return page
        else:
            print(f'Retrying after {n_secs} secs for page {page_num}')
            sleep(n_secs)
            get_html_content(page_num=page_num, n_secs=n_secs)


def run(page_num: int, n_secs: int):
    for i in range(1, page_num+1):
        print(f'Scrapping data for page {i}')

        html_content = get_html_content(page_num=i, n_secs=n_secs)

        scrapped_data = scrap(html_content)

        f = open('result.json', 'a')
        f.write(f'{json.dumps(scrapped_data)},')

        print(f'Scrapping done for page {i}') 
