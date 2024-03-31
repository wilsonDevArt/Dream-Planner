from . import views
from  django.urls import path

urlpatterns = [
   path('', views.home, name="home"),
   path('register_page/', views.register_page, name="register_page"),
   path('login_page/', views.login_page, name="login_page"),
   path('logout_page/', views.logout_page, name="logout_page"),
   path('list_of_steps/<str:foo>', views.list_of_steps, name="list_of_steps"),
   path('delete_step/<int:pk>', views.delete_step, name="delete_step"),
   path('delete_dream/<int:pk>', views.delete_dream, name="delete_dream"),
   path('add_new_dream/', views.add_new_dream, name="add_new_dream"),
   path('add_step/<str:foo>', views.add_step, name="add_step"),
   path('edit_step/<int:pk>', views.edit_step, name="edit_step"),
   path('edit_dream/<int:pk>', views.edit_dream, name="edit_dream"),
]
