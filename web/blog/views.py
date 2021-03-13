from django.shortcuts import render
from django.views import generic
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from rest_framework import viewsets

from .models import Post, Contact
from .serializers import PostSerializer


def index(request):
    return render(request, 'landing.html')

def contactForm(request):
    # process form here
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        message = request.POST['message']

        # create new contact instance
        m1 = Contact.objects.create(
            first_name=first_name, 
            last_name=last_name, 
            email=email, 
            message=message,
        )
        m1.save()

    return render(request, 'landing.html')


class PostList(generic.ListView):
    queryset = Post.objects.filter(
        status=1
    ).order_by(
        '-created_on'
    )
    template_name = 'blog/post_list.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


#### Posts filtered by hashtag
def filter_hashtag(request, hashtag):
    posts = Post.objects.filter(
        hashtags__name__contains=hashtag
    ).order_by(
        '-created_on'
    )

    context = {
        'hashtag': hashtag,
        'posts': posts
    }

    return render(request, 'post_hashtag.html', context)


#### API Views ####
class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    # get all posts that are marked "publish"
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @method_decorator(cache_page(60*60))
    def dispatch(self, *args, **kwargs):
        return super(PostViewSet, self).dispatch(*args, **kwargs)
