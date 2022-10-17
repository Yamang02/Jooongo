import re
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

https://web.joongna.com/_next/data/GiqzOLGvy-9lmY8J7ihC0/search.json?keyword=%EB%85%B8%ED%8A%B8%EB%B6%81

Jg_item_l = []

def Jg_keyword(keyword):

    url = "https://web.joongna.com/search?keyword="
    s_url = url + keyword
    # https://web.joongna.com/search?keyword={product}&page={int}

    #헤드리스를 사용하여 크롬을 열지 않고 크롬 구동
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    # options.add_argument("window-size=800x600")
    # options.add_argument("user-agent= Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36")

    # url로 이동
    pages = range(1,3)
    for page in pages:
        p_url = s_url+"&page={}".format(page)
        res = requests.get(p_url, headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"})
        res.raise_for_status()
        browser = webdriver.Chrome('./chromedriver', chrome_options=options)
        browser.get(p_url) 

        # 현재 페이지 소스 추출
        html = browser.page_source
        soup = BeautifulSoup(html,'html.parser')
        i_url = "https://web.joongna.com"

        item_list = soup.find_all("a", attrs={"class":"css-8rmnao"})

        # prouducts per page == 20(max)
        for idx in range(0,len(item_list)):
            item = item_list[idx]
            
            # 이미지 링크, 이름, 가격, 정보(위치 | 시간), 링크
            i_img = item.find("img")["src"]
            i_name = item.find("span", attrs={"class":"css-5uwdmz"}).get_text().strip()
            i_price = item.find("div", attrs={"class":"priceTxt"}).get_text().strip()
            i_regif_lt = item.find("div", attrs={"class":"registInfo"}).find_all("span")
            if len(i_regif_lt) == 2: # 위치 , 시간
                i_regif_l = i_regif_lt[0].get_text().strip()
                i_regif_t = i_regif_lt[1].get_text().strip()
                i_regif = i_regif_l, i_regif_t
                i_regif = re.sub("'","",str(list(i_regif))[1:-1])        
            elif len(i_regif_lt) == 1: # 시간
                i_regif = item.find("div", attrs={"class":"registInfo"}).get_text().strip()
            
            i_link = i_url + str(item["href"])

            print("========[중고나라] '" + keyword + "' {}번째 item ==================".format(idx+1) )
            print("이미지 링크 : ", i_img)
            print("상품명 : ", i_name)
            print("가격 : ", i_price)
            print("정보 : ", i_regif)
            print("상품 링크 :", i_link)

            # Jg_newitem = {'sort': 'Jg', 'page':page, 'idx':idx, 'img':i_img, 'name':i_name, 'price':i_price, 'info':i_regif, 'link':i_link}
            # Jg_item_l.append(Jg_newitem)


keyword = input("검색할 품목을 입력하세요 ")
Jg_keyword(keyword)