from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from apps.contacts.models import Contact,OurListingInterest
from apps.listings.models import Listing


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
          message="""
          Comunícate con {name} al teléfono <strong>{phone}.</strong>
          """.format(),
          from_email='Equipo kaari',
          recipient_list=['19jesusacosta96@gmail.com', realtor_email],
          fail_silently=False
        )

        messages.success(
            request, 'Gracias por tu interés, nuestros agentes se pondrán en contacto contigo.')
        return redirect('/listings/'+listing_id)
