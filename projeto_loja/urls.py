from django.contrib import admin
from django.urls import path
from app_loja import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('produtos/', views.produtos, name='produtos'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login_view, name='login'),
    path('contato/', views.contato, name='contato'),
    path('quemsomos/', views.quemsomos, name='quemsomos'),
    path('queropedir/', views.queropedir, name='queropedir'),
    path('pedidos/', views.pedidos, name='pedidos'),
    path('novopedido/', views.novopedido, name='novopedido'),
    path('perfil/', views.perfil, name='perfil'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('alterarsenha/', views.alterarsenha, name='alterarsenha'),
    path('excluir_pedido/<int:pedido_id>/', views.excluir_pedido, name='excluir_pedido'),
    path('politica-de-seguranca/', views.politica_seguranca, name='politica_seguranca'),  # Nova rota adicionada
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
