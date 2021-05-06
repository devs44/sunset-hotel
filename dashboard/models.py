from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

# Create your models here.
ADULT = (
        ('1', '1 Adult'),
        ('2', '2 Adults'),
        ('3', '3 Adults'),
)
CHILDREN = (
    ('0', '0 child'),
    ('1', '1 child'),
    ('2', '2 children'),
    ('3', '3 children'),
)


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

    def delete(self, hard=False):
        if not hard:
            self.deleted_at = timezone.now()
            return super().save()
        else:
            return super().delete()


class About(TimeStamp):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="about")
    description = RichTextField()

    def __str__(self):
        return self.title


class Room_Category(TimeStamp):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Feature(TimeStamp):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to="features")

    class Meta:
        verbose_name = _('Feature')
        verbose_name_plural = _('Features')

    def __str__(self):
        return self.title


class Room(TimeStamp):
    room_type = models.ForeignKey(Room_Category, on_delete=models.CASCADE)
    room_no = models.CharField(
        max_length=250, primary_key=True)
    description = RichTextField()
    checked_in_date = models.DateField(null=True, blank=True)
    checked_out_date = models.DateField(null=True, blank=True)
    availability = models.BooleanField(default=False)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to="rooms")
    features = models.ManyToManyField(Feature)

    class Meta:
        verbose_name = _('Room')
        verbose_name_plural = _('Rooms')

    def __str__(self):
        return self.room_no


class RoomImage(TimeStamp):
    room = models.ForeignKey(
        Room, related_name="r_image", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="room")

    def __str__(self):
        return self.room.room_no


class Image(TimeStamp):
    image_type = models.ForeignKey(Room_Category, on_delete=models.CASCADE)
    caption = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery')

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')

    def __str__(self):
        return self.caption


class Testomonial(TimeStamp):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='Testimonials', null=True, blank=True)
    profession = models.CharField(max_length=255, null=True, blank=True)
    voice = models.TextField()

    class Meta:
        verbose_name = _('Testimonial')
        verbose_name_plural = _('Testimonials')

    def __str__(self):
        return self.name


class News(TimeStamp):
    title = models.CharField(max_length=1255)
    image = models.ImageField(upload_to="News")
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    view_count = models.PositiveIntegerField(default=0, null=True, blank=True)

    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('News')

    def __str__(self):
        return self.title


class Event(TimeStamp):
    title = models.CharField(max_length=1255)
    image = models.ImageField(upload_to="Events")
    description = RichTextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    view_count = models.PositiveIntegerField(default=0, null=True, blank=True)

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')

    def __str__(self):
        return self.title


class Comment(TimeStamp):
    full_name = models.CharField(max_length=30)
    email = models.EmailField()
    website = models.URLField(null=True, blank=True)
    room = models.ForeignKey(
        Room, related_name='room_comment', on_delete=models.CASCADE, null=True, blank=True)
    news = models.ForeignKey(
        News, related_name="news_comment", on_delete=models.CASCADE, null=True, blank=True)
    events = models.ForeignKey(
        Event, related_name="event_comment", on_delete=models.CASCADE, null=True, blank=True)
    comment = models.TextField()

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')

    def __str__(self):
        return self.full_name


class Contact(TimeStamp):
    address = models.CharField(max_length=100)
    phone = models.PositiveIntegerField()
    fax = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField()


class Message(TimeStamp):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        verbose_name = _('Message')
        verbose_name_plural = _('Messages')

    def __str__(self):
        return self.full_name


class Reservation(TimeStamp):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    selected_room = models.ForeignKey(
        Room, on_delete=models.CASCADE, null=True, blank=True)
    check_in_date = models.DateTimeField()
    check_out_date = models.DateTimeField()
    adult = models.CharField(max_length=250, choices=ADULT)
    children = models.CharField(max_length=250, choices=CHILDREN)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=40)
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=250, null=True, blank=True)
    country = models.CharField(max_length=40)
    special_req = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = _('Reservation')
        verbose_name_plural = _('Reservations')

    def __str__(self):
        return self.first_name + self.last_name


class Services_description(TimeStamp):
    description = models.CharField(max_length=200)
    service_video = models.FileField(upload_to="service_description")

    def __str__(self):
        return self.description


class Services_type(TimeStamp):
    service_type_name = models.CharField(max_length=100)
    service_png = models.ImageField(upload_to="service_type")
    service_type_description = models.CharField(max_length=200)

    def __str__(self):
        return self.service_type_name


class Subscription(TimeStamp):
    email = models.EmailField()

    def __str__(self):
        return self.email
