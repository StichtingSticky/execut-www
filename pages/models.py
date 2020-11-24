from django.db import models
from precise_bbcode.fields import BBCodeTextField
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from tinymce import models as tinymce_models

class StaticPage(models.Model):

    # I examined the current website of execut and tried to let build everything as closely resembling that website 
    # as possible, so any 'weird' properties in this model should be attributed to that.

    # So, every page is of course connected to a core.Site. 

    sites = models.ManyToManyField('core.Site', related_name='pages')
    name = models.CharField(max_length=300)
    hero_text = tinymce_models.HTMLField(verbose_name='hero-tekst', default=None, null=True, blank=True)
    hero_button_enabled = models.BooleanField(verbose_name='schakel knop onder hero-tekst in', default=False)
    hero_button_text = models.CharField(verbose_name='tekst van de knop onder de hero-tekst', null=True, blank=True, max_length=300)
    hero_button_link = models.URLField(verbose_name='koppeling achter de knop onder de hero-tekst', null=True, blank=True, max_length=300)
    body = tinymce_models.HTMLField(verbose_name='inhoud', default=None, null=True)
    include_in_menu = models.BooleanField(verbose_name='laat zien in menu', default=True)
    order = models.IntegerField(verbose_name='volgorde')
    is_two_column_page = models.BooleanField(verbose_name='pagina heeft twee kolommen', default=False)
    second_column_body = tinymce_models.HTMLField(verbose_name='inhoud van tweede kolom', default=None, null=True, blank=True)
    visible = models.BooleanField(default=True, verbose_name='zichtbaar')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='aanmaakdatum')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    slug = models.SlugField(verbose_name='slug', unique=True)

    def __str__(self):
        return self.name

    def get_admin_url(self):
        content_type = ContentType.objects.get_for_model(self.__class__)
        return reverse('admin:%s_%s_change' % (content_type.app_label, content_type.model), args=(self.id,))