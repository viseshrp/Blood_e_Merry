from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
import logging
from django.urls import reverse
from ipware.ip import get_ip

from loginsignup.forms import RegistrationForm

logger = logging.getLogger(__name__)


# Create your views here.

# use generic views

def home(request):
    return render(request, 'loginsignup/index.html', {})


def confirmation(request):
    return render(request, 'loginsignup/confirmation.html', {})


def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)  # takes the post data from request
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.donor.phone = form.cleaned_data.get('phone')
            user.donor.city = form.cleaned_data.get('city')
            user.donor.state = form.cleaned_data.get('state')
            user.donor.country = form.cleaned_data.get('country')
            user.save()
            user.donor.save()
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=user.username, password=raw_password)
            # login(request, user)
            return HttpResponseRedirect(reverse('loginsignup:confirmation'))
        else:
            logger.error('Form invalid')
            return render(request, 'loginsignup/signup.html', {'form': form, 'error_message': "Form data invalid!", })
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            # # if user is not None:
            # login(request, user)

    else:
        form = RegistrationForm()
        return render(request, 'loginsignup/signup.html', {'form': form})


def profile(request):
    args = {'user': request.user}
    client_address = get_ip(request)
    logger.error('ip=' + client_address)
    return render(request, 'loginsignup/profile.html', args)

# def vote(request, question_id):
#     question = get_object_or_404(Donor, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # when there's no choice selected, re display the vote form
#         return render(request, 'polls/detail.html', {'question': question, 'error_message': "No choice, idiot!", })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
