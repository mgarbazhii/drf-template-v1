from django.urls import include, path
from users.urls import urlpatterns as user_urls


app_name = 'api'

urlpatterns = [
    # path('auth/', include('djoser.urls.jwt')),
    # path('', SpectacularSwaggerView.as_view(
    # url_name='schema'), name='swagger-ui'),
]
urlpatterns += user_urls
