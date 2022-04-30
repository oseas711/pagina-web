
from django.urls import path, include
from .views import inicio,about_us, inicio,typography,buscar,Register, CustomLoginView
from django.conf.urls.static import static
from django.conf import settings
from .forms import loginForm
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', inicio, name='inicio'),
    #path('index/', index, name='inicio'),
    path('buscar/', buscar, name='buscar'),
    path('about_us/', about_us, name='perfilesdeempresas'),
    path('typography/', typography, name='perfileslaborales'),
    path('register/', Register.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='login.html',authentication_form=loginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
  ]

urlpatterns += static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
