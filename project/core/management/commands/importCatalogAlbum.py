
from django.core.management.base import BaseCommand
import json
from django.core.files import File
import os
import uuid

from catalog.models import CatalogAlbum, CatalogImage, ProductSize, Color, AlbumImageThrough
class Command(BaseCommand):
    def handle(self, *args, **options):
        print('importCatalogAlbum')
        with open('catalogAlbumExp.json',encoding="utf8") as mfile:
            data = json.load(mfile)
            print(data)
            for album in data:
                album_id = album['id']
                albumObj, created = CatalogAlbum.objects.get_or_create(pk=album_id)
                print('Album ', albumObj.id, ' created: ', created)
                albumObj.title = album['title']
                albumObj.slug = album['slug']
                albumObj.description = album['description']
                albumObj.fotter = album['fotter']
                albumObj.keywords = album['keywords']
                albumObj.save()
                
                images = album['images']
                for image in images:
                    image_id = image['id']
                    imageObj, created = CatalogImage.objects.get_or_create(pk=image_id)
                    print('Image ', imageObj.id, ' created: ', created)
                    imageObj.title = image['title']
                    imageObj.description = image['description']
                    imageObj.title = image['title']
                    
                    imageObj.save()
                    colors = image['colors']
                    for color in colors:
                        color_id = color['id']
                        colorObj, created = Color.objects.get_or_create(pk= color_id)
                        print('Color ', colorObj.id, ' created: ', created)
                        colorObj.name = color['name']
                        colorObj.color = color['clr']
                        colorObj.save()
                        imageObj.colors.add(colorObj)
                    
                    imageObj.save()
                    sizes = image['sizes']
                    for size in sizes:
                        size_id = size['id']
                        sizeObj, created = ProductSize.objects.get_or_create(pk=size_id)
                        print('size ', sizeObj.id, ' created: ', created)
                        sizeObj.size = size['size']
                        sizeObj.code = size['code']
                        sizeObj.save()
                        imageObj.sizes.add(sizeObj)
                    albumImageThrough, created = AlbumImageThrough.objects.get_or_create(image=imageObj, catalog=albumObj)
                    print('albumImageThrough',albumImageThrough.id,' created: ',created)
                    imageObj.albumimagethrough_set.add(albumImageThrough)
                    imageObj.save()
                    
                    #filename =  image['url'][len('/media/'):]
                    #path = "C:/Users/ronio/Desktop/projects/BeGoodPlus3/begoodPlus/static/media_root/"+ filename
                    #imageObj.image.save(filename, File(open(path)))
                    
            #json_data = json.parse(data)
            #print(json_data)
        pass