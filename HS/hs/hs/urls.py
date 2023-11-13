
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
import item.urls

from core.views import index, contact
from core import views


urlpatterns = [
    path('', index, name='index'),
    path('.core', include('core.urls')),
    path('items/', include('item.urls')),
    path('contact/', contact, name='contact'),
    #path('signup/',views.signup, name='signup'),
    
    path('admin/', admin.site.urls),
    

            ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
