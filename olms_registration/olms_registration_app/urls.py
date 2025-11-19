from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('insert/', views.insert_name, name='insert'),

    # AJAX URLs - NO register/ prefix
    path('get_areas/<int:division_id>/', views.get_areas, name='get_areas'),
    path('get_branches/<int:division_id>/<int:area_id>/', views.get_branches, name='get_branches'),
    # path('get_country/<int:id>/', views.get, name='get_areas'),
]
