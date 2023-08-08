from django.urls import path
from . import views

app_name = 'cats'
urlpatterns = [
    path('',views.home,name="home"),
    path('about/', views.about, name="about"),
    path('cats/',views.cats_index,name="index"),
    path('cats/<int:cat_id>/',views.cats_detail,name="detail"),
    path('cats/create',views.CreateCat.as_view(),name="create"),
    path('cats/<int:pk>/delete', views.DeleteCat.as_view(),name="delete"),
    path('cats/<int:pk>/update', views.UpdateCat.as_view(),name="update"),
]