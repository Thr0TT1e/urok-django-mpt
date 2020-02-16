from django.urls import include, path
from django.http import response
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('Note/<int:Note_id>/', views.detail, name='note_detail_url'),
	path('Note/create', views.NoteCreate.as_view(), name='create_note_url'),
	path('Note/<int:Note_id>/update', views.NoteUpdate.as_view(), name='note_update_url'),
	path('Note/<int:Note_id>/delete', views.NoteDelete.as_view(), name='note_delete_url'),
	path('tags/', views.tag_list, name='tag_list_url'),
	path('tags/<int:Tag_id>/', views.tag_detail, name='tag_detail_url'),
]
