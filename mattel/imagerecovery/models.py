from django.db import models


class ImageSourceLinks(models.Model):
    product_name = models.CharField(max_length=400, blank=True, null=True)
    imagelinks = models.TextField(blank=True)

    class Meta:

        verbose_name = 'ImageSourceLinks'
        verbose_name_plural = 'ImageSourceLinks'

    def __str__(self):
        return self.product_name


class Lego(models.Model):
    product_name = models.CharField(max_length=20000, blank=True, null=True)
    product_price = models.CharField(max_length=20000, blank=True, null=True)
    product_age = models.CharField(max_length=20000, blank=True, null=True)
    product_pieces = models.CharField(max_length=20000, blank=True, null=True)
    items_number = models.CharField(max_length=20000, blank=True, null=True)
    image_list = models.TextField(max_length=20000, blank=True, null=True)
    Vip_points = models.TextField(max_length=20000, blank=True, null=True)
    product_description = models.TextField(
        max_length=20000, blank=True, null=True)

    class Meta:

        verbose_name = 'Lego'
        verbose_name_plural = 'Legos'

    def __str__(self):
        return self.product_name


class LogoToys(models.Model):
    product_name = models.CharField(max_length=20000, blank=True, null=True)
    product_price = models.CharField(max_length=20000, blank=True, null=True)
    product_age = models.CharField(max_length=20000, blank=True, null=True)
    product_pieces = models.CharField(max_length=20000, blank=True, null=True)
    items_number = models.CharField(max_length=20000, blank=True, null=True)
    image_list = models.TextField(max_length=20000, blank=True, null=True)
    Vip_points = models.TextField(max_length=20000, blank=True, null=True)
    product_description = models.TextField(
        max_length=20000, blank=True, null=True)
    product_features = models.TextField(
        max_length=20000, blank=True, null=True)

    class Meta:

        verbose_name = 'LogoToys'
        verbose_name_plural = 'LogoToys'

    def __str__(self):
        return self.product_name


class HasbroToys(models.Model):
    item_id = models.CharField(
        max_length=20000, blank=True, null=True)
    product_name = models.CharField(max_length=20000, blank=True, null=True)
    whats_in_box = models.CharField(max_length=20000, blank=True, null=True)
    category_url = models.CharField(max_length=20000, blank=True, null=True)
    product_description = models.CharField(
        max_length=20000, blank=True, null=True)
    image_list = models.TextField(max_length=20000, blank=True, null=True)

    class Meta:

        verbose_name = 'HasbroToys'
        verbose_name_plural = 'HasbroToys'

    def __str__(self):
        return self.product_name


class ThemeCategories(models.Model):
    category_url = models.TextField(
        max_length=20000, blank=True, null=True, unique=True)
    crawled = models.BooleanField(default=False)

    def __str__(self):
        return str(self.category_url)


class AgeCategories(models.Model):
    category_url = models.TextField(
        max_length=20000, blank=True, null=True, unique=True)
    crawled = models.BooleanField(default=False)

    def __str__(self):
        return str(self.category_url)


class AllProductLinks(models.Model):
    category_url = models.TextField(
        max_length=20000, blank=True, null=True, unique=True)
    crawled = models.BooleanField(default=False)

    def __str__(self):
        return str(self.category_url)


class Tire(models.Model):
    tire_name = models.CharField(max_length=2000)
    tire_price = models.IntegerField()
    tiredescription = models.CharField(
        max_length=2000, default=True, null=True)
    tirebrand = models.CharField(max_length=1200, blank=True, null=True)
    tiresku = models.CharField(max_length=1200, blank=True, null=True)

    class Meta:
        verbose_name = 'Tire'
        verbose_name_plural = 'Tires'

    def __str__(self):

        return self.tire_name
