from django.contrib import admin
from .models import Empleos,Empresas,perfiles,comentarios

# Register your models here.
class EmpleosAdmin(admin.ModelAdmin):
    list_display = ["nombre","description","paga"]
    list_editable = ["description"]
    search_fields = ["nombre", "description"]
    list_filter = ["nombre"]
    list_per_page = 2

class EmpresasAdmin(admin.ModelAdmin):
    list_display = ["Marca","description","jornadas"]
    list_editable = ["description"]
    search_fields = ["Marca", "description"]
    list_filter = ["Marca"]
    list_per_page = 2
    

admin.site.register(Empresas,EmpresasAdmin )
admin.site.register(perfiles)
admin.site.register(Empleos, EmpleosAdmin)
admin.site.register(comentarios)
