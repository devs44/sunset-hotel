from django.contrib import admin
from .models import*
# Register your models here.


admin.site.register([Room, Room_Category, Feature, Event, Comment, Services_description,
                     Services_type, Image, News, RoomImage])
