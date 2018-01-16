from django.shortcuts import render, redirect
from datetime import *
#importaciones propias
from django.http import HttpResponse
from django.http import HttpResponseRedirect
#imports proyecto
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from models import Evento
from models import Conferencia
from models import Pregunta
from models import RelUe
from models import Usuario
from models import RelPregunta
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib import auth
from django.core.urlresolvers import reverse_lazy
from enc.forms import RegistroForm
from django.template import RequestContext
# Create your views here
import os



def conferencia(request):
	if request.user.is_authenticated():
		#evento = request.POST['evento'] 
		#conf = Conferencia.objects.filter(id_evento = evento)
		preg = Pregunta.objects.all()
		
	return render_to_response('encuesta/conferencias.html',{'preg':preg})

def pregunta(request):
	if request.method == 'POST':
		preg = Pregunta.objects.all()	
		usuario = request.user.id
		##se extrae el evento en el que el usuario esta registrado
		relevent = RelUe.objects.filter(id_usuario = usuario).values('id_evento')
		relues = RelUe.objects.filter(id_usuario = usuario).values('id_rel_ue')
		event = Evento.objects.filter(id_evento = relevent).values('id_evento')
		
		conferencia = Conferencia.objects.filter(id_evento = event).values('id_conf')
		relacion = RelPregunta.objects.filter(id_conf = 6).values('id_relp')
		for dato in relacion:
		    evento = request.POST[str(dato)]
		    print(evento)
		    #relev = RelPregunta(id_rel_ue =  relues, id_relp = dato, calificacion = int(evento), texto = evento)
		    #relev.save()			
	else:
		preg = Pregunta.objects.all()	
		usuario = request.user.id
		##se extrae el evento en el que el usuario esta registrado
		relevent = RelUe.objects.filter(id_usuario = usuario).values('id_evento')
		relacion = RelPregunta.objects.all().values('id_conf', 'id_pregunta', 'tipo', 'id_relp')
		event = Evento.objects.filter(id_evento = relevent).values('id_evento')
		
		conferencia = Conferencia.objects.filter(id_evento = event)
		#session = request.session["nombre"]
		return render(request, 'encuesta/preguntas.html',{'preg':preg, 'conferencia':conferencia, 
			'rel':relacion})		


def evento(request):
	if request.user.is_authenticated():
		if request.method == 'POST':			
			evento = request.POST['evento']
			print(evento)
			usuario = request.user.id
			print("hello")
			user = Usuario.objects.get(id_usuario = usuario)#Instancias por la llave foranea
			event = Evento.objects.get(id_evento = evento) 
			relev = RelUe(id_usuario = user, id_evento = event, estatus = 0)
			relev.save()			
			return redirect('/preguntas')
		else:
			try:
				usuario = request.user.id
				relacion = RelUe.objects.get(id_usuario = usuario)
				return redirect('/preguntas')
			except RelUe.DoesNotExist:
					relacion = None
					if request.user.is_authenticated():
						print("usuario activo")
						usuario = request.user.id
						email = request.user.email
						fecha = request.user.date_joined
						saveUser = Usuario(id_usuario = usuario, email = email, fecha_reg = fecha)
						saveUser.save()
						event = Evento.objects.filter(fecha_fin__gt = (date.today() - timedelta(days=10)))
						total = 0
						for dato in event:
							total += 1
						print(total)
						#request.session["nombre"] = "Guillermo"
						#atributo = request.session["nombre"]
						return render(request, 'encuesta/eventos.html', {'event':event})

	else:
		return redirect('/')
		
   
# se genera la relacion de el usuario con el evento

	


class RegistroUsuario(CreateView):
	model = User
	template_name = "encuesta/registrar.html"	
	form_class = RegistroForm
	success_url = reverse_lazy('index')
     
#def selecciona(request):
#	if request.user.is_authenticated:
#		evento = Evento.objects.filter(fecha_in <= datetime.now())
#		idUsuario = request.user.id
#		nombreUsuario = request.user.username


#flujo de datos

