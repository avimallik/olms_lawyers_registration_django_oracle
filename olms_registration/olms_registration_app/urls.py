from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('insert/', views.insert_name, name='insert'),

    path('api/test/', include('test_api.urls')),
    path("api/register/", views.api_register),

    # AJAX URLs - NO register/ prefix
    path('get_areas/<int:division_id>/', views.get_areas, name='get_areas'),
    path('get_branches/<int:division_id>/<int:area_id>/', views.get_branches, name='get_branches'),
    path('get_division/', views.get_division, name="get_division"),
    path('get_country/', views.get_country, name="get_country"),
    path('get_member_bar_association/', views.get_member_bar_association, name="get_member_bar_association"),
    path('get_type_of_application/', views.get_type_of_application, name='get_type_of_application'),
    path('get_type_of_post/', views.get_type_of_post, name='get_type_of_post'),
    # path('get_country/<int:id>/', views.get, name='get_areas'),
]
