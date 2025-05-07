from django.db import models

class Donation(models.Model):
    STATUS_PENDING = 'PENDING'
    STATUS_COMPLETED = 'COMPLETED'
    STATUS_NOT_COMPLETED = 'NOT_COMPLETED'

    # Alan için seçenekler (choices)
    DONATION_STATUS_CHOICES = [
        (STATUS_PENDING, 'Beklemede (Pending)'),
        (STATUS_COMPLETED, 'Tamamlandı (Completed)'),
        (STATUS_NOT_COMPLETED, 'Tamamlanmadı (Not Completed)'),
    ]
    name_surname = models.CharField(max_length=255, verbose_name='Adı Soyadı (Name Surname)')
    phone_number = models.CharField(max_length=20, verbose_name='Telefon Numarası (Phone Number)')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Bağışlanan Miktar (Donation Amount)')
    donation_status = models.CharField(
        max_length=20,
        choices=DONATION_STATUS_CHOICES,
        default=STATUS_PENDING,  # Varsayılan durum "Beklemede"
        verbose_name='Bağış Durumu (Donation Status)'
    )

    explanation = models.TextField(
        blank=True,
        null=True,
        verbose_name='Genel Açıklama / Tamamlanmama Nedeni (General Explanation / Reason if Not Completed)' # verbose_name güncellendi
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi (Creation Date)')

    def __str__(self):
        return f"{self.name_surname} - {self.amount} ({self.get_donation_status_display()})"

    class Meta:
        verbose_name = 'Bağış (Donation)'
        verbose_name_plural = 'Bağışlar (Donations)'