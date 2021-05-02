from django.contrib import admin
from django.urls import path, include
from vtranscribe import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.MainView.as_view(), name='main-view'),
    path('upload/', views.file_upload_view, name='upload-view'),
    path('upload/transcribe/', views.transcribe),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
