from django.contrib import admin
# Register your models here.

from my_app.models import Beverage, Review


from my_app.models import UserProfile
admin.site.register(UserProfile)

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('name','rating', 'user_name', 'comment', 'pub_date')
    list_filter = ['pub_date', 'user_name', 'name']
    search_fields = ['comment', 'name']

admin.site.register(Beverage)
admin.site.register(Review, ReviewAdmin)