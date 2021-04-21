from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User 


# Create your models here.


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class About(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="about")
    slogan = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.title


class Room_Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


FEATURES = (
    (1, 'DOUBLE KING BED'),
    (2, 'BREAKFAST'),
    (3, 'AIR CONDITIONING'),
    (4, 'MINIBAR'),
    (5, 'WIFI SERVICE'),
    (6, 'FREE PARKING')
)


class Room(models.Model):
    room_type = models.ForeignKey(Room_Category, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to="rooms")
    features = models.CharField(max_length=200, choices=FEATURES)

    class Meta:
        verbose_name = _('Room')
        verbose_name_plural = _('Rooms')

    def __str__(self):
        return self.room_type


class Image(models.Model):
    image_type = models.ForeignKey(Room_Category, on_delete=models.CASCADE)
    caption = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
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


class Comment(TimeStamp):
    full_name = models.CharField(max_length=30)
    email = models.EmailField()
    website = models.CharField(max_length=255, null=True, blank=True)
    comment = models.TextField()

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')

    def __str__(self):
        return self.first_name + self.middle_name + self.last_name


class News(TimeStamp):
    title = models.CharField(max_length=1255)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="News")
    description = models.TextField()
    comment = models.ForeignKey(
        Comment, related_name='n_comment', on_delete=models.SET_NULL, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    view_count = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('News')

    def __str__(self):
        return self.title


class Event(TimeStamp):
    title = models.CharField(max_length=1255)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="Events")
    description = models.TextField()
    comment = models.ForeignKey(
        Comment, related_name="e_comment", on_delete=models.SET_NULL, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    view_count = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')

    def __str__(self):
        return self.title


class Contact(models.Model):
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    fax = models.CharField(max_length=30, null=True, blank=True)
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
    selected_room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateTimeField()
    check_out_date = models.DateTimeField()
    no_of_adults = models.CharField(max_length=255)
    no_of_children = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=40)
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=40)
    special_req = models.TextField()

    class Meta:
        verbose_name = _('Reservation')
        verbose_name_plural = _('Reservations')

    def __str__(self):
        return self.first_name + self.last_name
