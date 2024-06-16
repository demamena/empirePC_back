from django.contrib.auth.models import AbstractUser
from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class Customer(AbstractUser):
    first_name = models.CharField(max_length=80)
    middle_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    phone = models.CharField(max_length=100)
    bonus = models.IntegerField(default=0)
    birthday = models.DateField(blank=True, null=True)

    groups = None
    user_permissions = None

    def __str__(self):
        return f'{self.id}. {self.email}'


class Order(models.Model):
    DELIVERY_TYPES = [
        ('post', 'Post'),
        ('postal_carrier', 'Postal Carrier'),
        ('personal_delivery', 'Personal Delivery'),
    ]

    ORDER_TYPES = [
        ('build', 'Build Order'),
        ('cleaning', 'PC Cleaning'),
        ('upgrade', 'PC Upgrade'),
    ]

    STATUS_TYPES = [
        ('received', 'Received for processing'),
        ('confirmed', 'Confirmed'),
        ('finished', 'Finished'),
        ('canceled', 'Canceled'),
    ]

    PC_TYPES = [
        ('pc', 'PC'),
        ('notebook', 'Notebook')
    ]

    GRAPHIC_CARD_TYPES = [
        ('intel', 'Intel'),
        ('amd', 'AMD'),
        ('nvidia', 'Nvidia'),
    ]

    PROCESSOR_TYPES = [
        ('intel', 'Intel'),
        ('amd', 'AMD'),
    ]

    COOLING_TYPES = [
        ('air', 'Air cooling'),
        ('water', 'Water Cooling'),
        ('custom', 'Custom cooling'),
    ]

    OS_TYPES = [
        ('windows', 'Windows'),
        ('linux', 'Linux'),
        ('without', 'Without OS'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True, related_name='orders')
    phone = models.CharField(max_length=100)
    date = models.DateField(auto_created=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    preferences = models.TextField(blank=True, null=True)
    wishes = models.TextField(blank=True, null=True)
    call_time = models.CharField(max_length=20, blank=True, null=True)
    delivery_type = models.CharField(max_length=20, choices=DELIVERY_TYPES)
    type = models.CharField(max_length=20, choices=ORDER_TYPES)
    status = models.CharField(max_length=20, choices=STATUS_TYPES)
    pc_type = models.CharField(max_length=20, choices=PC_TYPES, blank=True, null=True)
    graphic_card = models.CharField(max_length=20, choices=GRAPHIC_CARD_TYPES, blank=True, null=True)
    processor = models.CharField(max_length=20, choices=PROCESSOR_TYPES, blank=True, null=True)
    cooling = models.CharField(max_length=20, choices=COOLING_TYPES, blank=True, null=True)
    os = models.CharField(max_length=20, choices=OS_TYPES, blank=True, null=True)
    setup = models.BooleanField(default=False)
    tasks = models.ManyToManyField('WorkTask', blank=True)
    presets = models.ManyToManyField('ProgramPreset', blank=True)
    peripheries = models.ManyToManyField('Periphery', blank=True)

    def __str__(self):
        return f'{self.id}. {self.customer}'


class WorkTask(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=100)
    )
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.id}. {self.name}'


class ProgramPreset(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=100)
    )
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.id}. {self.name}'


class Periphery(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=100)
    )
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.id}. {self.name}'


class Price(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.id}. {self.name}'


class AdditionalInfo(TranslatableModel):
    translations = TranslatedFields(
        text=models.CharField(max_length=200),
    )
    name = models.CharField(max_length=50, unique=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.id}. {self.text}'


class Review(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.PositiveSmallIntegerField(default=5)
    order = models.OneToOneField(Order, on_delete=models.SET_NULL,
                                 blank=True, null=True, related_name='review')
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id}. {self.text}'


class Gallery(TranslatableModel):
    translations = TranslatedFields(
        text=models.TextField(),
    )

    def __str__(self):
        return f'{self.id}. {self.text}'


class GalleryItem(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=100),
    )
    gallery = models.ForeignKey('Gallery', on_delete=models.CASCADE, related_name='items')
    file = models.FileField(upload_to='gallery')

    def __str__(self):
        return f'{self.id}. {self.gallery.title}'
