from django.contrib import admin

# Register your models here.
import main.models


admin.site.register(main.models.Shop)
admin.site.register(main.models.Product)

