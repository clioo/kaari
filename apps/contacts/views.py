from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from apps.contacts.models import Contact,OurListingInterest
from apps.listings.models import Listing
from django.core.mail import EmailMessage


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        name = request.POST['name']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
        contact, created = Contact.objects.get_or_create(
                            phone=phone,
                            defaults={'name':name}
                            )
        listing = Listing.objects.get(id=listing_id)
        interest = OurListingInterest(listing=listing,message=message)
        interest.save()
        contact.our_listing_interest.add(interest.id)
            
        send_mail(
          subject='Nuevo interés en tu bien.',
          message='',
          html_message="""
          <h1>¡Hubo un nuevo interés en tu bien!</h1>
          <h2>Mensaje del prospecto:</h2>
          <br>
          <h2><strong>"{2}"</strong></h2>
          <br>
          <h3>
          Comunícate lo antes posible con {0} al teléfono <strong>{1}.</strong>
          </h3>
          """.format(name,phone,message),
          from_email='Equipo kaari',
          recipient_list=['19jesusacosta96@gmail.com', realtor_email],
          fail_silently=False,
        )
        # email = EmailMessage(
        #     subject='Nuevo interés en tu bien.',
        #     body="""
        #     Comunícate con {0} al teléfono <strong>{1}.</strong>
        #     """.format(name,phone),
        #     from_email='Equipo kaari',
        #     to=['19jesusacosta96@gmail.com', realtor_email],
        #     reply_to=[realtor_email],
        # )

        messages.success(
            request, 'Gracias por tu interés, nuestros agentes se pondrán en contacto contigo.')
        return redirect('/listings/'+listing_id)
