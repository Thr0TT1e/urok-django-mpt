from django.contrib import admin
from .models import Tags, Notes, Comments

# Register your models here.

# admin.site.register(Comments)
admin.site.register(Tags)


class CommentsInLine(admin.TabularInline):
	model = Comments
	extra = 0


@admin.register(Notes)
class NoteAdmin(admin.ModelAdmin):
	list_display = ('Note_Title', 'Note_Text', 'Note_Author', 'Note_Pub_Date')
	# fields = ('Note_Title', 'Note_Text', ('Note_Author', 'Note_Pub_Date'), 'Note_FK_Tag')
	list_filter = ('Note_Author', 'Note_Pub_Date')
	inlines = [CommentsInLine]
	fieldsets = (
			('Описание', {
			'fields': [('Note_Title', 'Note_Author')]
		}),
			('Содержание', {
				'fields': ('Note_Text', ('Note_Pub_Date', 'Note_FK_Tag'))
			})
	)


@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
	list_display = ('Comment_Author', 'Comment_Text', 'Comment_FK_Note', 'Comment_Pub_DateTime')
	fields = ('Comment_Author', 'Comment_Text', 'Comment_FK_Note')
	list_filter = ('Comment_Author', 'Comment_Pub_DateTime')
	list_display_links = ['Comment_Author', 'Comment_FK_Note']
