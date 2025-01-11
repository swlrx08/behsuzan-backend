from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان خبر")
    short_description = models.CharField(max_length=200, verbose_name="توضیحات کوتاه")
    content = models.TextField(verbose_name="متن خبر")
    image = models.ImageField(upload_to='news_images/', null=True, blank=True, verbose_name="تصویر خبر")
    published_date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ انتشار")
    is_active = models.BooleanField(default=True, verbose_name="فعال بودن")

    class Meta:
        verbose_name = "خبر"
        verbose_name_plural = "اخبار"
        ordering = ['-published_date']

    def __str__(self):
        return self.title
