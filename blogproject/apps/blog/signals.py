from django.dispatch import Signal,receiver
from apps.blog.models import BlogPost
from django.core.mail import send_mail
email_signal = Signal()

@receiver(email_signal)
def email(sender, **kwargs):
    subject = kwargs.get('subject')
    message = kwargs.get('message')
    to_email = kwargs.get('to_email')
    print("mail sent")
    send_mail(subject="subject",message="message",from_email="Chandreshkanzariya19123@gmail.com",recipient_list=['Chandreshkanzariya19123@gmail.com'])