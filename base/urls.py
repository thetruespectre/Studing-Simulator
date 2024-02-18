from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path("classroom/<int:id>/", views.classroom, name="classroom"),
    
    path("create-classroom/", views.classroomCreate, name="create-classroom"),
    path("edit-classroom/<int:id>/", views.classroomEdit, name="edit-classroom"),
    path("delete-classroom/<int:id>/", views.deleteClassroom, name="delete-classroom"),
    path("create-subject/", views.subjectCreate, name="create-subject"),
    
    path("login/", views.loginForm, name="login"),
    path("logout/", views.logoutForm, name="logout"),
    path("register/", views.registerForm, name="register"),
    
    path("edit-message/<int:id>/", views.messageEdit, name="edit-message"),
    path("delete-message/<int:id>/", views.messageDelete, name="delete-message"),
]