from django.shortcuts import render
from django.http import HttpResponse

prestamos = [
]

def index(request):
    if request.method == 'POST':
        #monto: m, tasa: r, plazo: n
        m = int(request.POST.get('monto'))
        r = int(request.POST.get('tasa'))
        n = int(request.POST.get('plazo'))

        r = r / 100 / 12 #tasa mensual
        n = n * 12 #plazo en meses

        c = round((m * r) / (1 - (1 + r) ** -n), 2)   

        prestamos.append({
            'monto': m,
            'tasa': f'{r * 100 * 12}%', #tasa ingresada originalmente
            'plazo': f'{int(n / 12)}', #plazo original ingresado 
            'cuota': c,
            'total_pagar': round((c * n),2), #el plazo ya esta en meses, para saber el total a pagar al final solo multiplico por n
        })

        ctx = {
            'prestamos' : prestamos,
        }

        return render(request, 'app1/index.html', ctx)
    else:
        #Metodo GET
        #contexto que va a la plantilla
        ctx = {
            'prestamos' : prestamos,
        }

        return render(request, 'app1/index.html', ctx)