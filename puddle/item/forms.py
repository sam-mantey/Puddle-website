from  django import forms
from .models import Item

Input_class = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'item_image', )

        widgets = {
            'category': forms.Select(attrs = {
                'class': Input_class, 
            }), 

            'name': forms.TextInput(attrs = {
                'class': Input_class, 
            }),

            'description': forms.Textarea(attrs = {
                'class': Input_class, 
            }), 
            
            'price': forms.TextInput(attrs = {
                'class': Input_class, 
            }),

            'item_imaage': forms.FileInput(attrs = {
                'class': Input_class, 
            })
        }


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'item_image', 'is_sold', )

        widgets = { 
            'name': forms.TextInput(attrs = {
                'class': Input_class, 
            }),

            'description': forms.Textarea(attrs = {
                'class': Input_class, 
            }), 
            
            'price': forms.TextInput(attrs = {
                'class': Input_class, 
            }),

            'item_imaage': forms.FileInput(attrs = {
                'class': Input_class, 
            })
        }
