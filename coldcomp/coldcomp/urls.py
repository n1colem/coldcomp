"""coldcomp URL Configuration

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
from django.urls import path
from scraps.views import ScrapList, ScrapDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('scraps/', ScrapList.as_view(), name='scrap-list'),
#    path('scraps/add', ScrapCreate.as_view(), name='scrap-add'),
#    path('scraps/<int:pk>/edit', ScrapUpdate.as_view(), name='scrap-update'),
#    path('scraps/<int:pk>/delete', ScrapDelete.as_view(), name='scrap-delete'),
    path('scraps/<int:pk>', ScrapDetail.as_view(), name='scrap-detail'),
    path('scraps/<slug:slug>', ScrapDetail.as_view(), name='scrap-detail-slug'),
#    path('scraps/<slug:slug>/edit', ScrapUpdate.as_view(), name='scrap-update-slug'),
#    path('scraps/<slug:slug>/delete', ScrapDelete.as_view(), name='scrap-delete-slug'),
#    path('accounts/', include('django.contrib.auth.urls'))
]
