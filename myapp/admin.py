from django.contrib import admin
from myapp.models import contact
from myapp.models import userform
from myapp.models import feedback
from myapp.models import login_register


# Register your models here.
admin.site.register(contact)

admin.site.register(userform)

admin.site.register(feedback)

admin.site.register(login_register)





