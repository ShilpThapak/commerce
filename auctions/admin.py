from django.contrib import admin
from .models import activelistings, categories, comments, bids, User

# Register your models here.
admin.site.register(activelistings)
admin.site.register(categories)
admin.site.register(comments)
admin.site.register(bids)
admin.site.register(User)
