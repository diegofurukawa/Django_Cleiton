from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Customer, Contact, Product, Tax, SalesMan
from django.urls import reverse_lazy


# ========== Customer


class CustomerListView(ListView):
    model = Customer


class CustomerCreateView(CreateView):
    model = Customer
    fields = [
        "cCustomerName",
        "cCustomerShortName",
        "xCustomerDocument",
        "cPhone",
        "cEmail",
        "idSalesMan",
        "xCustomerType",
        "xCustomerClass",
        "xCustomerStatus",
        "xPaymentCondition",
        "xListPrice",
        "cObservation",
    ]
    success_url = reverse_lazy("customer_list")


class CustomerUpdateView(UpdateView):
    model = Customer
    fields = [
        "cCustomerName",
        "cCustomerShortName",
        "xCustomerDocument",
        "cPhone",
        "cEmail",
        "idSalesMan",
        "xCustomerType",
        "xCustomerClass",
        "xCustomerStatus",
        "xPaymentCondition",
        "xListPrice",
        "cObservation",
    ]
    success_url = reverse_lazy("customer_list")


class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = reverse_lazy("customer_list")


# ========== Contact
class ContactListView(ListView):
    model = Contact


class ContactCreateView(CreateView):
    model = Contact
    fields = [
        "idCustomer",
        "cName",
        "cPhone",
        "cEmail",
    ]
    success_url = reverse_lazy("contact_list")


class ContactUpdateView(UpdateView):
    model = Contact
    fields = [
        "idCustomer",
        "cName",
        "cPhone",
        "cEmail",
    ]
    success_url = reverse_lazy("contact_list")


class ContactDeleteView(DeleteView):
    model = Contact
    success_url = reverse_lazy("contact_list")


# ========== Product


class ProductListView(ListView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = [
        "cProductName",
        "cDescription",
        "xType",
        "xU",
        "xAreaCapacity",
        "xCapacity",
        "xDensity",
        "nValue",
    ]
    success_url = reverse_lazy("product_list")


class ProductUpdateView(UpdateView):
    model = Product
    fields = [
        "cProductName",
        "cDescription",
        "xType",
        "xU",
        "xAreaCapacity",
        "xCapacity",
        "xDensity",
        "nValue",
    ]
    success_url = reverse_lazy("product_list")


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("product_list")


# ========== Tax


class TaxListView(ListView):
    model = Tax


class TaxCreateView(CreateView):
    model = Tax
    fields = [
        "cTaxDescription",
        "cAcronym",
        "xType",
        "nValue",
        "nValueCalculated",
    ]
    success_url = reverse_lazy("tax_list")


class TaxUpdateView(UpdateView):
    model = Tax
    fields = [
        "cTaxDescription",
        "cAcronym",
        "xType",
        "nValue",
        "nValueCalculated",
    ]
    success_url = reverse_lazy("tax_list")


class TaxDeleteView(DeleteView):
    model = Tax
    success_url = reverse_lazy("tax_list")


# ========== SalesMan


class SalesManListView(ListView):
    model = SalesMan


class SalesManCreateView(CreateView):
    model = SalesMan
    fields = [
        "cName",
        "cPhone",
        "cEmail",
    ]
    success_url = reverse_lazy("salesman_list")


class SalesManUpdateView(UpdateView):
    model = SalesMan
    fields = [
        "cName",
        "cPhone",
        "cEmail",
    ]
    success_url = reverse_lazy("salesman_list")


class SalesManDeleteView(DeleteView):
    model = SalesMan
    success_url = reverse_lazy("salesman_list")
