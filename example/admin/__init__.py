from django.contrib import admin

from example.admin.group_a import MyModelAdmin
from example.models.group_a import MyModel


admin.site.register(MyModel, MyModelAdmin)