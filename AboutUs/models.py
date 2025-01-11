from django.db import models
from django.utils.safestring import mark_safe


class AboutUs(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان")
    image = models.ImageField(upload_to="uploads/AboutUs", verbose_name="عکس درباره ما")
    description = models.TextField()

    def about_image(self):
        return mark_safe("< img src='%s' width='50' height='50' />" % self.image)

    class Meta:
        verbose_name = "درباره ما"

    def __str__(self):
        return self.title
