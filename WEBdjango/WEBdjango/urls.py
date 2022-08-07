
from django.contrib import admin
from django.urls import path
from mysite.views import verPaquetes, verHotel, verVuelo

urlpatterns = [
    path('admin/', admin.site.urls),
    path("viajes-paquetes/",verPaquetes),
    path("viajes-hotels/",verHotel),
    path("viajes-vuelos/",verVuelo),
]