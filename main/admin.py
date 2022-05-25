from django.contrib import admin

# Register your models here.
import main.models

admin.site.register(main.models.Places)
admin.site.register(main.models.Nodes)
admin.site.register(main.models.Shop)