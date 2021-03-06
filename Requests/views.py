from django.shortcuts import render_to_response
from Requests.forms import Volunteer_ngo_request_form, Recurring_request_form
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from Requests.models import Volunteer_ngo_request,Events,Projects
from Registration.models import User,UserProfile

@login_required
def volunteer_request(request):
#make changes to automatically take sender id.
#make the recepient box a search and select box of ngo names
#make date and time selectable on a popup calendar
    request_sent = False
    context = RequestContext(request)
    username = request.session['username']
    if request.method == 'POST':
        request_type = request.POST.get('request_type')
        if request_type == "One Time":
            request_form = Volunteer_ngo_request_form(data=request.POST)
            if request_form.is_valid():
                new_request=request_form.save(commit=False)
                user_id = User.objects.get(username = request.session['username'])
                new_request.sender = user_id.id
                if request.POST.get('req_type')=='Event':
                    new_request.status='Accept'
                    new_request.date_vol=Events.objects.get(id=new_request.recepient).startdate_vol
                if request.POST.get('req_type')=='Project':
                    new_request.status='Accept'
                    new_request.date_vol=Projects.objects.get(id=new_request.recepient).startdate_vol
                new_request.req_type=request.POST.get('req_type')

                new_request.save()
            else:
                print request_form.errors

        else:
            recform = Recurring_request_form(data=request.POST)
            if recform.is_valid():
                new_request = recform.save(commit=False)
                user_id = User.objects.get(username = request.session['username'])
                new_request.sender = user_id.id
                new_request.save()
            else:
                print recform.errors

    return HttpResponseRedirect('/home/volunteer')

