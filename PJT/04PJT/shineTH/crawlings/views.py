from django.shortcuts import render, redirect, get_object_or_404
import time
import datetime
from .models import Comment


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException



    
# Create your views here.
def index(request):
    return render(request, "crawlings/index.html")


def crawling(request):
    company_name = request.GET.get('company_name')
    result = fetch_visible_comments(company_name)
    Comment.objects.bulk_create(result)
    return redirect('crawlings:index') # 작업 현황을 보여주는 페이지로 이동


def print_comment(request, company_code):
    # 댓글 출력
    # 분석 요약 출력
    pass



def fetch_visible_comments(company_name, limit=20, max_scroll=5):
    
    # 크롬 드라이버 옵션
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    # chrome_options.add_argument("--headless=new")

    # 이전 폴더의 크롬 드라이버 경로
    service = Service("chromedriver-win64\\chromedriver.exe")


    driver = webdriver.Chrome(service=service, options=chrome_options)

    # 1. Toss 메인 접속
    driver.get("https://www.tossinvest.com/")
    time.sleep(1)

    # 2. 회사명 검색
    body = driver.find_element(By.TAG_NAME, "body")
    body.send_keys("/")  # '/' 입력 → 검색창 열림
    time.sleep(1)

    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='검색어를 입력해주세요']")
        )
    )
    search_input.send_keys(company_name)
    search_input.send_keys(Keys.ENTER)
    time.sleep(1)

    # 3. 종목 코드 추출
    WebDriverWait(driver, 15).until(EC.url_contains("/order"))
    current_url = driver.current_url
    stock_code = current_url.split("/")[
        current_url.split("/").index("stocks") + 1
    ]

    # 4. 커뮤니티 페이지 접속
    community_url = f"https://www.tossinvest.com/stocks/{stock_code}/community"
    driver.get(community_url)
    time.sleep(1)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "main article"))
    )
    #회사 이름, 회사코드
    companyName = ""
    companyCode = ""

    tempBlocks = driver.find_elements(
        By.CSS_SELECTOR, "div._1sivumi0 span.tw-1r5dc8g0"
    )
    companyName = tempBlocks[0].text.strip()
    companyCode = tempBlocks[1].text.strip()

    # 5. 블록 수집 (스크롤 반복하며 누적)
    last_height = driver.execute_script("return document.body.scrollHeight")
    
    # 수집할 데이터 목록
    scrape_map = [
        {'name': 'content', 'selector': 'span.tw-1r5dc8g0._1sihfl60', 'type': 'text', 'default' : ""},
        {'name': 'content', 'selector': 'span.tw-1r5dc8g0._60z0ev1', 'type': 'text', 'default' : ""},
        {'name': 'nickname', 'selector': 'label.xdogm43 span.tw-1r5dc8g0', 'type': 'text', 'default' : ""},
        {'name': 'post_time', 'selector': 'time._1tvp9v40', 'type': 'attribute', 'attr': 'datetime', 'default' : ""},
        {'name': 'ttabong', 'selector': 'span.tw-1r5dc8g0._3z3wnf1', 'type': 'text', 'default' : "0"},
        {'name': 'ZZal', 'selector': 'img', 'type': 'attribute', 'attr': 'src', 'default' : ""},
    ]

    # 최종 수집 데이터를 담을 리스트
    all_comments_data = []
    # 중복 확인 용
    visited = set(Comment.objects.values_list('nickname', 'post_time'))
    # 스크롤 하기
    for _ in range(max_scroll):

        # 스크롤 다운
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )
        time.sleep(1)
        tempBlocks = driver.find_elements(
            By.CSS_SELECTOR, "article.comment.xdogm41"
            )

        # tempBlocks는 이전에 find_elements로 찾아온 댓글 블록 리스트라고 가정
        for tempBlock in tempBlocks:
            # 한 댓글의 데이터를 저장할 딕셔너리
            scraped_data = {}

            # 위에서 만든 '지도'를 따라 반복 실행
            for item in scrape_map:
                data = item['default']  # 기본값 설정
                try:
                    element = tempBlock.find_element(By.CSS_SELECTOR, item['selector'])
                    # 타입에 따라 다른 방식으로 데이터 추출
                    if item['type'] == 'text':
                        data = data + element.text.strip()
                    elif item['type'] == 'attribute':
                        data = element.get_attribute(item['attr'])
                        if item['name'] == 'post_time':
                            if data:
                                data = datetime.datetime.fromisoformat(data)

                except NoSuchElementException:
                    # 요소를 찾지 못하면 기본값(None)을 유지하고 그냥 넘어감
                    pass
                
                # 결과 딕셔너리에 저장
                scraped_data[item['name']] = data

            scraped_data['company_name'] = companyName
            scraped_data['company_code'] = companyCode
            # 완성된 한 댓글의 데이터를 최종 리스트에 추가
            visitedData =  (scraped_data['nickname'], scraped_data['post_time']) 
            if visitedData not in visited:
                visited.add(visitedData)
                comment_obj = Comment(**scraped_data)
                all_comments_data.append(comment_obj)
        if len(all_comments_data) > limit:
            break
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:  # 더 이상 내려갈 게 없으면 종료
            break
        last_height = new_height

    # 최종 결과 확인
    
    driver.quit()
    print("검색완료")
    return all_comments_data

