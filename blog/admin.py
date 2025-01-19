from django.contrib import admin

admin.site.register(

  Tag , PostAdmin
)

class PostAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)}
