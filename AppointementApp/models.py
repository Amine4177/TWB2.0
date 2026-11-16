from django.db import models

# Create your models here.

class Appointment(models.Model):
    reason=models.TextField()
    prescription=models.FileField(
        blank=True,
        upload_to='prescription'
    )
    class Status(models.TextChoices):
        PENDING = "PENDING","En attente"
        CONFIRMED = "CONFIRMED","confirmé"
        CANCELLED = "CANCELLED","Annulé"
    status=models.CharField(max_length=10,choices=Status.choices,default=Status.PENDING)
    duration_minutes=models.PositiveIntegerField(default=30)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    appointment_date=models.DateField()
    doctor=models.ForeignKey("AccountApp.Doctor",models.CASCADE,related_name="appointements")
    patient=models.ForeignKey("AccountApp.Patient",models.CASCADE,related_name="appointements")
    class Meta:
        ordering=["appointment_date"]
        constraints=[
            models.UniqueConstraint(
                fields= ["doctor","appointment_date"],
                name="unicite-patient-doctor-date",
                violation_error_message="ce docteur possede un rdv avec cette date"
            )
        ]