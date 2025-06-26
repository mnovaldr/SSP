from django.contrib import admin
from . models import Barang, Jenis

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group

from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
from unfold.admin import ModelAdmin


admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    # Forms loaded from `unfold.forms`
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass

# Register your models here.

class BarangAdmin(ModelAdmin):
    list_display = ['kdbrg', 'nama', 'stok', 'harga', 'jenis', 'waktu_post']
    search_fields = ['kdbrg', 'nama', 'jenis__nama']
    list_filter = ['jenis',]
    list_per_page = 3

    def get_jenis(self, obj):
        return obj.jenis.nama
    get_jenis.short_description = 'Jenis'

class JenisAdmin(ModelAdmin):
    list_display = ['nama', 'deskripsi']
    search_fields = ['nama']
    list_per_page = 5

admin.site.register(Barang, BarangAdmin)
admin.site.register(Jenis, JenisAdmin)