from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import contactform
from django.contrib import messages


# Create your views here.


def accueil(request, *args, **kwargs):
    if request.method == 'POST':
        form = contactform(request.POST)
        if form.is_valid():
            # Récupérer les données du formulaire
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Construire le message
            full_message = f"Message de {name} ({email}):\n\n{message}"
            
            # Envoyer l'email
            send_mail(
                subject='Nouveau message du formulaire de contact',
                message=full_message,
                from_email=email,
                recipient_list=['romaricthiombiano4@gmail.com'],  # Remplacez par votre email
                fail_silently=False,
            )
            
             # Ajouter un message de succès
            messages.success(request, 'Votre message a été envoyé avec succès!')
            
        # Rediriger vers le même endroit sur la page avec un hash pour l'id contact
        return redirect('/#contact')
        

    else:
        form = contactform()

    return render(request, 'index.html', {'form': form})
