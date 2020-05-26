from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
	path('detail/<int:id>/',views.post_detail,name='detail'),
	path('upsighn/',views.up_sighn,name='upsighn'),
	path('inlog/',views.in_log,name='inlog'),
	path('outlog/',views.out_log,name='outlog'),
	path('like/<int:id>/', views.add_like, name='like'),
	path('comment/<int:id>/', views.add_comment, name='comment'),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)