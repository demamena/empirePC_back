import parler.admin
from django.contrib import admin
from parler.admin import TranslatableAdmin, TranslatableStackedInline
from .models import Customer, Order, WorkTask, ProgramPreset, Periphery, Price, AdditionalInfo, Review, Gallery, \
    GalleryItem


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'middle_name', 'last_name', 'phone', 'bonus', 'birthday')
    search_fields = ('email', 'first_name', 'middle_name', 'last_name', 'phone')
    list_filter = ('bonus', 'birthday')
    fields = ('email', 'first_name', 'middle_name', 'last_name', 'phone', 'bonus', 'birthday')


class OrderInline(admin.TabularInline):
    model = Order
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'phone', 'date', 'price', 'status', 'type', 'delivery_type')
    search_fields = ('customer__email', 'phone', 'status', 'type')
    list_filter = ('status', 'type', 'delivery_type', 'pc_type', 'graphic_card', 'processor', 'cooling', 'os')
    date_hierarchy = 'date'
    filter_horizontal = ('tasks', 'presets', 'peripheries')
    fields = (
        'customer', 'phone', 'date', 'price', 'preferences', 'wishes', 'call_time', 'delivery_type', 'type',
        'status', 'pc_type', 'graphic_card', 'processor', 'cooling', 'os', 'setup', 'tasks', 'presets', 'peripheries'
    )


@admin.register(WorkTask)
class WorkTaskAdmin(TranslatableAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(ProgramPreset)
class ProgramPresetAdmin(TranslatableAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Periphery)
class PeripheryAdmin(TranslatableAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    search_fields = ('name',)


@admin.register(AdditionalInfo)
class AdditionalInfoAdmin(TranslatableAdmin):
    list_display = ('id', 'name', 'available')
    search_fields = ('name',)
    list_filter = ('available',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'rating', 'verified', 'order')
    search_fields = ('name', 'text')


class GalleryItemInline(TranslatableStackedInline):
    model = GalleryItem
    extra = 0
    fields = ('file', 'title')


@admin.register(Gallery)
class GalleryAdmin(TranslatableAdmin):
    list_display = ('id', 'text')
    list_display_links = ('id', 'text')
    inlines = [GalleryItemInline]
