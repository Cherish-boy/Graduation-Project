from django.db import models


class Ceshi(models.Model):
    name = models.CharField(max_length=255)
    id = models.IntegerField(primary_key=True)
    text = models.CharField(max_length=255)


class Building(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    legal_person = models.TextField()
    Contacts = models.TextField()
    Phone = models.BigIntegerField()
    email = models.CharField(max_length=255)
    industry = models.TextField()
    address = models.TextField()
    scope = models.TextField()
    label = models.TextField()
    regis_time = models.TextField()
    regis_capital = models.BigIntegerField()
    credit_code = models.BigIntegerField()
    tax_iden_number = models.CharField(max_length=255)
    kind = models.TextField()
    size = models.TextField()


class Jincheng(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField()
    abbreviation = models.TextField()
    author = models.TextField()
    department = models.TextField()
    release_source = models.TextField()
    prefecture_city = models.TextField()
    kind = models.TextField()
    abstract = models.TextField()
    details = models.TextField()
    declares = models.TextField()
    declare_start_time = models.TextField()
    declare_end_time = models.TextField()
    reward_description = models.TextField()
    release_time = models.TextField()
    key_words = models.TextField()
    label = models.TextField()
    subsidy_amount = models.IntegerField()
