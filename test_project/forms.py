from django.forms import ModelForm
from test_project.models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['url', 'files']
