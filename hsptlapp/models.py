from django.db import models

# Create your models here.
class Doctors(models.Model):
    doc_name=models.CharField(max_length=200)
    doc_img=models.ImageField(upload_to='pics')
    doc_spec=models.CharField( max_length=150)
    
    def __str__(self):
       return 'Dr.'+ self.doc_name +'- ('+ self.doc_spec + ')'
   
class Booking(models.Model):
    p_name=models.CharField(max_length=150)
    p_ph=models.CharField(max_length=50)
    doc_name=models.ForeignKey(Doctors,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on=models.DateField(auto_now=True)