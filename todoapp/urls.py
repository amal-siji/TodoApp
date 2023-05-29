from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('addtask', views.Addtask,name='addtask'),
    path('userhome/',views.userhome,name="userhome"),
    path('edit/<int:id>/',views.edittask,name="edit"),
    path('delete/<int:id>',views.Deletetask,name="delete"),
    # path('del/<str:item_id>', views.remove, name="del"),
   
   
   
    path('register/', views.registration, name='register'),
    path('login', views.login, name="login"),
    path('logout', views.logout_user, name="logout"),
    
    

]
