from django.db import models #django.db에서 models import
from django.utils import timezone

# 장고가 Post가 디비에 저장되어야 한다고 알게 된다
class Post(models.Model): #Post 모델 정의 #models Post가 장고 모델임을 의미
#모델 속성과 데이터 타입 정의
    #다른 모델에 대한 링크
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    #글자 수에 제한 있는 텍스트
    title = models.CharField(max_length=200)
    #글자 수에 제한 없는 긴  텍스트
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publich(self): #self가 this 포인터
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
