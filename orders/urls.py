from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = "orders"
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("register", views.register_view, name="register"),
    path("logout", views.logout_view, name="logout"),
    path("item/<item_name>/", views.menu_select, name="item"),
    path("item/<pizza_type>/<pizza_top_type>/", views.pizza_size, name="pizza_size"),
    path("item/<pizza_type>/<pizza_top_type>/order", views.pizza_order, name="pizza_order"),
    path("item/<item_name>/<sub_name>/extra", views.sub_extra, name="sub_extra"),
    path("item/<item_name>/<item_type>/ps", views.pasta_salad, name="pasta_salad"),
    path("item/<item_name>/<item_type>/dinner_platter", views.dinner_platter, name="dinner_platter"),
    path("shopping_cart", views.shopping_cart, name="shopping_cart"),
    path("clear_shopping_cart", views.clear_shopping_cart, name="clear_shopping_cart"),
    path("shopping_cart/check_out", views.check_out, name="check_out"),
    path("order_history", views.order_history, name="order_history"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
