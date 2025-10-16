# test.py
import requests
import time
import random
from pathlib import Path

# === 설정 ===
COOKIE_STRING = "WMONID=QSTwK8_CKVu; lgnId=shine379@naver.com; JSESSIONID_HAKSAF=bInqTrDmJTjOufeuPcH6iaRGoEkZDWXAs66o0YyFkoMIy6TueDyC!1456852319!-2096080651!1760572649702"
BASE_PREFIX = "https://edu.ssafy.com/data/upload_files/crossUpload/openLrn/ebook/unzip/A2025101512361977200/assets/page-images/page-71b53e30-35547038-"
SAVE_DIR = Path("C:\\Users\\SSAFY\\Desktop")  # 저장할 폴더 이름
START_PAGE = 1
END_PAGE = 167  # 페이지 수 (마지막 페이지 번호 쓰면 됨)
# ============= 아래는 건들지 않아도 됩니다! 
# 혹시나 하면 User-Agent 만 뭐 Mozilla 어쩌고로 설정해주시면 될 듯

SAVE_DIR.mkdir(parents=True, exist_ok=True)

# 쿠키 파싱 하는 애
def parse_cookie_string(s):
    d = {}
    for p in s.split(";"):
        if "=" in p:
            k, v = p.split("=", 1)
            d[k.strip()] = v.strip()
    return d

# 세션 준비
session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://edu.ssafy.com/"
})
session.cookies.update(parse_cookie_string(COOKIE_STRING))

# 다운로드 실행
for i in range(START_PAGE, END_PAGE + 1):
    fname = f"{i:04d}.jpg"
    url = BASE_PREFIX + fname
    r = session.get(url, stream=True, timeout=15)
    if r.status_code == 200:
        path = SAVE_DIR / fname
        with open(path, "wb") as f:
            for chunk in r.iter_content(8192):
                f.write(chunk)
        print(f"[{i}] Saved {fname}")
    else:
        print(f"[{i}] Failed status={r.status_code}")
    # 요청 간 딜레이 (차단 방지) - 얘가 인간처럼 보이게 하는거니 꼬옥 잊지 말아주세요
    time.sleep(0.6 + random.random() * 0.4)
