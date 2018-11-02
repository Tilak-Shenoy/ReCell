from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('search', views.search, name='search'),
    path('login', views.login, name='login'),
    path('display', views.display, name='display'),
    path('products', views.products, name='products'),
    path('register', views.register, name='register'),
    path('productReg', views.productReg, name='productReg'),

    # static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
]
