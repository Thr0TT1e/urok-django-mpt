from django.db import models
from django.shortcuts import reverse


class Tags(models.Model):
	Tag_Name = models.CharField(max_length=50, verbose_name='Название тэга')

	class Meta:
		verbose_name = "Тег"
		verbose_name_plural = "Теги"

	def __str__(self):
		return self.Tag_Name

	def get_absolute_url(self):
		return reverse('tag_detail_url', kwargs={'Tag_id': self.pk})


class Notes(models.Model):
	Note_Title = models.CharField(max_length=50, verbose_name='Заголовок статьи')
	Note_Text = models.TextField(verbose_name='Текст статьи')
	Note_Pub_Date = models.DateField(verbose_name='Дата публикации')
	Note_Author = models.CharField(verbose_name='Автор статьи', max_length=15)
	Note_FK_Tag = models.ManyToManyField(Tags, verbose_name='Теги')

	class Meta:
		verbose_name = "Статья"
		verbose_name_plural = "Статьи"

	def __str__(self):
		return '{}, {}'.format(self.Note_Title, self.Note_Author)

	def get_absolute_url(self):
		return reverse('note_detail_url', kwargs={'Note_id': self.pk})

	def get_update_url(self):
		return reverse('note_update_url', kwargs={'Note_id': self.pk})

	def get_delete_url(self):
		return reverse('note_delete_url', kwargs={'Note_id': self.pk})

	def get_create_url(self):
		return reverse('create_note_url', kwargs={'Note_id': self.pk})


class Comments(models.Model):
	Comment_Author = models.CharField(verbose_name='Автор комментария', max_length=50)
	Comment_Text = models.TextField(verbose_name='Текст комментария', max_length=144)
	Comment_Pub_DateTime = models.DateTimeField(verbose_name='Дата и время публикации')
	Comment_FK_Note = models.ForeignKey(to=Notes, on_delete=models.CASCADE, verbose_name='Статья')

	class Meta:
		verbose_name = "Комментарий"
		verbose_name_plural = "Комментарии"

