# 라이브러리 불러오기
import requests
from bs4 import BeautifulSoup

# 검색 키워드

# 해당 url의 html문서를 soup 객체로 저장
url='https://kart.nexon.com/Kart/News/Patch/view.aspx?n4articlesn=75185'
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')


search_result = soup.select('#kart_main_sections> section.board > div.board_inner>div.board_viewsec>div.board_imgarea>table>tbody>tr>td>p')

for i in search_result:
    print(i.text)
    
#수정중 깃데스크탑 배우는
