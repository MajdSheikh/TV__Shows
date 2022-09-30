from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('shows/new/', views.shows_new),
    path('shows/create/', views.create_shows),
    # path('shows/',views.display_table),
    path('shows/<int:show_id>/', views.display_shows),
    path('shows/<int:show_id>/edit', views.edit_show),
    path('shows/<int:show_id>/update/', views.update_show),
    path('shows/<int:show_id>/destroy', views.destroy_show),
]

