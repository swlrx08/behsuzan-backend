from django.db import models
from django.utils.safestring import mark_safe


class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name="عنوان")
    short_description = models.CharField(max_length=200, verbose_name="توضیحات کوتاه")
    description = models.TextField(verbose_name="معرفی")
    category = models.CharField(
        max_length=20,
        choices=[('cooler', 'کولر'), ('fireplace', 'شومینه'), ('other', 'سایر')],
        verbose_name="دسته‌بندی"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

    def __str__(self):
        return self.title


class Specification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="specifications", verbose_name="محصول")
    key = models.CharField(max_length=50, verbose_name="ویژگی")
    value = models.CharField(max_length=255, verbose_name="مقدار")

    class Meta:
        verbose_name = "مشخصه محصول"
        verbose_name_plural = "مشخصات محصولات"

    def __str__(self):
        return f"{self.key}: {self.value}"


class ProductImages(models.Model):
    images = models.ImageField(upload_to="uploads/products/images/", null=True, blank=True)
    product = models.ForeignKey(Product, related_name="p_images", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def vehicle_image(self):
        return mark_safe("< img src='%s' width='50' height='50' />" % self.images)

    class Meta:
        verbose_name = "Product Image"
        verbose_name_plural = "Products Images"
