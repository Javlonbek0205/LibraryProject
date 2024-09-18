from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Book

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'title', 'subtitle', 'content', 'author', 'isbn', 'price',)


    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)
        # kitobning sarlavhasi faqat harflardan iborat bo'lishi uchun validatysiya
        if not title.replace(" ", "").isalpha():
            raise  ValidationError(
                {
                    "status": False,
                    "massage": "Kitobning sarlavhasi harflardan iborat bo'lishi kerak"
                }
            )

        #kitob sarlavhasi va authori bir xil bo'lgan malumotni bazaga qoshmasligi uchun
        elif Book.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                {
                    "status": False,
                    "massage": "sarlavhasi va authori bir xil malumotni kirita olmaysiz"
                }
            )
        return data

    def validate_price(self, price):
        if price < 0 or price > 9999999999999999:
            raise ValidationError(
                {
                    "status": False,
                    "massage": "narx noto'g'ri kiritildi"
                }
            )

        return price
