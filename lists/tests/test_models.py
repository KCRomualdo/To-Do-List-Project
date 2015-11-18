	#from lists.models import Item
#from lists.models import Item,List
#from django.core.urlresolvers import resolve
from django.core.exceptions import ValidationError
from django.test import TestCase
from lists.models import Item,List
#from django.http import HttpRequest
#from django.template.loader import render_to_string

#from lists.views import home_page

# Create your tests here.

#class HomePageTest(TestCase):

#	def test_root_url_resolvers_to_home_page_view(self):
#		found=resolve('/')
#		self.assertEqual(found.func,home_page)

#	def test_home_page_returns_correct_html(self):
#		request=HttpRequest()
#		response=home_page(request)
#		expected_html=render_to_string('home.html')
#		self.assertEqual(response.content.decode(),expected_html)

class ItemModelTest(TestCase):

	def test_default_text(self):
		item=Item()
		self.assertEqual(item.text,'')

	def test_item_is_related_to_list(self):
		list_=List.objects.create()
		item=Item()
		item.list=list_
		item.save()
		self.assertIn(item,list_.item_set.all())

class ListModelsTest(TestCase):

	#def test_cannot_save_empty_list_items(self):
	#	list_=List.objects.create()
	#	item=Item(list=list_,text='')
	#	with self.assertRaises(ValidationError):
			#try:
	#			item.save()
	#			item.full_clean()
			#	self.fail('The save should have raised an exception')
			#except ValidationError:
			#	pass

	def test_get_absolute_url(self):
		list_=List.objects.create()
		self.assertEqual(list_.get_absolute_url(),'/lists/%d/'%(list_.id,))

	def test_duplicate_items_are_invalid(self):
		list_=List.objects.create()
		Item.objects.create(list=list_, text='bla')
		with self.assertRaises(ValidationError):
			item=Item(list=list_, text='bla')
			item.full_clean()
			#item.save()

	def test_CAN_save_same_time_to_different_lists(self):
		list1=List.objects.create()
		list2=List.objects.create()
		Item.objects.create(list=list1,text='bla')
		item=Item(list=list2,text='bla')
		item.full_clean()

	def test_list_ordering(self):
		list1=List.objects.create()
		item1=Item.objects.create(list=list1,text='i1')
		item2=Item.objects.create(list=list1,text='item 2')
		item3=Item.objects.create(list=list1,text='3')
		self.assertEqual(
			list(Item.objects.all()),
			[item1,item2,item3]
		)

	def test_string_representation(self):
		item=Item(text='some text')
		self.assertEqual(str(item),'some text')
