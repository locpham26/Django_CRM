from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from leads.views import LandingPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('leads/', include("leads.urls", namespace="leads")),
    path('', LandingPageView.as_view(), name='landing'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)