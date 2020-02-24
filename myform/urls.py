from django.urls import path
from myform import views
from myform.views import ClassViews
urlpatterns = [
    path('form/', views.form_test),
    #视图
    path('fun_views/', views.fun_views),
    path('class_view/', ClassViews.as_view()),
]