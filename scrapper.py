from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

results = []

def scrap(page_num):

    for i in range(1, page_num + 1):

        driver.get(f"https://dentalstall.com/shop/page/{i}")

        titles = driver.find_elements(
            By.CSS_SELECTOR,
            "#mf-shop-content > ul > li > div > div.mf-product-details > div.mf-product-content > h2",
        )
        images = driver.find_elements(
            By.CSS_SELECTOR,
            "#mf-shop-content > ul > li > div > div.mf-product-thumbnail > a > img",
        )
        prices = driver.find_elements(
            By.CSS_SELECTOR,
            "#mf-shop-content > ul > li > div > div.mf-product-details > div.mf-product-price-box > span.price",
        )

        for x in range (len(titles)):
            try:
                product_title = titles[x].text
            except IndexError:
                product_title = 'none'

            try:
                product_price = prices[x].text
            except IndexError:
                product_price = 'none'

            try:
                path_to_image = images[x].get_attribute('src')
            except IndexError:
                path_to_image = 'none'


            results.append({
                'product_title': product_title,
                'product_price': product_price,
                'path_to_image': path_to_image
            })
        
    return results

if __name__ == '__main__':
    print(results)
