from django.contrib import admin

from application.models import menu, orderplaced, verification


admin.site.register(menu)
admin.site.register(orderplaced)
admin.site.register(verification)
