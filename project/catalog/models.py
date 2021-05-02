from django.db import models
from django.utils.translation import gettext_lazy  as _

# Create your models here.




class CatalogImage(models.Model):
    title = models.CharField(max_length=120, verbose_name=_("title"), unique=False)
    description = models.TextField(verbose_name=_("description"))
    
    image = models.ImageField(verbose_name=_("image"))
    #colors = models.ManyToManyField(to=Color)
    #sizes = models.ManyToManyField(to=ProductSize)
    
    NO_DISCOUNT = ''
    DISCOUNT_10_PRES = '/static/assets/catalog/imgs/discount_10.gif'
    DISCOUNT_20_PRES = '/static/assets/catalog/imgs/discount_20.gif'
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)
    class Meta(object):
        ordering= ['my_order',]


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