# serializers.py created inside your app folder
from rest_framework import serializers
from .models import *

class BookSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Book
		fields = ['id','title','year','author','price','synopsis','category']

from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
