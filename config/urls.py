from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path, register_converter

from apps.core import views as core_views

from .converters import UidConverter, TokenConverter


register_converter(UidConverter, 'uid')
register_converter(TokenConverter, 'token')

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    # Core app
    path('', include('apps.core.urls', namespace='core')),
    # Tickets app
    path('tickets/', include('apps.tickets.urls', namespace='tickets')),
    # Login and Logout views
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    # Signup view
    path('signup/', core_views.signup, name='signup'),
    # My profile view
    path(
        'my_account/',
        core_views.UserUpdateView.as_view(),
        name='my_account'
    ),
    # Reset views
    path(
        'reset/',
        auth_views.PasswordResetView.as_view(),
        name='password_reset'
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done'
    ),
    path(
        'reset/<uid:uidb64>/<token:token>/',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),
    path(
        'reset/complete/',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'
    ),
]
