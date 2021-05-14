from rest_framework import serializers

from ordering.models import OrderItem, Order
from product.serializers import FlowerNewSerializer, FlowerSerializer




class OrderItemSerializer(serializers.ModelSerializer):
    # flower = FlowerSerializer()
    # quantity = serializers.IntegerField()

    class Meta:
        model = OrderItem
        fields = '__all__'




    # def create(self, validated_data):
    #     flower = OrderItem.objects.create( **validated_data)
    #     return flower
    # def update(self, instance, validated_data):
    #     instance.order_id = validated_data.get('order', instance.order)
    #     instance.flower_id = validated_data.get('flower', instance.flower)
    #     instance.quantity = validated_data.get('quantity', instance.quantity)
    #
    #     instance.save()
    #     return instance
    #
    # def to_representation(self, instance):
    #     rep = super().to_representation(instance)
    #     rep['items'] = OrderItemSerializer(instance.order.items).data
    #     print(instance.order.items)
    #     return rep



    # flower = FlowerSerializer()
    # items = OrderSerializer(source='order')

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)



    # def create(self, validated_data):
         # print(self.context.get("customer"))
         # order = Order.objects.create(customer=validated_data("customer"), total_price=validated_data("total_price"),
         #                            comment=validated_data('comment'), created_at=validated_data('created_at'),
         #                            order_date=validated_data('order_date'), delivery_type=validated_data('delivery_type'),
         #                              status=validated_data('status')
         #                              )
         # return order
    class Meta:
        model = Order
        fields = ('customer', 'total_price', 'comment', 'created_at', 'order_date', 'delivery_type', 'status', 'items')

    def validate_total_price(self, value):
        if value < 0:
            raise serializers.ValidationError('Вы не заказали ничего')
        return value

class OrderCustomerSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)



    # def create(self, validated_data):
         # print(self.context.get("customer"))
         # order = Order.objects.create(customer=validated_data("customer"), total_price=validated_data("total_price"),
         #                            comment=validated_data('comment'), created_at=validated_data('created_at'),
         #                            order_date=validated_data('order_date'), delivery_type=validated_data('delivery_type'),
         #                              status=validated_data('status')
         #                              )
         # return order
    class Meta:
        model = Order
        fields = ('total_price', 'comment', 'created_at', 'order_date', 'delivery_type', 'status', 'items')

    def validate_total_price(self, value):
        if value < 0:
            raise serializers.ValidationError('Вы не заказали ничего')
        return value

