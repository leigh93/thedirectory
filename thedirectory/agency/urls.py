from django.urls import path
from . import views

app_name = 'agency'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('search',views.search, name = 'search' ),
    path('<int:agency_id>/',views.agency_detail, name = 'agency_detail' ),

]