from django.urls import path

from memberapp.views import hello_world, MemberCreateView

app_name = 'memberapp'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),

    path('create/', MemberCreateView.as_view(), name='create'),
]