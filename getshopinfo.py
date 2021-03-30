import requests
from bs4 import BeautifulSoup
import csv
import Api #APIを取ってくる別プログラム

#APIで取ってきたURL
get_url = Api.result_url

#ファイルオープン
file = open('shopinfo.csv', 'w', encoding = 'utf-8')
w = csv.writer(file)

#スクレイピング
for i in get_url:
    load_url=i.find('pc').text
    html = requests.get(load_url)
    soup = BeautifulSoup(html.content, "html.parser")

    #店名
    shop_name = soup.find('h1', class_='shopName').text

    #電話番号
    shop_number = soup.find('span', class_='telNumber').text

    #予算
    shop_budget = soup.find('span', class_='shopInfoBudgetDinner').text

    #写真
    if soup.find('p', class_='shopHeaderLogo') is not None:
        shop_photo = soup.find('p', class_='shopHeaderLogo')
        shop_photo = shop_photo.find('img')
        shop_photo = shop_photo['src']
    else:
        shop_photo = 0

    #レビュー数(今は使えない)
    if soup.find('p', class_='review') is not None:
        shop_review  = soup.find('p', class_='review')
        shop_review = shop_review.find('span').text
    else:
        shop_review = 0

    #口コミ数
    if soup.find('p', class_='recommendReportNum') is not None:
        shop_report = soup.find('p', class_='recommendReportNum')
        shop_report = shop_report.find('span').text
    else:
        shop_report = 0

    #ジャンル
    shop_genre = soup.find('p', class_='shopInfoInnerItemTitle').text
    shop_genre = shop_genre.strip()
    """
    #全ジャンル取ろうとする場合（この場合エリアも入る）
    shop_genre = soup.find_all('p', class_='shopInfoInnerItemTitle')
    count = 0
    for j in shop_genre:
        shop_genre[count] = j.text
        shop_genre[count] = shop_genre[count].strip()
        count = count + 1
    """

    #メニュー
    menu_url = soup.find('li', class_='jscShopNavTab')#コースへのリンク取得
    menu_url = menu_url.find('a')
    menu_url = 'https://www.hotpepper.jp' + menu_url['href']

    html = requests.get(menu_url)#コースのページに飛んでスクレイピング
    soup = BeautifulSoup(html.content, "html.parser")
    shop_menu = soup.find('p', class_='courseCassetteTitle').text
    shop_menu = shop_menu.strip()
    menu_price = soup.find('span', class_='priceNumber').text

    #csvファイルに書き込み
    w.writerow([load_url, shop_name, shop_number, shop_budget, shop_photo, shop_review, shop_report, shop_genre, shop_menu, menu_price])

#ファイルクローズ
file.close()
