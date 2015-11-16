from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render
from lists.models import Item, List
from django.shortcuts import redirect, render


def home_page(request):
	return render(request, 'home.html')

def view_list(request,list_id):
	#pass
	list_=List.objects.get(id=list_id)
	if request.method=='POST':
		Item.objects.create(text=request.POST['item_text'],list=list_)
		return redirect('/lists/%d/'%(list_.id))
	#items=Item.objects.all()
	#return render(request,'list.html',{'items':items})
	return render(request,'list.html',{'list':list_})

def new_list(request):
	#Item.objects.create(text=request.POST['item_text'])
	#return redirect('/lists/the-only-list-in-the-world/')
	list_=List.objects.create()
	item=Item.objects.create(text=request.POST['item_text'],list=list_)
	try:
		item.full_clean()
		item.save()
	except ValidationError:
		#pass
		list_.delete()
		error="You can't have an empty list item"
		return render(request,'home.html',{"error":error})

		#return redirect('/lists/the-only-list-in-the-world/')
	return redirect('/lists/%d/' % (list_.id,))

#def add_item(request,list_id):
#	list_=List.objects.get(id=list_id)
#	Item.objects.create(text=request.POST['item_text'],list=list_)
#	return redirect('/lists/%d/' % (list_.id,))