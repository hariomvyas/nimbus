from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from community import views


urlpatterns = [
    # Django admin
    path('h-j-m/', admin.site.urls),

    # User management
    path('account/', include('allauth.urls')),
    path('user/', include('users.urls')),
    path('console/', include('console.urls')),


    # Local apps
    path('accounts/', include('users.urls')),
    path('', include('pages.urls')),

    # Community app
    path('community/', include('community.urls')),

    # Services apps
    path('services/', include('services.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls))] + urlpatterns
