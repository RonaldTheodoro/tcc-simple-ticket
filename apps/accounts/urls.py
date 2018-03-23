from django.urls import path

from . import views


app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('my_account/', views.UserUpdateView.as_view(), name='my_account'),
]
