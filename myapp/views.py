from django.shortcuts import render
def home(request):
	#text = """<h1>welcome to my app </h1>"""
	#return HttpResponse(text)
	return render(request,"Automobile_sales/home.html",{})
