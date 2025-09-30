from django.db import models

# Create your models here.

class Comment(models.Model):
    
    nickname = models.CharField(max_length = 15) # 사용자
    content = models.TextField() # 댓글 내용
    post_time = models.DateTimeField() # 댓글 단 시간
    ttabong = models.IntegerField() # 좋아요 수
    ZZal = models.CharField(blank = True, null = True) # 이미지 링크
    company_name = models.CharField() # 회사 이름
    company_code = models.CharField(max_length=7) # 회사 코드


class Analyst(models.Model):

    company_name = models.CharField() # 회사 이름 
    context_analyst = models.TextField() # GPT 분석 
    save_date = models.DateTimeField(auto_now_add = True) # 분석 날짜
