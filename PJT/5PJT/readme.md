## 설계
### 기능 1
- 회원가입
- 로그인
- 로그아웃

### 기능 2 
- 사용자별 관심종목 저장 기능
- 관심종목 관리 (추가 삭제 조회)
- 관심종목 클릭시 댓글데이터 크롤링


### 모델 1
- 모델명 : accounts
- userid : charfield(varchar=20)
- nickname : charfield(varchar=100, unique=True)
- password1 : 
- password2 : 


### 모델 2
- 모델명 : favorites
- nickname : 
- company_name :
- create_at :
- supfav : 



기본페이지
- nav(회원가입 + 로그인 / 프로필 + 로그아웃,  댓글 분석 페이지)
- body: 비회원 -> 로그인을 통해 관심종목을 사용해보세요   /  회원 - 홈페이지 
- 홈페이지 : 관심 종목 출력 및 종목명 검색하여 관심종목 등록 가능
