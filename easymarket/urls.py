
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
	url(r'^productos/',include('productos.urls')),
    url(r'^admin/', admin.site.urls),
]
