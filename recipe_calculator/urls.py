from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from recipe_calculator import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("recipes/", include("recipes.urls")),
    path("", include("layout.urls")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "layout.views.not_found"
handler500 = "layout.views.server_error"
