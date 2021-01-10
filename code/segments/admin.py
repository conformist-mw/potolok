from django.contrib import admin

from .models import Color, ColorType, OrderNumber, Segment


@admin.register(Segment)
class SegmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    pass


@admin.register(ColorType)
class ColorTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderNumber)
class OrderNumberAdmin(admin.ModelAdmin):
    pass
