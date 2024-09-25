from datetime import datetime

from django.forms import ModelForm, TextInput, Textarea, forms, Form, ModelChoiceField, Select, DateInput, CharField
from core.erp.models import Category, Product, Client, Sale
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker


class CategoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
       # for form in self.visible_fields():
        #    form.field.widget.attrs['class'] = 'form-control'
         #   form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['name'].widget.attrs['autofocus'] = True
    
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Ingrese un Nombre',
                }
            ),
            'desc': Textarea(
                attrs={
                    'placeholder': 'Ingrese una Descripcion',
                    'rows': 3,
                    'columns': 3
                }
            )
        }
        exclude = ['user_creation', 'user_updated']

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


    #
    # def clean(self):
    #     cleaned = super().clean()
    #     if len(cleaned['name']) <= 50:
    #         raise forms.ValidationError('Validacion sdfsdsdf')
    #         # self.add_error('name', 'Le faltan caracteres')
    #     return cleaned



class ProductForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Ingrese el nombre del Producto',
                }
            ),
        }
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data



class TestForm(Form):
    categories = ModelChoiceField(queryset=Category.objects.all() , widget=Select({
        'class': 'form-control select2',
        'style': 'width: 100%'

    }))

    products = ModelChoiceField(queryset=Product.objects.none(), widget=Select({
        'class': 'form-control select2',
        'style': 'width: 100%'

    }))

    #search = CharField(widget=TextInput(attrs={
     #   'class': 'form-control',
      #  'placeholder': 'Ingrese una descripcion'
    #}))

    search = ModelChoiceField(queryset=Product.objects.none(), widget=Select(attrs={
        'class': 'form-control select2',
        'style': 'width: 100%'

    }))



class ClientForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['names'].widget.attrs['autofocus'] = True

    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'names': TextInput(
                attrs={
                    'placeholder': 'Ingrese sus nombres',
                }
            ),
            'surnames': TextInput(
                attrs={
                    'placeholder': 'Ingrese sus apellidos',
                }
            ),
            'dni': TextInput(
                attrs={
                    'placeholder': 'Ingrese su Dni',
                }
            ),
            'date_birthday': DateInput(format='%Y-%m-%d',
                attrs={
                    'value': datetime.now().strftime('%Y-%m-%d'),
                }
            ),
            'address': TextInput(
                attrs={
                    'placeholder': 'Ingrese su direccion',
                }
            ),
            'gender': Select()
        }
        exclude = ['user_updated', 'user_creation']

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                instance = form.save()
                data = instance.toJSON()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class SaleForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cli'].queryset = Client.objects.none()
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'


        # # Forma 2
        # self.fields['date_joined'].widget.attrs = {
        #     'autocomplete': 'off',
        #     'class': 'form-control datetimepicker-input',
        #     'id': 'date_joined',
        #     'data-target': '#date_joined',
        #     'data-toggle': 'datetimepicker'
        # }


    class Meta:
        model = Sale
        fields = '__all__'
        widgets = {
            'cli': Select(attrs={
                'class': 'custom-select select2',
                #'style': 'width: 100%'
            }),
            'date_joined': DateInput(format='%Y-%m-%d', 
                            attrs={
                                'class': 'form-control datetimepicker-input',
                                'value': datetime.now().strftime('%Y-%m-%d'),
                                'autocomplete': 'off',
                                'id': 'date_joined',
                                'data-target': '#date_joined',
                                'data-toggle': 'datetimepicker'
            }),

            'subtotal': TextInput(attrs={
                'readonly': True,
                'class': 'form-control',
            }),
            'iva': TextInput(attrs={
                'class': 'form-control',
            }),
            'total': TextInput(attrs={
                'readonly': True,
                'class': 'form-control',
            })
        }


