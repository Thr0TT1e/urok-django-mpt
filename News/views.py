from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.urls import reverse
from django.shortcuts import redirect
from django.views.generic import View
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


def index(request):
	Notes_content = Notes.objects.all()
	context = {'Notes_content': Notes_content, }
	return render(request, 'News/index.html', context)


def detail(request, Note_id):
	try:
		note = Notes.objects.get(pk=Note_id)
	except Notes.DoesNotExist:
		raise Http404('Данной статьи не существует!!!')
	return render(request, 'News/detail.html', {'note': note, 'admin_panel': note, 'detail': True})


def tag_list(request):
	tag_list = Tags.objects.all()
	context = {'tags': tag_list, }
	return render(request, 'News/tag_list.html', context)


def tag_detail(request, Tag_id):
	# tag = get_object_or_404(Tags, Tag_id)
	try:
		tag = Tags.objects.get(pk=Tag_id)
	except Tags.DoesNotExist:
		raise Http404('Данной статьи не существует!!!')
	context = {'Tag': tag, }
	return render(request, 'News/tag_detail.html', context)


class NoteCreate(LoginRequiredMixin, View):
	model_form = NoteForm
	template = 'News/note_create_form.html'
	raise_exception = True

	def get(self, request, *args, **kwargs):
		form = self.model_form()
		return render(request, self.template, context={'form': form})

	def post(self, request, *args, **kwargs):
		bound_form = self.model_form(request.POST)

		if bound_form.is_valid():
			new_object = bound_form.save()
			return redirect(new_object)
		return render(request, self.template, context={'form': bound_form})


class NoteUpdate(LoginRequiredMixin, View):
	raise_exception = True

	def get(self, request, Note_id):
		Note_obj = Notes.objects.get(pk=Note_id)
		bound_form = NoteForm(instance=Note_obj)
		return render(request, 'News/note_update_form.html', context={'form': bound_form, 'Note': Note_obj})

	def post(self, request, Note_id):
		Note_obj = Notes.objects.get(pk=Note_id)
		bound_form = NoteForm(request.POST, instance=Note_obj)

		if bound_form.is_valid():
			new_obj = bound_form.save()
			return redirect(new_obj)
		return render(request, 'News/note_update_form.html', context={'form': bound_form, 'Note': Note_obj})


class NoteDelete(LoginRequiredMixin, View):
	raise_exception = True

	def get(self, request, Note_id):
		Note_obj = Notes.objects.get(pk=Note_id)
		return render(request, 'News/note_delete_form.html', context={'Note': Note_obj})

	def post(self, request, Note_id):
		Note_obj = Notes.objects.get(pk=Note_id)
		Note_obj.delete()
		return redirect(reverse('index'))
