from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from core.settings.yasg import urlpatterns as doc_urls
from api.common.views import GlobalSeacrh

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/src/", include("api.doctors.urls")),
    path("api/v1/src/", include("api.clinics.urls")),
    path("api/v1/users/", include("api.users.urls")),
    path("search/", GlobalSeacrh.as_view(), name="global-search"),
]
urlpatterns += doc_urls

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
