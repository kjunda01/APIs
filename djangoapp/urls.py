from . import views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


urlpatterns = [
    path ('create', views.addUser),
    path ('read/<str:pk>', views.getUser),
    path ('update/<str:pk>', views.updateUser),
    path ('delete/<str:pk>', views.deleteUser),
    path ('', views.getData),
    #path ('', TemplateView.as_view(template_name='index.html')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
