from django.urls import path
from . import views


urlpatterns = [

    # path('login/', views.loginUser, name='login'),
    # path('logout/', views.logoutUser, name='logout'),
    # path('register/', views.registerUser, name='register'),
    #

]









from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root =settings.MEDIA_ROOT)