from django.contrib import admin

# Register your models here.
from .models import Test, Contact, Tag

# admin.site.register([Test, Contact, Tag])

# -------------------------------------------


# class ContactAdmin(admin.ModelAdmin):
#     fields = ('name', 'email')

# class ContactAdmin(admin.ModelAdmin):
#     fieldsets = (
#         ['Main',{
#             'fields':('name','email'),
#         }],
#         ['Advance',{
#             'classes': ('collapse',), # CSS
#             'fields': ('age',),
#         }]
#     )
#
#
# admin.site.register(Contact, ContactAdmin)
# admin.site.register([Test, Tag])

# -------------------------------------------

class TagInline(admin.TabularInline):
    model = Tag

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email')  # list
    inlines = [TagInline]  # Inline
    fieldsets = (
        ['Main', {
            'fields': ('name', 'email'),
        }],
        ['Advance', {
            'classes': ('collapse',),
            'fields': ('age',),
        }]

    )


admin.site.register(Contact, ContactAdmin)
admin.site.register([Test])