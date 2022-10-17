import pickle
from Danngn_module import *
from Bunjang_module import *
from Joongna_module import *

keyword = input("검색할 품목을 입력하세요 ")

def input(keyword):
    Dg_keyword(keyword)
    # Bg_keyword(keyword)
    Jg_keyword(keyword)

input(keyword)

# with open("Dg_item_l.pkl","wb") as f:
#     pickle.dump(Dg_item_l, f)
# with open("Bg_item_l.pkl","wb") as f:
#     pickle.dump(Bg_item_l, f)
# with open("Jg_item_l.pkl","wb") as f:
#     pickle.dump(Jg_item_l, f)

print(Jg_item_l)
print(Dg_item_l)

