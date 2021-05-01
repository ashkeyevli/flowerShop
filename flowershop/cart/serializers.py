from rest_framework import serializers

from product.serializers import FlowerSerializer


class CartSerializer(serializers.Serializer):

    flower = FlowerSerializer()

    total_product_price = serializers.DecimalField(max_digits=9, decimal_places=2)
    quantity = serializers.IntegerField()
