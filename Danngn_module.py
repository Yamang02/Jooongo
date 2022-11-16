import rehttps://github.com/Yamang02/Jooongo/blob/main/Danngn_module.py
import requests
from bs4 import BeautifulSoup

Dg_item_l = {}

def Dg_keyword(keyword):

    url = "https://www.daangn.com/search/"
    s_url = url + keyword
    # https://www.daangn.com/search/{product}/more/flea_market?page={int}
    # prouducts per page == 6(max)

    pages = range(1,3)
    for page in pages:
        p_url = s_url+"/more/flea_market?page={}".format(page)
        res = requests.get(p_url)
        res.raise_for_status()
        soup = BeautifulSoup(res.text,'html.parser')

        item_list = soup.find_all("a", attrs={"class":"flea-market-article-link"})
        # prouducts per page == 6(max)

        for idx in range(0,len(item_list)):
            item = item_list[idx]
            i_url = "https://www.daangn.com"
            # 이미지 링크, 이름, 가격, 정보(위치 | 시간), 링크
            i_img = item.find("img")["src"]
            i_name = item.find("span", attrs={"class":"article-title"}).get_text().strip()
            i_price = item.find("p", attrs={"class":"article-price"}).get_text().strip()
            i_region= item.find("p", attrs={"class":"article-region-name"}).get_text().strip()
            i_link = i_url + str(item["href"])

            print("========[당근마켓] '" + keyword + "' {}번째 item ==================".format(idx+1) )
            print("이미지 링크 : ", i_img)
            print("상품명 : ", i_name)
            print("가격 : ", i_price)
            print("정보 : ", i_region)
            print("상품 링크 :", i_link)

            # Dg_newitem = {'sort': 'Dg', 'page':page, 'idx':idx, 'img':i_img, 'name':i_name, 'price':i_price, 'region':i_region, 'link':i_link}
            # Dg_item_l.append(Dg_newitem)

Dg_keyword("인형")
