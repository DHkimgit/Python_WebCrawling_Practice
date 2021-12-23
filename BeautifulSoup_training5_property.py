import bs4

html_str = """
<html>
    <body>
        <ul class="ko">
            <li>
                <a herf="https://www.naver.com/">네이버</a>
            </li>
            <li>
                <a herf="https://www.daum.net/">다음</a>
            </li>
        </ul>
        <ul class="sns">
            <li>
                <a herf="https://www.google.com/">구글</a>
            </li>
            <li>
                <a herf="https://www.facebook.com/">페이스북</a>
            </li>
        </ul>
    </body>
</html>
"""

bs_obj = bs4.BeautifulSoup(html_str, "html.parser")
ul = bs_obj.find("ul", {"class":"ko"})
li = ul.findAll("li")
ol = li[0].find("a")
print(ol.text)