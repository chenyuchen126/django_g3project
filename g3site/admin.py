import uniout
from django.contrib import admin
from django.contrib.admin import site, ModelAdmin
from .models import Post
from .models import Address
from .models import Janet
from .models import Travel,Parking

def categories(instance):
    return ', '.join(instance.categories)

class PostAdmin(ModelAdmin):
    list_display = ['tags', categories]

admin.site.register(Parking)
admin.site.register(Post)
admin.site.register(Address)
admin.site.register(Janet, PostAdmin)
admin.site.register(Travel)

