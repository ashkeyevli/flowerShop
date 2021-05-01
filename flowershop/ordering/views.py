# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from _auth.models import Customer
from ordering.models import Order, OrderItem
from ordering.serializer import OrderSerializer, OrderItemSerializer
from product.models import Flower


@api_view(['POST'])
def order_view(request):
    # del request.session['cart']
    # return Response("ok", status=201)
    order = OrderSerializer()
    customer = Customer.objects.get(username=request.user)
    cart = request.session.get('cart')
    total_price = request.session['total_price']
    context = {
        "total_price": total_price,
        "customer": customer
    }
    order = Order.objects.create(customer = customer, total_price=total_price,
                         comment=request.data["comment"])

    # order = OrderSerializer(data = request.data, context = context )

    products = Flower.objects.filter(pk__in=cart.keys())
    for product in products:
        cart[str(product.id)]['flower'] = product

    for item in cart.values():
        # flower = Flower.objects.create(flower = item['flower'])
        order_item = OrderItem.objects.create(order=order,
                                 flower=item['flower'],
                                 quantity=item['quantity']
                                 )

    result = OrderItem.objects.filter(order=order.id)
    # print(result.values())
    serializer = OrderSerializer(order)


    # del request.session['cart']
    #
    #
    # serializer = FlowerNewSerializer(data=request.data, context = context)
    # if order.is_valid():
    #     order.save()
    #     return Response(order.data, status=201)
    return Response(serializer.data, status=201)
