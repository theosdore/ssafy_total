from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import FavoriteCompanyForm
from django.contrib import messages
from .models import FavoriteCompany


import datetime
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException


def index(request):
    companyLst = FavoriteCompany.objects.filter(nickname=request.user).order_by("company_name")
    context = {
        'companyLst' : companyLst
    }
    return render(request, 'favorites/index.html', context)

# @login_required
def addFavCompany(request):
    company_name = request.GET.get('stock_name')
    
    if not company_name:
        messages.warning(request, "검색어를 입력해주세요")
        return redirect("favorites:index") 
    # 크롬 드라이버 옵션
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--headless=new")

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
    try:
        WebDriverWait(driver, 4).until(EC.url_contains("/order"))
    except TimeoutException:
        driver.quit()
        messages.warning(request, "해당 이름으로 저장된 회사는 없습니다")
        return redirect("favorites:index")
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
    #회사 이름
    companyName = ""

    tempBlocks = driver.find_element(
        By.CSS_SELECTOR, "div._1sivumi0 span.tw4k-1r5dc8g0"
    )
    companyName = tempBlocks.text.strip()
    
    form = FavoriteCompanyForm({'company_name':companyName})

    if form.is_valid():
        favorite = form.save(commit=False)
        favorite.nickname = request.user
        favorite.save()
        messages.warning(request, "등록되었습니다")
    else:
        messages.warning(request, "등록 실패하였습니다")
    return redirect("favorites:index")


def deleteFav(request, fav_id):
    if request.method == 'POST':
        FavC = get_object_or_404(FavoriteCompany, pk=fav_id)
        if FavC.nickname == request.user:
            # 4. 객체 삭제
            FavC.delete()
            # messages.success(request, "즐겨찾기에서 삭제되었습니다.") # (선택) 성공 메시지
        else:
            # 권한이 없는 경우 처리
            # messages.error(request, "삭제할 권한이 없습니다.")
            pass
    return redirect('favorites:index')