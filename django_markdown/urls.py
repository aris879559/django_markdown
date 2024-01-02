"""
URL configuration for django_markdown project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django_markdown_doc import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('documents/', views.document_list, name='document_list'),
    path('document/<int:document_id>/', views.document_detail, name='document_detail'),
    path('document/new/', views.document_new, name='document_new'),
    path('document/<int:document_id>/edit/', views.document_edit, name='document_edit'),
    path('document/<int:document_id>/delete/', views.document_delete, name='document_delete'),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:  # 只在DEBUG模式下使用
    urlpatterns += static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)
