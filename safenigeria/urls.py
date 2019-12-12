from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view

# project's library/app imports
from .baseviews import UserCreationView, UserProfileView, change_password


urlpatterns = [
    path('safenigeria-admin-console/', admin.site.urls),
    path('accounts/login/', auth_view.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_view.LogoutView.as_view(), name='logout'),
    path('accounts/change-password/', change_password, name='update_password'),
    path('accounts/settings/<int:pk>/', UserProfileView.as_view(), name='profile'),
    path(
         'accounts/registration/', 
         UserCreationView.as_view(
                template_name='registration/register.html'), 
         name='register'
        ),

    # project's library/app url hooks
    path('', include('core.urls')),

    # third party library/app url hooks
    path('select2/', include('django_select2.urls')),
]




if settings.DEBUG:
    # when in development, use static_url as route to render
    # static files (user-uploaded files)
    urlpatterns += static(
        settings.STATIC_URL, 
        document_root=settings.STATIC_ROOT
    )

    # when in development, use media_url as route to render
    # media files (user-uploaded files)
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT
    )