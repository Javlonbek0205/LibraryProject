from decimal import Decimal
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator, MinValueValidator, MaxValueValidator
from django.db import models
from .validators import validate_file_type
from django_resized import ResizedImageField
# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Category(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name

class Books(BaseModel):
    class Availability(models.TextChoices):
        in_stock = 'In stock', 'In stock'
        out_of_stock = 'Out of stock', 'Out of stock'
        on_sale = 'On sale', 'On sale'
        new = 'New', 'New'
    class Format(models.TextChoices):
        standard = 'Standard', 'Standard'
        downloadable = 'Downloadable', 'Downloadable'
        external = 'External', 'External'

    title = models.CharField(max_length=250)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ManyToManyField(Category, related_name='categories', blank=True)
    availability = models.CharField(max_length=250,choices=Availability.choices)
    format = models.CharField(max_length=250, choices=Format.choices)
    book_image = ResizedImageField(size=[219, 317], crop=['middle', 'center'], upload_to='images/',
                                   validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'bmp', 'webp'])], null=True, blank=True)
    book_pdf = models.FileField(upload_to='books_pdf/',
                                validators=[validate_file_type], null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')
    average_rating = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    language = models.CharField(max_length=250, null=True, blank=True)
    pages = models.PositiveIntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    publisher = models.CharField(max_length=250, null=True, blank=True)
    isbn = models.CharField(max_length=250)
    quantity = models.PositiveIntegerField()
    def update_average_rating(self):
        reviews = self.reviews.all()
        if reviews.exists():
            total_rating = sum(review.rating for review in reviews if review.rating is not None)
            self.average_rating = round(Decimal(total_rating) / Decimal(reviews.count()), 1)
        else:
            self.average_rating = 0
        self.save()

    def __str__(self):
        return self.title


class Reviews(BaseModel):
    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    text = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=True, blank=True)
    def __str__(self):
        return f"{self.user}-{self.book}"


class OrderItem(BaseModel):
    class OrderStatus(models.TextChoices):
        new = 'New', 'New'
        sent = 'Sent', 'Sent'
        canceled = 'Canceled', 'Canceled'

    book = models.OneToOneField(Books, on_delete=models.CASCADE, related_name='book_orders')
    order_status = models.CharField(max_length=250, choices=OrderStatus.choices, default=OrderStatus.new)
    quantity = models.PositiveIntegerField(default=1)


    def __str__(self):
        return f"{self.quantity}-{self.book}"

class Cart(BaseModel):
    class CartStatus(models.TextChoices):
        saved = 'Saved', 'Saved'
        sent = 'Sent', 'Sent'
        canceled = 'Canceled', 'Canceled'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')
    orders = models.ManyToManyField(OrderItem, related_name='carts', blank=True)
    cart_status = models.CharField(max_length=250, choices=CartStatus.choices, default=CartStatus.saved)
    def __str__(self):
        return f"Cart_id:{self.id} - {self.user.username}"

