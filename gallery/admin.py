from .models import HeroSection
from django.contrib import admin
from .models import Photo
from .models import Background


admin.site.register(Photo)


admin.site.register(HeroSection)

# Register your models here.


admin.site.register(Background)
