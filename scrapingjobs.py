# Import all packages
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.common.exceptions import WebDriverException
import pandas as pd
from datetime import date
import time

user_word = input("Enter the name of the product: ")

ubicacion = r''
# # The driver route goes between r''  // example: r'C:\Users\chromedriver.exe'


driver = webdriver.Chrome(ubicacion)

home_link = "https://listado.mercadolibre.com.ar/"
search_kw = str(user_word).replace(" ", "-")

driver.get(home_link + search_kw + "#D[A:sony%20wh%201000]")

headphone_title = []
headphone_link = []
headphone_price = []
headphone_review = []

page = BeautifulSoup(driver.page_source, 'html.parser')

pg_amount = 2

for i in range(0, pg_amount):

    for head in page.findAll('li', attrs={'class':'ui-search-layout__item shops__layout-item'}):
        title = head.find('h2', attrs={'class': 'ui-search-item__title shops__item-title'})
        if title:
            headphone_title.append(title.text)
        else: 
            headphone_link.append(' ')
            
        link = head.find('a', attrs={'class': 'ui-search-item__group__element shops__items-group-details ui-search-link'})
        if link:
            headphone_link.append(link['href'])
        else:
            headphone_link.append(' ')
            
        price = head.find('span', attrs={'class': 'price-tag-fraction'})
        if price:
            headphone_price.append(price.text)
        else:
            headphone_price.append(' ')
            
        reviews = head.find('span', attrs={'class': 'ui-search-reviews__amount'})
        if reviews:
            headphone_review.append(reviews.text)
        else:
            headphone_review.append(' ')
        
next_btn = driver.find_element_by_class_name('andes-pagination__link shops__pagination-link ui-search-link')
next_btn.click()
time.sleep(7)
        
headphone_list = pd.DataFrame({
                                'TITLE': headphone_title,
                                'LINK': headphone_link,
                                'PRICE': headphone_price,
                                'REVIEWS': headphone_review
})

headphone_list.to_csv(r'', index=None, header=True, encoding='utf-8-sig') #
# The destination route goes between r''  // example: r'C:\Users\Desktop\example_test.csv'