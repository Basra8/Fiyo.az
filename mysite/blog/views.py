from csv import reader
from django.views import generic
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'base.html'

def index(request):
    return reader(request, 'index.html')

#class PostDetail(generic.DetailView):
   # model = Post
   #template_name = 'post_detail.html'
