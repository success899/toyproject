from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from memberapp.views import MemberCreateView, MemberDetailView, MemberUpdateView, MemberDeleteView

app_name = 'memberapp'

urlpatterns = [
    path('create/', MemberCreateView.as_view(), name='create'),
    path('detail/<int:pk>', MemberDetailView.as_view(), name='detail'),
    path('update/<int:pk>', MemberUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', MemberDeleteView.as_view(), name='delete'),

    path('login/', LoginView.as_view(template_name='memberapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]