"""cs108 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static  # allows us to access static content not part of app
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hw/', include('hello_world.urls')),
    path('pages/', include('pages.urls')),  # link to urls in hello_world app
    path('quotes/', include('quotes.urls')),
    path('mini_fb/', include('mini_fb.urls')),
    path('green_biz/', include('green_biz.urls')), # links to urls in green_biz
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
