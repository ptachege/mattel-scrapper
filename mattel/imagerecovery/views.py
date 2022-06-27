from ast import Break
from email import header
import imp
from itertools import product
from django.http import HttpResponse
from django.shortcuts import render
import urllib.request
import requests
from bs4 import BeautifulSoup

# Create your views here.
from django.core.exceptions import ObjectDoesNotExist
from selenium.webdriver.common.by import By
import csv
from django.http import HttpResponse

from .models import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .serialzers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
import math
import time


def donwload_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="products.csv"'

    writer = csv.writer(response)
    writer.writerow(['Tire name', 'Brand', 'SKU', 'Price',
                    'Description'])

    users = Tire.objects.all().values_list('tire_name', 'tirebrand', 'tiresku', 'tire_price',
                                           'tiredescription')
    for user in users:
        writer.writerow(user)
    return response


def donwload_csv_legos(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="legos.csv'
    writer = csv.writer(response)
    writer.writerow(['Product name', '#item number', 'Age', 'Pieces', 'Price',
                    'Image List', 'Product Features', 'product specification'])

    users = LogoToys.objects.all().values_list('product_name', 'items_number', 'product_age', 'product_pieces', 'product_price',
                                               'image_list', 'product_description', 'product_features')
    for user in users:
        writer.writerow(user)
    return response


@api_view(['GET', ])
def fetchAllTires(request):
    all_tires = Tire.objects.all()
    serializer = TireSerializer(all_tires, many=True)
    return Response(serializer.data)


@api_view(['GET', ])
def fetchAllLegos(request):
    all_legos = LogoToys.objects.all()
    serializer = LegoSerializer(all_legos, many=True)
    return Response(serializer.data)


def entry(request):
    return render(request, 'imagerecovery/index.html')


def crawl_theme(request):

    # first click
    pagenumbers = 22

    i = 1

    for eachpage in range(0, pagenumbers):

        item_url = 'https://shop.mattel.com/collections/shop-all#page=' + \
            str(i)
        options = Options()
        options.headless = True
        options.add_argument("--window-size=1920,1200")

        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(item_url)

        # now we are in main page
        time.sleep(10)
        soup = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(soup, 'lxml')
        driver.quit()
        # all_cards = soup.find_elements_by_class_name(
        #     "CategoryListingPagestyle__ListItemAlternate-sc-880qxz-7 drzfAx")

        all_cards = soup.findAll(
            'li', class_="collection-grid__item")

        print(all_cards)

        for each_card in all_cards:
            anchor_tag = each_card.find(
                'a', href=True)
            try:
                AllProductLinks.objects.create(
                    category_url=anchor_tag['href'],
                    crawled=False
                )

            except:
                pass
        i += 1
    return HttpResponse("saved")


def fetch_theme_category(request):
    all_category_links = AllProductLinks.objects.filter(crawled=False)

    for each_category in all_category_links:
        category_url = 'https://shop.mattel.com' + each_category.category_url
        options = Options()
        options.headless = True
        options.add_argument("--window-size=1920,1200")

        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(category_url)
        soup = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(soup, 'lxml')

        # get the number of pagination in this category

        # get relevant fields.
        # try:
        #     header_one = soup.find(
        #         'div', class_='pv-header')
        # except:
        #     header_one = ''

        try:
            product_name = soup.find(
                'h1', class_="pv-title").text.strip()
        except:
            product_name = ''

        # item Id
        # try:
        item_id = category_url.split('-')[-1]
        print(item_id)
        # except:
        #     item_id = ''

        # description.

        try:
            product_description = soup.find(
                'div', class_='pv-details__description-wrapper').text
        except:
            product_description = 'none'

        # whats in the box.

        try:
            whats_in_box = soup.find(
                'div', class_='acc__menu acc__menu--alt js-acc-menu').text.strip()
        except:
            whats_in_box = 'none'

        all_image_links = soup.findAll(
            'div', class_='pv-gallery__thumbnail js-gallery-thumbnail')

        image_list = []

        for img_link in all_image_links:
            # get image_link
            try:
                temp = img_link.find(
                    'img')['srcset']
                image_list.append(temp)
            except:
                pass

        print(item_id)
        print(product_name)
        print(whats_in_box)
        print(category_url)
        print(product_description)
        print(image_list)

        HasbroToys.objects.create(
            item_id=item_id,
            product_name=product_name,
            whats_in_box=whats_in_box,
            category_url=category_url,
            product_description=product_description,
            image_list=image_list
        )

        each_category.crawled = True
        each_category.save()
        driver.quit()
        # all_cat_cards = soup.findAll(
        #     'li', class_="ProductGridstyles__Item-lc2zkx-1 lsIZD")
        break


def fetchPrices(request):
    try:
        pagenumber = 1
        for page in range(0, 1):
            item_url = 'https://auto-xpress.co.ke/tyres/' + \
                '?wpv_view_count=19&wpv-wpcf-section-width=&wpv-wpcf-aspect-ratio=&wpv-wpcf-rim-size=&wpv_paged=' + \
                str(pagenumber)
            options = Options()
            options.headless = True
            options.add_argument("--window-size=1920,1200")

            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.get(item_url)
            soup = driver.page_source.encode('utf-8').strip()
            soup = BeautifulSoup(soup, 'lxml')

            all_cards = driver.find_elements_by_class_name("product-box")
            mybtn = driver.find_elements_by_xpath(
                "//*[@class='yith-wcqv-button button']")

            i = 0
            for eachcard in all_cards:
                print(i)
                divwithTitle = eachcard.find_elements_by_class_name(
                    "grey-box-loop")
                for tt in divwithTitle:
                    tirehead = tt.find_elements_by_tag_name("span")[0].text
                    tiredescription = tt.find_elements_by_tag_name("span")[
                        1].text
                # GET PRICE
                tireprice = eachcard.find_elements_by_tag_name("bdi")[0].text
                price1 = tireprice.replace("KSh", "")
                price2 = price1.replace(",", "")
                price = price2.replace(" ", "")

                # GET BRAND

                first_word_brand = tirehead.split()[0]
                btn = mybtn[i]
                driver.execute_script("arguments[0].click();", btn)
                import time
                time.sleep(3)
                # print(heading)

                try:

                    this_SKU = eachcard.find_elements_by_xpath(
                        "//*[@class='sku']")[0].get_attribute('textContent')
                except:
                    this_SKU = 'N/A'
                closebtn = driver.find_elements_by_xpath(
                    "//*[@class='yith-quick-view-close']")[0]

                # print(this_SKU)

                try:
                    n = Tire.objects.get(tiresku=this_SKU)
                    n.tire_price = price
                    n.save()

                except ObjectDoesNotExist:
                    Tire.objects.create(
                        tire_name=tirehead,
                        tire_price=price,
                        tirebrand=first_word_brand,
                        tiresku=this_SKU,
                        tiredescription=tiredescription,
                    )
                    print('save successfull')

                driver.execute_script("arguments[0].click();", closebtn)
                i += 1
            driver.quit()
            print('Printed page' + str(pagenumber))
            pagenumber += 1

            # driver.refresh()
        context = {
            'all_a_list': 'Data Saved Successfully',
        }
        return render(request, 'imagerecovery/index.html', context)
    except:
        context = {
            'error': 'Sorry an error occured',
        }
        return render(request, 'imagerecovery/index.html', context)
