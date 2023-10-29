from django.db import models


# ========= Vendedor | SalesMan
class SalesMan(models.Model):
    idSalesMan = models.IntegerField(primary_key=True)
    cName = models.CharField(
        max_length=100, null=False, blank=False, verbose_name="Vendedor"
    )
    cPhone = models.CharField(
        max_length=100, null=False, blank=False, verbose_name="Telefone"
    )
    cEmail = models.EmailField(
        max_length=100, null=False, blank=False, verbose_name="E-mail"
    )
    dCreated = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    dLastUpdate = models.DateTimeField(null=True)
    lActive = models.IntegerField(auto_created=True, default=1)

    def __str__(self):
        return "{} ({})".format(self.idSalesMan, self.cName)


# ========= Cliente | Customer
class Customer(models.Model):
    idCustomer = models.IntegerField(primary_key=True, verbose_name="idCliente")

    xCustomerDocument = models.CharField(max_length=21, verbose_name="CNPJ")

    cCustomerName = models.CharField(
        max_length=100, null=False, blank=False, verbose_name="Razão Social"
    )
    cCustomerShortName = models.CharField(
        max_length=100, null=False, blank=False, verbose_name="Nome Fantasia"
    )
    cPhone = models.CharField(
        max_length=100, null=False, blank=False, verbose_name="Telefone"
    )
    cEmail = models.EmailField(
        max_length=100, null=True, blank=False, verbose_name="E-mail"
    )
    xCustomerType = models.CharField(
        max_length=50, null=False, blank=False, verbose_name="Tipo"
    )
    xCustomerClass = models.CharField(
        max_length=50, null=False, blank=False, verbose_name="Classe"
    )
    xCustomerStatus = models.CharField(
        max_length=50, null=False, blank=False, verbose_name="Status"
    )
    xPaymentCondition = models.CharField(
        max_length=50, null=False, blank=False, verbose_name="Cond. Pag."
    )
    xListPrice = models.CharField(
        max_length=100, null=False, blank=False, verbose_name="Lista Preço"
    )
    cObservation = models.TextField(null=True, blank=True, verbose_name="Observação")
    idSalesMan = models.ForeignKey("SalesMan", on_delete=models.PROTECT)
    dCreated = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    dLastUpdate = models.DateTimeField(auto_now_add=True, null=True)
    lActive = models.IntegerField(auto_created=True, default=1)

    def __str__(self):
        return "{} ({})".format(self.idCustomer, self.cCustomerShortName)


# ========= Contacto | Contact
class Contact(models.Model):
    idContact = models.IntegerField(primary_key=True)

    cName = models.CharField(
        max_length=100, null=False, blank=False, verbose_name="Nome Contato"
    )
    cPhone = models.CharField(
        max_length=100, null=False, blank=False, verbose_name="Telefone"
    )
    cEmail = models.EmailField(
        max_length=100, null=False, blank=False, verbose_name="Email"
    )
    dCreated = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    dLastUpdate = models.DateTimeField(null=True)

    idCustomer = models.ForeignKey(
        "Customer", on_delete=models.PROTECT, verbose_name="Cliente"
    )

    lActive = models.IntegerField(auto_created=True, default=1)

    def __str__(self):
        return "{} ({})".format(self.idContact, self.cName)


# ========= Produto | Product
class Product(models.Model):
    idProduct = models.IntegerField(primary_key=True)
    cProductName = models.CharField(
        max_length=100, null=False, blank=False, verbose_name="Material"
    )
    cDescription = models.CharField(
        max_length=300, null=True, blank=True, verbose_name="Descrição"
    )
    xType = models.CharField(max_length=100, null=True, blank=True, verbose_name="Tipo")
    xU = models.CharField(max_length=100, null=True, blank=True, verbose_name="xU")
    xAreaCapacity = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="g/m2"
    )
    xCapacity = models.FloatField(null=True, blank=True, verbose_name="gm")
    xDensity = models.FloatField(null=True, blank=True, verbose_name="Densidade")
    nValue = models.FloatField(null=True, blank=True, verbose_name="Valor Unit")

    lActive = models.IntegerField(auto_created=True, default=1)

    def __str__(self):
        return "{} ({})".format(self.idProduct, self.cProductName)


# ========= Orçamento | Budget
class Tax(models.Model):
    idTax = models.IntegerField(primary_key=True)
    cTaxDescription = models.CharField(
        max_length=300, null=False, blank=False, verbose_name="Descrição"
    )
    cAcronym = models.CharField(
        max_length=20, null=False, blank=False, verbose_name="Sigla"
    )
    xType = models.CharField(
        max_length=10, null=False, blank=False, verbose_name="Tipo"
    )
    nValue = models.FloatField(null=False, blank=False, verbose_name="Valor")
    nValueCalculated = models.FloatField(
        null=False, blank=False, verbose_name="Valor Imposto"
    )
    lActive = models.IntegerField(auto_created=True, default=1)

    def __str__(self):
        return "{} ({})".format(self.idTax, self.cAcronym)


# ========= Orçamento | Budget
class Budget(models.Model):
    idBudget = models.IntegerField(primary_key=True)
    idProduct = models.ForeignKey("Product", on_delete=models.SET)
    lActive = models.IntegerField(auto_created=True, default=1)


# ========= Contrato | Contract
class Contract(models.Model):
    idContract = models.IntegerField(primary_key=True)
    cVendedor = models.CharField(
        max_length=100, null=False, blank=False, verbose_name="Vendedor"
    )
    cDescription = models.CharField(
        max_length=300, null=True, blank=True, verbose_name="Descrição"
    )
    dContractCreated = models.DateField(
        null=True, blank=False, verbose_name="Contrato desde"
    )
    nContractDuration = models.IntegerField(null=True, verbose_name="Tempo de Contrato")
    dLastUpdate = models.DateTimeField(null=True)
    idCustomer = models.ForeignKey("Customer", on_delete=models.PROTECT)
    idSalesMan = models.ForeignKey("SalesMan", on_delete=models.PROTECT)
    lActive = models.IntegerField(auto_created=True, default=1)


# ========= Endereço | Address
class Address(models.Model):
    idAddress = models.IntegerField(primary_key=True)

    cAddress = models.CharField(
        max_length=100, null=False, blank=False, verbose_name="Endereço"
    )
    idCity = models.IntegerField(null=True)

    cCityName = models.CharField(
        max_length=100, null=False, blank=False, verbose_name="Cidade"
    )
    idState = models.IntegerField(null=True)
    cStateName = models.CharField(
        max_length=100, null=False, blank=False, verbose_name="Estado"
    )
    cZipCode = models.CharField(
        max_length=20, null=False, blank=False, verbose_name="CEP"
    )

    idCustomer = models.ForeignKey(
        "Customer", on_delete=models.PROTECT, verbose_name="Cliente"
    )

    dCreated = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    dLastUpdate = models.DateTimeField(null=True)

    lActive = models.IntegerField(auto_created=True, default=1)

    def __str__(self):
        return "{} ({})".format(self.idAddress, self.cName)
