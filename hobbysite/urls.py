from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from hobbysite.views import HomePageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wiki/', include('wiki.urls', namespace="wiki")),
    path('forum/', include('forum.urls', namespace = 'forum')),
    path('blog/', include('blog.urls', namespace = 'blog')),
    path('commissions/', include("commissions.urls", namespace='commissions')),
    path('merchstore/', include('merchstore.urls', namespace='merchstore')),
    path("accounts/", include("django.contrib.auth.urls")),
    path("profile", include("user_management.urls", namespace="user_management")),
    path("", HomePageView.as_view(), name="homepage") #homepage
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)