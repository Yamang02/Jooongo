import requests


Bg_item_l = {}
keyword = input("검색할 품목을 입력하세요 ")

# url = "https://api.bunjang.co.kr/api/1/find_v2.json?q={keyword}&order=score&page={int}
page = 0
url = "https://api.bunjang.co.kr/api/1/find_v2.json?q={}&order=score&page={}".format(keyword, page)
json = requests.get(url).json()
Bg_lists = json.get("list")
# max 100 products per page

class Bg_item:
    def __init__(self, i_idx, img, link, name, price, location, time):
        self.idx = i_idx
        self.img = img
        self.link = link
        self.name = name
        self.price = price
        self.location = location
        self.time = time

def Bg_keyword(keyword):
    
    for idx in range(0,len(Bg_lists)):
        item = Bg_lists[idx]
        i_url = "https://m.bunjang.co.kr/products/"
        i_link = i_url + item.get("pid")
        i_img = item.get("product_image")
        i_name = item.get("name")
        i_price = item.get("price")
        i_location = item.get("location")
        i_time = item.get("update_time")

        Bg_item_l.setdefault("Bg_{}_{}".format(page+1,idx+1),Bg_item("Bg_{}_{}", i_img, i_link, i_name, i_price, i_location, i_time))

Bg_keyword(keyword)

   