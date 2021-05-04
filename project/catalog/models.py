from django.db import models
from django.utils.translation import gettext_lazy  as _
from colorfield.fields import ColorField
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import Thumbnail, SmartResize, ResizeToFill
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

#a.image.save('temp2.png', File(open(r'C:/Users/ronio/Downloads/trans_images/temp9.png','rb',encoding="utf16")))
class CatalogImage(models.Model):
    title = models.CharField(max_length=120, verbose_name=_("title"), unique=False)
    description = models.TextField(verbose_name=_("description"))
    
    image = models.ImageField(verbose_name=_("image"), upload_to='CatalogImage')
    image_69 = ImageSpecField(source='image', processors=[SmartResize(69,69)], format='png',options={'quality': 50})
    image_248 = ImageSpecField(source='image', processors=[SmartResize(248,248)], format='png',options={'quality': 50})
    image_376 = ImageSpecField(source='image', processors=[SmartResize(376,376)], format='png',options={'quality': 50})
    '''
    image_100 = ImageSpecField(source='image', processors=[SmartResize(100,100)],format='png', options={'quality': 0})
    image_200 = ImageSpecField(source='image', processors=[SmartResize(200,200)],format='png', options={'quality': 0})
    image_300 = ImageSpecField(source='image', processors=[SmartResize(300,300)],format='png', options={'quality': 0})
    image_400 = ImageSpecField(source='image', processors=[SmartResize(400,400)],format='png', options={'quality': 0})
    image_500 = ImageSpecField(source='image', processors=[SmartResize(500,500)],format='png', options={'quality': 0})
    image_600 = ImageSpecField(source='image', processors=[SmartResize(600,600)],format='png', options={'quality': 0})
    image_700 = ImageSpecField(source='image', processors=[SmartResize(700,700)],format='png', options={'quality': 0})
    image_800 = ImageSpecField(source='image', processors=[SmartResize(800,800)],format='png', options={'quality': 0})
    image_900 = ImageSpecField(source='image', processors=[SmartResize(900,900)],format='png', options={'quality': 0})
    image_1000 = ImageSpecField(source='image', processors=[SmartResize(1000,1000)],format='png', options={'quality': 0})
    image_1100 = ImageSpecField(source='image', processors=[SmartResize(1100,1100)],format='png', options={'quality': 0})
    image_1200 = ImageSpecField(source='image', processors=[SmartResize(1200,1200)],format='png', options={'quality': 0})
    image_1300 = ImageSpecField(source='image', processors=[SmartResize(1300,1300)],format='png', options={'quality': 0})
    
    image_150 = ImageSpecField(source='image', processors=[SmartResize(150,150)],format='png', options={'quality': 0})
    image_250 = ImageSpecField(source='image', processors=[SmartResize(250,250)],format='png', options={'quality': 0})
    image_350 = ImageSpecField(source='image', processors=[SmartResize(350,350)],format='png', options={'quality': 0})
    image_450 = ImageSpecField(source='image', processors=[SmartResize(450,450)],format='png', options={'quality': 0})
    image_550 = ImageSpecField(source='image', processors=[SmartResize(550,550)],format='png', options={'quality': 0})
    image_650 = ImageSpecField(source='image', processors=[SmartResize(650,650)],format='png', options={'quality': 0})
    image_750 = ImageSpecField(source='image', processors=[SmartResize(750,750)],format='png', options={'quality': 0})
    image_850 = ImageSpecField(source='image', processors=[SmartResize(850,850)],format='png', options={'quality': 0})
    image_950 = ImageSpecField(source='image', processors=[SmartResize(950,950)],format='png', options={'quality': 0})
    
    image_69 = ImageSpecField(source='image', processors=[SmartResize(69,69)],format='png', options={'quality': 0})

    '''
    
    
    

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
    @property
    def sorted_image_set(self):
        return self.images.order_by('albumimagethrough__my_order')
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