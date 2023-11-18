from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

#Para las imagenes
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicio, name= "inicio"),
    path('login/', views.user_login, name="user_login"),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name="Logout"),
    path('register/', views.user_register, name="user_register"),
    path('editarPerfil/', views.editarPerfil, name="EditarPerfil"),
    path('cambiarContraseña/', views.CambiarContraseña.as_view(), name="CambiarContraseña"),
    
    path('pages/', views.BlogsListView.as_view(), name="blogs_list"),
    path('pages/crear', views.BlogsCreateView.as_view(), name="crear_blogs"),
    path('pages/<pk>', views.BlogsDetailView.as_view(), name="detalle_blog"),
    path('pages/<pk>/editar', views.BlogsUpdateView.as_view(), name="editar_blog"),
    path('pages/<pk>/eliminar', views.BlogsDeleteView.as_view(), name="eliminar_blog"),
]

urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
