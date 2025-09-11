from django import forms
from dashboard.models import Order, OrderItem, Item

# ✅ Order ဖောင် - စားပွဲ/table ရွေးရန်အတွက်
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['table']  


class OrderItemForm(forms.ModelForm):
    item = forms.ModelChoiceField(
        queryset=Item.objects.all(),
        label="ပစ္စည်း",
        widget=forms.Select,
        empty_label="ရွေးပါ",
    )

    class Meta:
        model = OrderItem
        fields = ['item', 'quantity']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Customize labels shown in dropdown
        self.fields['item'].label_from_instance = lambda obj: f"{obj.name} - {obj.description[:30]} - {obj.price} MMK"

