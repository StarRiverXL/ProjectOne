"""jfcnproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from public import views as pub_index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^asset/', include('asset.urls')),
    url(r'^public/', include('public.urls')),
    url(r'^servers/', include('servers.urls')),
    url(r'^ywdocument/', include('ywdocument.urls')),
    url(r'^samllfun/', include('smallfun.urls')),
    url(r'^interface/', include('interface.urls')),
    url(r'^$', pub_index.checkuser),
    url(r'^index/', pub_index.indexpage),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # 图片访问地址




