from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("my_blog.urls")),
    path('api/', include('blog.api.urls')),

]
