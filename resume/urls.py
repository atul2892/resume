from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('login/',views.loginLogic),
    path('logout/',views.logoutLogic),
    path('resume/<str:name>-<int:id>/',views.resume_Page),
    
    #User Dashboard
    path('user-dashboard/',views.user_dashboard),
    path('user-add-resume/',views.user_add_resume),
    path('user-update-resume/<int:id>/',views.user_update_resume),
    path('user-delete-resume/<int:id>/',views.user_delete_resume),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
