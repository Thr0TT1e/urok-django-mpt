from django import forms
from .models import *
from django.core.exceptions import ValidationError


class NoteForm(forms.ModelForm):
	class Meta:
		model = Notes
		fields = [
			'Note_Title',
			'Note_Text',
			'Note_Author',
			'Note_Pub_Date',
			'Note_FK_Tag',
		]
		widgets = {
			'Note_Title': forms.TextInput(attrs={'class': 'form-control'}),
			'Note_Text': forms.Textarea(attrs={'class': 'form-control'}),
			'Note_Author': forms.TextInput(attrs={'class': 'form-control'}),
			'Note_Pub_Date': forms.DateInput(attrs={'class': 'form-control'}),
			'Note_FK_Tag': forms.SelectMultiple(attrs={'class': 'form-control'}),
		}
