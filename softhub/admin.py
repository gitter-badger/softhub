from django.contrib import admin

# Register your models here.
from .models.OperatingSystem import OperatingSystem
from .models.Application import Application
from .models.User import User
from .models.Developer import Developer
from .models.Version import Version
from .models.Executable import Executable


admin.site.register(User)
admin.site.register(Developer)
admin.site.register(OperatingSystem)
admin.site.register(Application)
admin.site.register(Version)
admin.site.register(Executable)