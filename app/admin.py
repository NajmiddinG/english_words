from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from app.models import Word, General, CustomUser, KnowWord, Test, TestEnglish, Category
from django.utils.translation import gettext_lazy as _


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ['id', 'english', 'uzbek', 'date', 'category']
    search_fields = ['english', 'uzbek']
    # list_filter = ['created_user']


@admin.register(General)
class GeneralAdmin(admin.ModelAdmin):
    list_display = ['id', 'english', 'status']


@admin.register(CustomUser)
class UserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('CustomFields'), {'fields': ('image',)}),
    )


@admin.register(KnowWord)
class KnowWordAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_user', 'english', 'uzbek', 'date']


@admin.register(TestEnglish)
class TestEnglishAdmin(admin.ModelAdmin):
    list_display = ['id', 'tartib', 'english', 'uzbek', 'topilgan']


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'savollar_id', 'boshlanish_vaqt', 'tugash_vaqt', 'umumiy_soni', 'topgan_soni']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
