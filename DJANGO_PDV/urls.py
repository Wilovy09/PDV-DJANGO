from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from catalogo import views
from inventario import views as inventario_views
from punto_de_venta import views as puntodeventa_views
from pedidos_pendientes import views as pedidospendientes_views
from users import views as user_views

urlpatterns = [
    path('generar_pdf/', inventario_views.generar_pdf, name='generar_pdf'),
    path('admin/', admin.site.urls),

    #path('signup/', user_views.signup, name='signup'),
    path('logout/', user_views.signout, name='logout'),
    path('', user_views.signin, name='signin'),
    
    path('catalogo/', views.catalogo, name='catalogo'),
    path('inventario/', inventario_views.inventario, name='inventario'),
    path('puntodeventa/', puntodeventa_views.punto_de_venta, name='puntodeventa'),
    path('pedidospendientes/', pedidospendientes_views.pedidos_pendientes, name='pedidospendientes')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
