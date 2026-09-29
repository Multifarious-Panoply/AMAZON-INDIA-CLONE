from decimal import Decimal

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from .models import Order, OrderItem, Product


def home(request):
    products = Product.objects.all()
    deals = products.filter(is_deal=True)[:8]
    categories = Product.CATEGORY_CHOICES

    return render(request, "store/home.html", {
        "products": products[:8],
        "deals": deals,
        "categories": categories,
    })


def product_list(request):
    products = Product.objects.all()

    query = request.GET.get("q", "").strip()
    category = request.GET.get("category", "").strip()
    sort = request.GET.get("sort", "").strip()

    if query:
        products = products.filter(name__icontains=query)

    if category:
        products = products.filter(category=category)

    if sort == "price_low":
        products = products.order_by("price")
    elif sort == "price_high":
        products = products.order_by("-price")
    elif sort == "rating":
        products = products.order_by("-rating")
    else:
        products = products.order_by("-created_at")

    return render(request, "store/products.html", {
        "products": products,
        "query": query,
        "selected_category": category,
        "selected_sort": sort,
        "categories": Product.CATEGORY_CHOICES,
    })


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    return render(request, "store/product_detail.html", {
        "product": product,
    })


def cart_view(request):
    cart = request.session.get("cart", {})
    products = Product.objects.filter(id__in=cart.keys())

    items = []
    total = Decimal("0")

    for product in products:
        quantity = int(cart.get(str(product.id), 0))
        subtotal = product.price * quantity
        total += subtotal

        items.append({
            "product": product,
            "quantity": quantity,
            "subtotal": subtotal,
        })

    return render(request, "store/cart.html", {
        "items": items,
        "total": total,
    })


def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)

    cart = request.session.get("cart", {})
    product_id = str(product.id)

    cart[product_id] = int(cart.get(product_id, 0)) + 1

    request.session["cart"] = cart
    request.session.modified = True

    messages.success(request, f"{product.name} added to cart.")
    return redirect(request.META.get("HTTP_REFERER", "cart"))


def remove_from_cart(request, pk):
    cart = request.session.get("cart", {})
    product_id = str(pk)

    if product_id in cart:
        del cart[product_id]

    request.session["cart"] = cart
    request.session.modified = True

    return redirect("cart")


def update_cart(request, pk):
    if request.method == "POST":
        cart = request.session.get("cart", {})
        product_id = str(pk)

        try:
            quantity = int(request.POST.get("quantity", 1))
        except ValueError:
            quantity = 1

        if quantity > 0:
            cart[product_id] = quantity
        else:
            cart.pop(product_id, None)

        request.session["cart"] = cart
        request.session.modified = True

    return redirect("cart")


def register(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully.")
            return redirect("home")
    else:
        form = UserCreationForm()

    return render(request, "registration/register.html", {
        "form": form,
    })


@login_required
def checkout(request):
    cart = request.session.get("cart", {})

    if not cart:
        messages.warning(request, "Your cart is empty.")
        return redirect("products")

    products = Product.objects.filter(id__in=cart.keys())

    items = []
    total = Decimal("0")

    for product in products:
        quantity = int(cart.get(str(product.id), 0))
        subtotal = product.price * quantity
        total += subtotal

        items.append({
            "product": product,
            "quantity": quantity,
            "subtotal": subtotal,
        })

    if request.method == "POST":
        full_name = request.POST.get("full_name", "").strip()
        address = request.POST.get("address", "").strip()
        city = request.POST.get("city", "").strip()
        state = request.POST.get("state", "").strip()
        pincode = request.POST.get("pincode", "").strip()
        payment_method = request.POST.get("payment_method", "COD")

        if not all([full_name, address, city, state, pincode]):
            messages.error(request, "Please fill all address fields.")
            return redirect("checkout")

        order = Order.objects.create(
            user=request.user,
            full_name=full_name,
            address=address,
            city=city,
            state=state,
            pincode=pincode,
            payment_method=payment_method,
            total=total,
        )

        for item in items:
            OrderItem.objects.create(
                order=order,
                product=item["product"],
                quantity=item["quantity"],
                price=item["product"].price,
            )

        request.session["cart"] = {}
        request.session.modified = True

        return redirect("order_detail", pk=order.pk)

    return render(request, "store/checkout.html", {
        "items": items,
        "total": total,
    })


@login_required
def orders(request):
    user_orders = Order.objects.filter(
        user=request.user
    ).order_by("-created_at")

    return render(request, "store/orders.html", {
        "orders": user_orders,
    })


@login_required
def order_detail(request, pk):
    order = get_object_or_404(
        Order,
        pk=pk,
        user=request.user,
    )

    return render(request, "store/order_detail.html", {
        "order": order,
    })
