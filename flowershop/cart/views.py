from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
from product.models import Flower


class CartList(APIView):
    def get(self, request):
        if request.session.get('cart'):
            id_list = [data_dict.get('pk') for data_dict in request.session['cart'].values()]
        else:
            return Response('no item in the cart', status=200)

        cart = request.session.get('cart')
        flowers = Flower.objects.filter(pk__in = id_list)
        for flower in flowers:
            cart[flower.pk]['total_product_price'] = flower[flower.pk]['quantity'] * flower.price
            cart[flower.pk]['flower'] = flower

        total_price = sum([cart_item['total_product_price'] for cart_item in cart.values()])
        print(cart)
        context = {
            'products': flowers,
            'cart': cart,
            'total_price': total_price
        }
        return Response(context, status=200)

    def post(self, request, pk):
        if not request.session.get('cart'):
            request.session['cart'] = dict()
        else:
            request.session['cart'] = dict(request.session['cart'])
        exist = request.session['cart'].get(str(pk))
        add_data = {
            'pk': pk,
            'quantity': int(request.POST['quantity'])
        }
        if not exist:
            request.session['cart'][str(pk)] = add_data  # {pk:{}, pk:{}, pk:{}}
        else:
            item_pk = exist['pk']
            request.session['cart'][str(item_pk)]['quantity'] = request.session['cart'][str(item_pk)]['quantity'] + int(
                request.POST.get('quantity'))
        request.session.modified = True
        return Response(add_data, status= status.HTTP_201_CREATED)



