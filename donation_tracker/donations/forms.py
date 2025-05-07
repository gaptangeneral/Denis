
from django import forms
from .models import Donation

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['name_surname', 'phone_number', 'amount', 'donation_status', 'explanation'] # donation_status eklendi

        widgets = {
            'name_surname': forms.TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Your Name and Surname'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Your Phone Number (e.g., +1234567890)'
            }),
            'amount': forms.NumberInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Donation Amount (USD)'
            }),
            'donation_status': forms.Select(attrs={ # Seçim alanı için Select widget'ı
                'class': 'form-select mb-2' # Bootstrap 5 için form-select sınıfı
            }),
            'explanation': forms.Textarea(attrs={
                'class': 'form-control mb-2',
                'rows': 3,
                'placeholder': 'General explanation or reason if not completed' # Placeholder güncellendi
            }),
        }
        labels = { # İngilizce etiketler için
            'name_surname': 'Full Name',
            'phone_number': 'Phone Number',
            'amount': 'Amount (USD)',
            'donation_status': 'Donation Status',
            'explanation': 'Explanation / Reason if Not Completed',
        }