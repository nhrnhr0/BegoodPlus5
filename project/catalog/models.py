from django.db import models
from django.utils.translation import gettext_lazy  as _

# Create your models here.
class CatalogAlbum(models.Model):
    title = models.CharField(max_length=120, verbose_name=_("title"))
    slug = models.SlugField(max_length=120, verbose_name=_("slug"))
    description= models.TextField(verbose_name=_('description'), default='', blank=True)
    fotter = models.TextField(verbose_name=_('fotter'), default='', blank=True)
    keywords = models.TextField(verbose_name=_('keyworks'), default='', blank=True)
    
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)
    #images = models.ManyToManyField(to=CatalogImage, related_name='album', blank=True, through='ThroughImage')
    
    class Meta(object):
        ordering = ['my_order']
        
    def __str__(self):
        return self.title
    
    def __unicode__(self):
        return self.title