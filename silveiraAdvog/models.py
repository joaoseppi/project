from django.db import models
# from django.contrib.auth.models import User


class states(models.Model):
    states = models.CharField(max_length=32)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return self.uf


class city(models.Model):
    city = models.CharField(max_length=64)
    id_states = models.ForeignKey(
        states, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.city


class address(models.Model):
    street = models.CharField(max_length=64)
    num = models.IntegerField()
    cep = models.CharField(max_length=8)
    update_time = models.DateTimeField(auto_now=True)
    id_city = models.ForeignKey(
        city, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.num


class user_tbl(models.Model):
    register_date = models.DateTimeField(auto_now=True)
    email = models.CharField(max_length=64)
    phone = models.CharField(max_length=12)
    username = models.CharField(max_length=32)
    user_pwd = models.CharField(max_length=64)
    id_address = models.ForeignKey(
        address, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.email


class physical_person(models.Model):
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=10)
    date_birth = models.DateField()
    given_name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    id_user_tbl = models.ForeignKey(
        user_tbl, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.rg


class employee_position(models.Model):
    employee_position = models.CharField(max_length=32)


class employee(models.Model):
    date_contract = models.DateField()
    pis = models.CharField(max_length=16)
    id_physical_person = models.ForeignKey(
        physical_person, on_delete=models.SET_NULL, null=True)
    id_position = models.ForeignKey(
        employee_position, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.pis


class lawyer(models.Model):
    cod_oab = models.CharField(max_length=32)
    id_employee = models.ForeignKey(
        employee, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.cod_oab


class client(models.Model):
    cnpj = models.CharField(max_length=16)
    fantasy_name = models.CharField(max_length=64)
    social_reason = models.CharField(max_length=64)
    id_user_tbl = models.ForeignKey(
        user_tbl, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.id_user_tbl


class consultation(models.Model):
    schedule = models.DateField()
    register_time = models.DateTimeField(auto_now=True)
    id_employee = models.ForeignKey(
        employee, on_delete=models.SET_NULL, null=True)
    id_lawyer = models.ForeignKey(
        lawyer, on_delete=models.SET_NULL, null=True)
    id_client = models.ForeignKey(
        client, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.register_time


class connect_reg(models.Model):
    page = models.CharField(max_length=32)
    ip = models.CharField(max_length=12)
    connect_time = models.DateTimeField(auto_now=True)
    id_user_tbl = models.ForeignKey(
        user_tbl, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.ip


class legal_process(models.Model):
    cod_process = models.CharField(max_length=64)
    process_type = models.CharField(max_length=32)
    register_time = models.DateTimeField(auto_now=True)
    id_lawyer = models.ForeignKey(
        lawyer, on_delete=models.SET_NULL, null=True)
    id_client = models.ForeignKey(
        client, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.cod_process


class document(models.Model):
    locale = models.CharField(max_length=128)
    update_time = models.TimeField(auto_now=True)
    id_legal_process = models.ForeignKey(
        legal_process, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.id_legal_process


class status(models.Model):
    update_time = models.DateTimeField(auto_now=True)
    id_legal_process = models.ForeignKey(
        legal_process, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.id_legal_process
