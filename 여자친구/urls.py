from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from 여자친구 import views

app_name = '여자친구'

urlpatterns = [
    # path('유주/', views.show_유주, name='유주.html'),
    # path('소원/', views.show_소원, name='소원.html'),
    # path('예린/', views.show_예린, name='예린.html'),
    # path('신비/', views.show_신비, name='신비.html'),
    # path('엄지/', views.show_엄지, name='엄지.html'),
    # path('은하/', views.show_은하, name='은하.html'),
    path('<멤버>/', views.show_멤버, name='멤버.html'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)