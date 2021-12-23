from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from  account.models import AccountUser

# Register your models here.

class UserCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required fields,
    plus a repeated password.

    """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation',
                                widget=forms.PasswordInput)

    class Meta:
        model = AccountUser
        fields = ('email', 'first_name', 'last_name',)

    def clean_password2(self):
        """
        Check that two password entries match
        :return:
        """
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError('Password dont match')
        return password2

    def save(self, commit=True):
        """
        Save the provided pasword in hashed format
        :param commit:
        :return:
        """

        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
        """
        A form for updating users. Includes all the fields on the user but replaces
        but replaces the password field with admin's disabled password hash
        diplay field
        """
        password = ReadOnlyPasswordHashField()

        class Meta:
            model = AccountUser
            fields = ('email', 'password', 'first_name', 'last_name', 'is_active',)
                      # 'is_admin', 'is_student', 'is_instructor')


class UserAdmin(BaseUserAdmin):
        """
        The forms to add and change user intances
        """

        form = UserChangeForm
        add_form = UserCreationForm
        # The field to be used in displaying the User Model.
        # These overide the definitions on the base UserAdmin
        # that reference specific fields on authuser

        list_display = ('email','first_name','last_name','is_admin')
                        # ,'is_student','is_instructor')
        list_filter = ('is_admin',)
        fieldsets = (
        (None, {'fields' : ('email','password','username')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_admin','is_staff')})
        )

        # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
        # overrides get_fieldsets to use this attribute when creating a user.
        add_fieldsets = (
            (None, {
                'classes': ('wide',),
                'fields' : ('email', 'firs_name', 'last_name',
                            'password1', 'password2'),
            }),
        )
        search_fields = ('email',)
        ordering = ('email',)
        filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(AccountUser, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)








