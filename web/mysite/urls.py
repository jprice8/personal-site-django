from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers

from blog import views as blog_views
from projects import views as project_views

# set up automatic API routing
router = routers.DefaultRouter()
router.register(r'blogApi', blog_views.PostViewSet)
router.register(r'projectApi', project_views.ProjectViewSet)

urlpatterns = [

    # langing page
    path('', blog_views.index, name='landing'),

    # contact form submission
    path('contact/', blog_views.contactForm, name='contact'),

    # API urls using automatic URL routing.
    path('', include(router.urls)),

    # blog 
    path('blog/', include('blog.urls')),

    # projects
    path('projects/', include('projects.urls')),

    # admin
    path('admin/', admin.site.urls),

    # markdownx
    re_path(r'^markdownx/', include('markdownx.urls')),
]
