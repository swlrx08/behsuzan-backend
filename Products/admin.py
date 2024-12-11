from django.contrib import admin
from .models import Product, Specification


# تعریف inline برای مشخصات محصول
class SpecificationInline(admin.TabularInline):  # یا admin.StackedInline برای نمای متفاوت
    model = Specification
    extra = 10  # تعداد ردیف‌های اضافی برای اضافه کردن مشخصات جدید
    fields = ('key', 'value')  # فیلدهایی که در فرم نمایش داده می‌شوند
    verbose_name = "مشخصه"
    verbose_name_plural = "مشخصات"


# تعریف تنظیمات پنل مدیریت محصول
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at')
    list_filter = ('category',)
    search_fields = ('title','id')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    inlines = [SpecificationInline]  # اضافه کردن مشخصات به صفحه محصول
