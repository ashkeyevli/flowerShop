from rest_framework import serializers

from product.models import Category, Flower


class CateogriesSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField()
    class Meta:
        model = Category
        fields = ('name', 'image')


class FlowerNewSerializer(serializers.Serializer):
    category_id = serializers.IntegerField()
    title = serializers.CharField()
    # slug = serializers.SlugField()
    image = serializers.ImageField()
    description = serializers.CharField(style={'base_template': 'textarea.html'})
    price = serializers.DecimalField(max_digits=9, decimal_places=2)
    color = serializers.CharField()
    stock = serializers.IntegerField()
    available = serializers.BooleanField()

    def create(self, validated_data):
        flower = Flower.objects.create( **validated_data)
        return flower
    def update(self, instance, validated_data):
        instance.category = validated_data.get('category', instance.category)
        instance.title = validated_data.get('title', instance.title)
        # instance.slug = validated_data.get('slug', instance.slug)
        instance.image = validated_data.get('image', instance.image)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.color = validated_data.get('color', instance.color)
        instance.stock = validated_data.get('stock', instance.stock)
        instance.available = validated_data.get('available', instance.available)
        instance.save()
        return instance



class FlowerSerializer(serializers.ModelSerializer):
    # id = serializers.ImageField()
    class Meta:
        model = Flower
        fields = '__all__'


