from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

layout="""
    <h1>Proyecto Web (LP3) | LLanos Rojas</h1>
    <hr/>
    <ul>
        <li>
            <a href="/inicio">Inicio</a>
        </li>
    </ul>
    <hr/>
"""

def index(request):
        return render(request,"index.html", {'titulo':'Proyecto Web DJango LP3','autor':'Mauricio'})