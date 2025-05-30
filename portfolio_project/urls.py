# portfolio_project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls', namespace='portfolio')),
    path('captcha/', include('captcha.urls')),
]