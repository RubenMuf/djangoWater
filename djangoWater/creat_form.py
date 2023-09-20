from django import forms
from django.core.validators import RegexValidator, ValidationError

def p1(value):
    if not str(value).isalpha():
        raise forms.ValidationError('Введите только буквы,без цифр!')
    pass

def p2(value):
    if str(value)[0].islower():
        raise forms.ValidationError('Первая буква должна быть в верхнем регистре!')
    pass

def p3(value):
    if '@' not in str(value):
        raise forms.ValidationError('Почта должна содержать @ !')
    pass

def p4(value):
    if not str(value).endswith('.ru'):
        raise forms.ValidationError('почта должна заканчиваться на .ru')
    pass

def p5(value):
    if not str(value).startswith('+7'):
        raise forms.ValidationError('Телефон должен начинатся на +7')

def p6(value):
    if not str(value)[1:].isdigit():
        raise forms.ValidationError('Телефон не должен содержать буквы')

# def p7(value):
#     if len(str(value)) > 11 and len(str(value)) < 11:
#         raise forms.ValidationError('Телефон должен содержать только 11 цифр!')

class Creat_form(forms.Form):
    name = forms.CharField(label='Введите имя', max_length=15, validators=[p1, p2])

    lastname = forms.CharField(label='Введите фамилию',  validators=[p1, p2], required=False)

    E_mail = forms.EmailField(label='E-mail', validators=[p3, p4])

    tel = forms.CharField(label='Телефон:', validators=[p5, p6]) # RegexValidator('[+7][0-9]{11}', message='неправильный телефон')

    address = forms.CharField(label='Введите адрес')

    list_months = (('1', '1'), ('1', '3'), ('6', '6'), ('9', '9'), ('12', '12'))
    month = forms.TypedChoiceField(label='Количество месяцев:', choices=list_months)

    list_v = (('5', '5'), ('10', '10'), ('19', '19'))
    v = forms.TypedChoiceField(label='Объем бутыля:', choices=list_v)

    quantity = forms.IntegerField(label='Количество бутылей:', min_value=1)

