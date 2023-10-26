from django.db import models


from django.db import models


class Birthday(models.Model):
    first_name = models.CharField('Имя', max_length=20)
    last_name = models.CharField(
        'Фамилия', blank=True, help_text='Необязательное поле', max_length=20
    )
    birthday = models.DateField('Дата рождения')


from django import forms
from .models import Contest

class ContestForm(forms.ModelForm):
    class Meta:
        model = Contest
        fields = '__all__'
        widgets = {
            'comment': forms.Textarea({'cols': '22',
                                       'rows': '5'
                                       }),
            'description': forms.Textarea({'cols': '22',
                                       'rows': '5'
                                       }),
        }
        
        
        
        from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Contest(models.Model):
    title = models.CharField(
        'Название', 
        max_length=20
    )
    description = models.TextField(
        'Описание',
    )
    price = models.IntegerField(
        'Цена',
        validators=[MinValueValidator(10), MaxValueValidator(100)],
        help_text='Рекомендованная розничная цена',
    )
    comment = models.TextField(
        'Комментарий',
        blank=True,
    )      
        