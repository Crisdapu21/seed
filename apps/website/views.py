from django.shortcuts import render

def indexWebsite(request):
	data = { 
	# "something" : something,
	}
	return render(request,'indexWebsite.html',data)
