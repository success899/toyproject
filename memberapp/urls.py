from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from memberapp.views import hello_world, MemberCreateView, MemberDetailView, MemberUpdateView

app_name = 'memberapp'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),

    path('create/', MemberCreateView.as_view(), name='create'),
    path('detail/<int:pk>', MemberDetailView.as_view(), name='detail'),
    path('update/<int:pk>', MemberUpdateView.as_view(), name='update'),

    path('login/', LoginView.as_view(template_name='memberapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]