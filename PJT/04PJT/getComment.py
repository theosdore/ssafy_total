import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# 크롬 드라이버 옵션
chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--headless=new")

# 이전 폴더의 크롬 드라이버 경로
service = Service("chromedriver-win64\\chromedriver.exe")


def fetch_visible_comments(company_name, limit=40, max_scroll=5):
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
    comments = set()
    blocks = []
    last_height = driver.execute_script("return document.body.scrollHeight")

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
        while tempBlocks:
            tempBlock = tempBlocks.pop()
            #제목
            commentTitle = tempBlock.find_element(
                By.CSS_SELECTOR, "span.tw-1r5dc8g0._1sihfl60"
            ).text.strip()
            #댓글본문
            comment = tempBlock.find_element(
                By.CSS_SELECTOR, "span.tw-1r5dc8g0._60z0ev1"
            ).text.strip()
            #작성자
            writer = tempBlock.find_element(
                By.CSS_SELECTOR, "label.xdogm43 span.tw-1r5dc8g0"
            ).text.strip()
            #작성날짜
            timeData = tempBlock.find_element(
                By.CSS_SELECTOR, "time._1tvp9v40"
            ).get_attribute('datetime')
            #좋아요 수
            liked = tempBlock.find_element(
                By.CSS_SELECTOR, "span.tw-1r5dc8g0._3z3wnf1"
            ).text.strip()
            #이미지 링크
            imgLink = tempBlock.find_element(
                By.CSS_SELECTOR, "img"
            ).get_attribute('src')
            
            totalText = commentTitle + comment
            if totalText not in comments:
                comments.add((totalText, writer, timeData, liked, imgLink, companyName, companyCode))
            if len(comments) >= limit:
                break
        if len(comments) >= limit:
            break

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:  # 더 이상 내려갈 게 없으면 종료
            break
        last_height = new_height
    

    driver.quit()
    return comments


if __name__ == "__main__":
    comments = fetch_visible_comments("삼성전자", limit=40)
    print("\n=== 커뮤니티 댓글 (최대 20개) ===")
    if not comments:
        print("댓글을 가져오지 못했습니다.")
    else:
        for item in comments:
            print(item)
