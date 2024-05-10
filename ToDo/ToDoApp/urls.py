from django.urls import path
from ToDoApp import views

urlpatterns = [
    path('',views.SignUpPage,name="SignUpPage"),
    path('HomePage/',views.HomePage,name="HomePage"),
    path('SignupPage/',views.SignupPage,name="SignupPage"),
    path('LoginUser/',views.LoginUser,name="LoginUser"),
    path('user_logout/',views.user_logout,name="user_logout"),
    path('psave/',views.psave,name="psave"),
    path('Tsave/',views.Tsave,name="Tsave"),
    path('Task_Page/<T>/',views.Task_Page,name="Task_Page"),
    path('deltask/<int:tid>/',views.deltask,name="deltask"),
    path('upadtetask/<int:uid>/',views.upadtetask,name="upadtetask"),
    path('EditPage/<int:uid>/',views.EditPage,name="EditPage"),
    path('delProject/<int:pid>/',views.delProject,name="delProject"),
]