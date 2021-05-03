from django.db import models
from django.utils.translation import gettext_lazy  as _
from colorfield.fields import ColorField

# Create your models here.


class Color(models.Model):
    name = models.CharField(max_length=30, verbose_name=_('color name'), unique=True)
    color = ColorField(verbose_name=_('color'), default='#FF0000')
    def __str__(self):
        return self.name

class ProductSize(models.Model):
    size = models.CharField(_('size'), default='X', max_length=30, unique=True)
    code = models.CharField(_('code'), default=0, max_length=2)
    class Meta():
        ordering = ('code',)
    def __str__(self):
        return self.size + ' (' + self.code + ')'


class CatalogImage(models.Model):
    title = models.CharField(max_length=120, verbose_name=_("title"), unique=False)
    description = models.TextField(verbose_name=_("description"))
    
    image = models.ImageField(verbose_name=_("image"), upload_to='CatalogImage')
    colors = models.ManyToManyField(to=Color)
    sizes = models.ManyToManyField(to=ProductSize)
    
    NO_DISCOUNT = ''
    DISCOUNT_10_PRES = '/static/assets/catalog/imgs/discount_10.gif'
    DISCOUNT_20_PRES = '/static/assets/catalog/imgs/discount_20.gif'
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)
    class Meta(object):
        ordering= ['my_order',]
        pass


    DISCOUNT_TYPES = [
        (NO_DISCOUNT, 'ללא הנחה'),
        (DISCOUNT_10_PRES, '10% הנחה'),
        (DISCOUNT_20_PRES, '20% הנחה'),
    ]
    discount = models.CharField(max_length=50, choices=DISCOUNT_TYPES, default=NO_DISCOUNT, null=True, blank=True)
    
    def __str__(self):
        return self.title



class CatalogAlbum(models.Model):
    title = models.CharField(max_length=120, verbose_name=_("title"))
    slug = models.SlugField(max_length=120, verbose_name=_("slug"))
    description= models.TextField(verbose_name=_('description'), default='', blank=True)
    fotter = models.TextField(verbose_name=_('fotter'), default='', blank=True)
    keywords = models.TextField(verbose_name=_('keyworks'), default='', blank=True)
    
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)
    #images = models.ManyToManyField(to=CatalogImage, related_name='album', blank=True, through='ThroughImage')
    images = models.ManyToManyField(to=CatalogImage, through='AlbumImageThrough')
    
    class Meta(object):
        ordering = ['my_order',]
        
    def __str__(self):
        return self.title
    
    def __unicode__(self):
        return self.title
        



class AlbumImageThrough(models.Model):
    catalog = models.ForeignKey(CatalogAlbum, on_delete=models.CASCADE)
    image = models.ForeignKey(to=CatalogImage, on_delete=models.CASCADE)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)
    class Meta(object):
        ordering = ['my_order',]