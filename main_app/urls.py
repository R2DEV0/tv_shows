from django.urls import path
from . import views

urlpatterns = [
    path('', views.shows),
    path('show_info/<int:show_id>', views.show_info),
    path('edit_show/<int:show_id>', views.edit_show),
    path('submit_edit', views.submit_edit),
    path('delete/<int:show_id>', views.delete),
    path('add_show', views.add_show),
    path('submit_new_show', views.submit_new_show),
    
]