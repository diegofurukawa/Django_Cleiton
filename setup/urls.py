"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from furukawa.views import (
    # === Customer
    CustomerListView,
    CustomerCreateView,
    CustomerUpdateView,
    CustomerDeleteView,
    # === Contact
    ContactListView,
    ContactCreateView,
    ContactUpdateView,
    ContactDeleteView,
    # === Product
    ProductListView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    # === Tax
    TaxListView,
    TaxCreateView,
    TaxUpdateView,
    TaxDeleteView,
    # === SalesMan
    SalesManListView,
    SalesManCreateView,
    SalesManUpdateView,
    SalesManDeleteView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", CustomerListView.as_view(), name="customer_list"),
    # === Customer
    path("customer", CustomerListView.as_view(), name="customer_list"),
    path("customer/create", CustomerCreateView.as_view(), name="customer_create"),
    path(
        "customer/update/<int:pk>", CustomerUpdateView.as_view(), name="customer_update"
    ),
    path(
        "customer/delete/<int:pk>", CustomerDeleteView.as_view(), name="customer_delete"
    ),
    # === Contact
    path("contact", ContactListView.as_view(), name="contact_list"),
    path("contact/create", ContactCreateView.as_view(), name="contact_create"),
    path("contact/update/<int:pk>", ContactUpdateView.as_view(), name="contact_update"),
    path("contact/delete/<int:pk>", ContactDeleteView.as_view(), name="contact_delete"),
    # === Product
    path("product", ProductListView.as_view(), name="product_list"),
    path("product/create", ProductCreateView.as_view(), name="product_create"),
    path("product/update/<int:pk>", ProductUpdateView.as_view(), name="product_update"),
    path("product/delete/<int:pk>", ProductDeleteView.as_view(), name="product_delete"),
    # === Tax
    path("tax", TaxListView.as_view(), name="tax_list"),
    path("tax/create", TaxCreateView.as_view(), name="tax_create"),
    path("tax/update/<int:pk>", TaxUpdateView.as_view(), name="tax_update"),
    path("tax/delete/<int:pk>", TaxDeleteView.as_view(), name="tax_delete"),
    # === SalesMan
    path("salesman", SalesManListView.as_view(), name="salesman_list"),
    path("salesman/create", SalesManCreateView.as_view(), name="salesman_create"),
    path(
        "salesman/update/<int:pk>", SalesManUpdateView.as_view(), name="salesman_update"
    ),
    path(
        "salesman/delete/<int:pk>", SalesManDeleteView.as_view(), name="salesman_delete"
    ),
]
