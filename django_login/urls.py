from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    # You could give template_name='some_other_login_page' argument too, if you wanted to.
    path('', LoginView.as_view(next_page=settings.LOGIN_REDIRECT_URL), name='home_login'),

    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('tili/', include('tilit.urls')),
]