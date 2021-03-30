import requests
from bs4 import BeautifulSoup
#import ??? ←スクレイピング用ファイル呼び出し？(.py無し)

"""
メインファイルとの接続用…？

#def Api(area)
import requests
uni = 0
#if area = 0:
uni = '居酒屋'
#else:
    #uni = "イタリアン".encord("utf-8")
"""


"""
APIによってweb内容を取得
large_area=Z024...兵庫
midlle_area=Y370...神戸
genre=G001...居酒屋
genre=G006...イタリアン
"""
url = 'https://webservice.recruit.co.jp/hotpepper/gourmet/v1/?key=2393178cfd63b737&large_area=Z024&midlle_area=Y370&genre=G006&count=20'
#膨大な数読み込むので厳選したい…けど出来ない…

"""
結果を取得
"""
response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")

"""
リスト化
"""
result_url = range(20)#お店のURL
result_logo = range(20)#お店のロゴのURL

result_url = soup.find_all("urls")
result_logo = soup.find_all("logo_image")

#print(result_url)
#print(result_logo)

#検索結果表示
