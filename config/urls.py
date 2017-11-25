from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [
    # Admin
    url(r'^admin/', admin.site.urls),
    # Core app
    url(r'^', include('apps.core.urls', namespace='core')),
    # Accounts app
    url(r'^accounts/', include('apps.accounts.urls', namespace='accounts')),

    url(
        r'reset/$',
        auth_views.PasswordResetView.as_view(),
        name='password_reset'
    ),
    url(
        r'reset/done/$',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done'
    ),
    url(
        r'reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),
    url(
        r'reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'
    ),
]
