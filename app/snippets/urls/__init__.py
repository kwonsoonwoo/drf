from django.urls import path, include

# /snippets/snippets/
# /snippets/snippets/<pk>/

# /snippets/django_view/snippets/
# /snippets/django_view/snippets/<pk>

# /snippets/api_view/snippets/
# /snippets/api_view/snippets/<pk>/

from . import django_view, api_view, mixins, generic_cbv, viewsets_router

app_name = 'snippets'
urlpatterns = [
    # config.urls를 참조
    path('django_view/', include(django_view)),
    path('api_view/', include(api_view)),
    path('mixins/', include(mixins)),
    path('generic_cbv/', include(generic_cbv)),
    path('viewsets_router/', include(viewsets_router)),
]