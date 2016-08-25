from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse

import json

from formapp.models import *


def index(request):
	if request.method == 'POST':
		data = dict(request.POST.iterlists())
		del data['csrfmiddlewaretoken']
		print data['formbuilder']
		builder = {'fields':data['formbuilder'][0]}
		del data['formbuilder']
		form = FormBuilder(id=1, data=data, builder=builder)
		form.save()
	return render_to_response('index.html',
    	context_instance=RequestContext(request))

def formbuilder(request):
	try:
		formbuilder = FormBuilder.objects.get(id=1)
		data = json.dumps({'data':formbuilder.data, 'builder':formbuilder.builder})
	except Exception as e:
		data = 'fail'
	mimetype = 'application/json'
	return HttpResponse(data, mimetype)