from django.urls import path
from portfolio import views

# from django.urls import path
# from .views import projects, post_detail

# urlpatterns = [
#     path('',views.home,name='home'),
#     path('about',views.about,name='about'),
#     path('contact',views.contact,name='contact'),
#     path('blog',views.handleblog,name='handleblog'),
#     path('internshipdetails',views.internshipdetails,name='internshipdetails'),
#     path('projects/', projects, name='projects'),
#     path('blog/<int:post_id>/', post_detail, name='post_detail'),
# ]


urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
   
    path('contact/',views.contact,name='contact'),
    # path('project',views.project,name='project'),
    path('blog/',views.handleblog,name='handleblog'),
    path('internshipdetails',views.internshipdetails,name='internshipdetails'),
    
]
