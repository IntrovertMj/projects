from http.cookies import SimpleCookie
from urllib.parse import urlparse, parse_qs, urlencode
import json

URL = 'https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState=%7B%22usersSearchTerm%22%3A%22SD%22%2C%22mapBounds%22%3A%7B%22west%22%3A-104.057738%2C%22east%22%3A-96.436588%2C%22south%22%3A42.479686%2C%22north%22%3A45.945713%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A52%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22isForSaleByAgent%22%3A%7B%22value%22%3Afalse%7D%2C%22isForSaleByOwner%22%3A%7B%22value%22%3Afalse%7D%2C%22isNewConstruction%22%3A%7B%22value%22%3Afalse%7D%2C%22isForSaleForeclosure%22%3A%7B%22value%22%3Afalse%7D%2C%22isComingSoon%22%3A%7B%22value%22%3Afalse%7D%2C%22isAuction%22%3A%7B%22value%22%3Afalse%7D%2C%22isPreMarketForeclosure%22%3A%7B%22value%22%3Afalse%7D%2C%22isPreMarketPreForeclosure%22%3A%7B%22value%22%3Afalse%7D%2C%22isForRent%22%3A%7B%22value%22%3Atrue%7D%2C%22isAllHomes%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D&wants={%22cat1%22:[%22listResults%22]}&requestId=3'

def cookie_parser():
    cookie_string = 'zguid=23|%2411470f48-6e79-42f0-a387-873fb09ed543; _ga=GA1.2.1856115804.1615872455; zjs_user_id=null; zjs_anonymous_id=%2211470f48-6e79-42f0-a387-873fb09ed543%22; _gcl_au=1.1.1212786610.1615872456; _pxvid=50e437a7-8618-11eb-bf11-0242ac120005; _pin_unauth=dWlkPVkyWTJZVFptWlRZdE9URmhOQzAwWldaakxUZzNaRFF0WXpRNU5HRTJNalkwTWpSbA; __pdst=8d96c2fc59b74271a6674cfaf18579a2; g_state={"i_p":1621661015546,"i_l":4}; zgsession=1|c4f8e7eb-7d15-4976-b256-74fb9e64d7cf; _gid=GA1.2.62753539.1620042691; KruxPixel=true; DoubleClickSession=true; _pxff_bsco=1; JSESSIONID=3F282C27A6BAF296BD159A0AA7008B9C; utag_main=v_id:0178b12d982d008045b4a782848803083001707b0089f$_sn:11$_se:1$_ss:1$_st:1620044492602$dc_visit:11$ses_id:1620042692602%3Bexp-session$_pn:1%3Bexp-session$tdsyncran:1%3Bexp-session$dc_event:1%3Bexp-session$dc_region:ap-northeast-1%3Bexp-session; KruxAddition=true; _pxff_tm=1; _gat=1; _px3=b715d96d2b6b9ed7dedcfe999990d9a24f35dae642921cb4186b00d1eae6e980:yFiOXogsl98+DvymKAzHtcOSywsEReXb0vOIrIbIN4M5zth4AnzdFtr2heAZv7Pvp2uJVHCooY18wJQjBk9DdQ==:1000:l9W4w3lhxpL/AynnXIYpSgzDj1Sy0gWzmOauUBaCrkmBxoOdt4XAJ/zGU29Shp7NrlKAxfA0O3IzQ9p3EdQiN5FiVerOypdbwulO/Czuq0r5Kk7My67qERTR6I2vvogu/bVNfQK+TePlu9Dq5dtFuxcZ98Fc3WD0PU193gmQpC8=; _uetsid=e74d2040ac0511eba73e990e8514d5d3; _uetvid=187cdcb0985b11ebab7ff3c813e68b4a; AWSALB=LrC/PwBTzJETGBOYHfRq0pSnzbOuDH3ZDvI+NWOxRBc2lnwAUiJMd8nI9tN94N9ZWlyz9dA7wqvVHudJvNbD+F2hskScBYDQW3fXHAgzLooIkeEKCsM1uV4Y8h5U; AWSALBCORS=LrC/PwBTzJETGBOYHfRq0pSnzbOuDH3ZDvI+NWOxRBc2lnwAUiJMd8nI9tN94N9ZWlyz9dA7wqvVHudJvNbD+F2hskScBYDQW3fXHAgzLooIkeEKCsM1uV4Y8h5U; search=6|1622634775770%7Crect%3D40.85072000685613%252C-73.83891947781667%252C40.7092244017722%252C-74.06108052218333%26rid%3D61705%26disp%3Dmap%26mdm%3Dauto%26p%3D2%26sort%3Ddays%26z%3D1%26fs%3D0%26fr%3D1%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%09%0961705%09%09%09%09%09%09'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    cookies = {}

    for key, morsel in cookie.items():
        cookies[key] = morsel.value

    return cookies

def parse_new_url(url,page_number):
    url_parsed = urlparse(url)
    query_string = parse_qs(url_parsed.query)
    search_query_state = json.loads(query_string.get('searchQueryState')[0])
    search_query_state['pagination'] = {'currentPage': page_number}
    query_string.get('searchQueryState')[0] = search_query_state
    encoded_qs = urlencode(query_string, doseq=1)
    new_url = f"https://www.zillow.com/search/GetSearchPageState.htm?{encoded_qs}"
    return new_url

