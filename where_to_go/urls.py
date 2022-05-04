from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from places import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('place/<int:place_id>', views.retrive_place_by_id, name='place-by-id'),
    path('', views.show_map, name='map'),
    
    # Custom endpoints for django-tinymce HTML Editor
    path('tinymce/', include('tinymce.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)