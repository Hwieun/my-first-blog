from django import forms
from .models import Post

#ModelForm. django에게 알려줌
class PostForm(forms.ModelForm):
    #이 form을 만들기 위해 어떤 model이 쓰여야 하는지 장고에게 알려줌
    class Meta:
        model = Post
        #이 Form에 title, text를 넣음
        fields = ('title', 'text')
