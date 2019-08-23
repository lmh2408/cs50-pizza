from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from decimal import *

from .models import *

# Create your views here.
def index(request):
    return render(request, "orders/index.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(reverse("orders:index"))
        else:
            return HttpResponse("Invalid credentials")
    else:
        return render(request, "orders/login.html")


def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            user = User.objects.create_user(username=username, password=password)
        except:
            return HttpResponse("Error when registering")
        login(request, user)
        return redirect(reverse("orders:index"))
    else:
        return render(request, "orders/register.html")


def logout_view(request):
    logout(request)
    return redirect(reverse("orders:index"))


def menu_select(request, item_name):
    if item_name == 'Regular Pizza' or item_name == 'Sicilian Pizza':
        item = Pizza_type.objects.get(pizza_type=item_name)
        pizza = Pizza.objects.filter(pizza_type=item)
        context = {
            "menu_type": "pizza",
            "title": item.pizza_type,
            "list": pizza
        }
        return render(request, 'orders/item.html', context)

    elif item_name == 'Subs':
        item = Sub.objects.all()
        context = {
            "menu_type": "sub",
            "title": item_name,
            "list": item
        }
        return render(request, 'orders/item.html', context)

    elif item_name == 'Salads' or item_name == 'Pasta':
        if item_name == 'Salads':
            item = Salad.objects.all()
            link = "Salads"
        elif item_name == 'Pasta':
            item = Pasta.objects.all()
            link = "Pasta"

        context = {
            "menu_type": "salad",
            "title": item_name,
            "list": item,
            "link": link,
        }
        return render(request, 'orders/item.html', context)

    elif item_name == 'Dinner Platters':
        item = Dinner_platter.objects.all()
        context = {
            "menu_type": "dinner_platters",
            "title": item_name,
            "list": item
        }
        return render(request, 'orders/item.html', context)

    else:
        return HttpResponse("No such item")


def pizza_size(request, pizza_type, pizza_top_type):
    pizza_type = Pizza_type.objects.get(pizza_type=pizza_type)
    pizza_topping = Pizza_topping_number.objects.get(pizza_topping_number=pizza_top_type)
    pizza = Pizza.objects.filter(pizza_type=pizza_type).get(pizza_topping_number=pizza_topping)

    topping_list = Pizza_topping.objects.all()

    context = {
        "pizza": pizza,
        "topping_list": topping_list
    }

    return render(request, 'orders/pizza_size.html', context)


def pizza_order(request, pizza_type, pizza_top_type):
    # get input
    size = request.POST["size"]
    topping = request.POST.getlist("topping[]")
    quantity = request.POST["quantity"]
    # check input
    try:
        quantity = int(quantity)
        if quantity == 0:
            return HttpResponse("Invalid quantity")
    except:
        return HttpResponse("Invalid number input")
    try:
        pizza_type = Pizza_type.objects.get(pizza_type=pizza_type)
    except:
        return HttpResponse("Invalid type")
    try:
        pizza_topping = Pizza_topping_number.objects.get(pizza_topping_number=pizza_top_type)
    except:
        return HttpResponse("Invalid type")

    pizza = Pizza.objects.filter(pizza_type=pizza_type).get(pizza_topping_number=pizza_topping)

    if len(topping) != pizza.pizza_topping_number.topping_number:
        return HttpResponse("Invalid topping number")

    stock_topping_list = []

    for stock_topping in Pizza_topping.objects.all().values():
        stock_topping_list.append(stock_topping["pizza_topping"])

    for item in topping:
        if item not in stock_topping_list:
            return HttpResponse("Invalid topping")

    price = 0
    if size == "sml":
        price = pizza.small_price
    elif size == "lrg":
        price = pizza.large_price
    else:
        return HttpResponse("Invalid size")

    shopping_cart = Shopping_cart(user=request.user, item=f"{pizza_type} ({pizza_topping})", note=", ".join(topping), price=price, quantity=quantity)
    shopping_cart.save()

    return redirect(reverse("orders:shopping_cart"))


def sub_extra(request, item_name, sub_name):
    if request.method == "POST":
        # get input
        extra = request.POST.getlist("extra[]")
        size = request.POST["size"]
        try:
            quantity = int(request.POST["quantity"])
            if quantity == 0:
                return HttpResponse("Invalid quantity")
        except:
            return HttpResponse("Invalid quantity")

        price = 0
        cart_name = ""
        # check input
        try:
            sub = Sub.objects.get(sub=sub_name)
        except:
            return HttpResponse("Wut???? >.<")

        if size == "sml":
            price = price + sub.small_price
            cart_name = f"Sub: {sub.sub} (S)"
        elif size == "lrg":
            price = price + sub.large_price
            cart_name = f"Sub: {sub.sub} (L)"
        else:
            return HttpResponse("Wut???? >.<")

        extra_list = []
        for item in extra:
            extra_name = Sub_extra.objects.get(sub_extra=item)
            extra_list.append(extra_name.sub_extra)
            if size == "sml":
                price = price + extra_name.small_price
            elif size == "lrg":
                price = price + extra_name.large_price

        shopping_cart = Shopping_cart(user=request.user, item=cart_name, note=", ".join(extra_list), price=price, quantity=quantity)
        shopping_cart.save()

        return redirect(reverse("orders:shopping_cart"))

    else: # method = "GET"
        try:
            sub = Sub.objects.get(sub=sub_name)
        except:
            return HttpResponse("sub doesn't exist")

        sub_extra = Sub_extra.objects.all()
        context = {
            "sub": sub,
            "extra": sub_extra,
        }
        return render(request, 'orders/sub_extra.html', context)


def pasta_salad(request, item_name, item_type):
    if request.method == "POST":
        try:
            quantity = int(request.POST["quantity"])
            if quantity == 0:
                return HttpResponse("Invalid quantity")
        except:
            return HttpResponse("Invalid quantity")

        if item_name == "Salads":
            try:
                item = Salad.objects.get(item=item_type)
            except:
                return HttpResponse("Item name not exist")
        elif item_name == "Pasta":
            try:
                item = Pasta.objects.get(item=item_type)
            except:
                return HttpResponse("Item name not exist")

        shopping_cart = Shopping_cart(user=request.user, item=item.item, note="", price=item.price, quantity=quantity)
        shopping_cart.save()

        return redirect(reverse("orders:shopping_cart"))

    else:
        if item_name == "Salads":
            try:
                item = Salad.objects.get(item=item_type)
            except:
                return HttpResponse("Item name not exist")
        elif item_name == "Pasta":
            try:
                item = Pasta.objects.get(item=item_type)
            except:
                return HttpResponse("Item name not exist")
        else:
            return HttpResponse("Item name not exist")

        context = {
            "item_name": item_name,
            "item": item,
        }
        return render(request, "orders/pasta_salad.html", context)


def dinner_platter(request, item_name, item_type):
    if request.method == "POST":
        size = request.POST["size"]
        try:
            quantity = int(request.POST["quantity"])
            if quantity == 0:
                return HttpResponse("Invalid quantity")
        except:
            return HttpResponse("Invalid quantity")

        try:
            item = Dinner_platter.objects.get(dinner_platter=item_type)
        except:
            return HttpResponse("Item name not exist")

        if size == "sml":
            price = item.small_price
            cart_name = f"Dinner Platter: {item.dinner_platter} (S)"
        elif size == "lrg":
            price = item.large_price
            cart_name = f"Dinner Platter: {item.dinner_platter} (L)"
        else:
            return HttpResponse("Wut???? >.<")

        shopping_cart = Shopping_cart(user=request.user, item=cart_name, note="", price=price, quantity=quantity)
        shopping_cart.save()
        return redirect(reverse("orders:shopping_cart"))

    else:
        try:
            item = Dinner_platter.objects.get(dinner_platter=item_type)
        except:
            return HttpResponse("Item name not exist")

        context = {
            "item": item,
            "item_name": "Dinner Platters",
        }
        return render(request, "orders/dinner_platter.html", context)

def shopping_cart(request):
    try:
        shopping_cart = Shopping_cart.objects.filter(user=request.user)
    except:
        context = {
            "empty": True,
        }
        return render(request, "orders/shopping_cart.html", context)
    total = 0

    for item in shopping_cart:
        total = total + item.price * item.quantity

    context = {
        "empty": False,
        "shopping_cart": shopping_cart,
        "total": total,
    }

    return render(request, "orders/shopping_cart.html", context)


def clear_shopping_cart(request):
    Shopping_cart.objects.filter(user=request.user).delete()
    return redirect(reverse("orders:shopping_cart"))


def check_out(request):
    try:
        shopping_cart = Shopping_cart.objects.filter(user=request.user)
    except:
        return HttpResponse("Empty cart!")

    for item in shopping_cart:
        transaction = Transaction(user=item.user, item=item.item, note=item.note, price=item.price, quantity=item.quantity)
        transaction.save()

    shopping_cart.delete()

    return redirect(reverse("orders:order_history"))


def order_history(request):
    try:
        transaction = Transaction.objects.filter(user=request.user).order_by("-date")
    except:
        return HttpResponse("Empty history!")

    data = []

    for order in transaction:
        order_dict = {
            "order": order,
            "total": order.total()
        }
        data.append(order_dict)

    context = {
        "data": data
    }
    return render(request, "orders/order_history.html", context)
