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

#class ItemModelTest(TestCase):

class ListAndItemModelsTest(TestCase):

	def test_saving_and_retrieving_items(self):
		list_=List()
		list_.save()

		first_item=Item()
		first_item.text='The first (ever) list item'
		first_item.list=list_
		first_item.save()

		second_item=Item()
		second_item.text='Item the second'
		second_item.list=list_
		second_item.save()

		saved_list=List.objects.first()
		self.assertEqual(saved_list,list_)

		saved_items=Item.objects.all()
		self.assertEqual(saved_items.count(),2)

		first_saved_item=saved_items[0]
		second_saved_item=saved_items[1]
		self.assertEqual(first_saved_item.text, 'The first (ever) list item')
		self.assertEqual(first_saved_item.list,list_)
		self.assertEqual(second_saved_item.text, 'Item the second')
		self.assertEqual(second_saved_item.list,list_)

	def test_cannot_save_empty_list_items(self):
		list_=List.objects.create()
		item=Item(list=list_,text='')
		with self.assertRaises(ValidationError):
			#try:
				item.save()
				item.full_clean()
			#	self.fail('The save should have raised an exception')
			#except ValidationError:
			#	pass

	def test_get_absolute_url(self):
		list_=List.objects.create()
		self.assertEqual(list_.get_absolute_url(),'/lists/%d/'%(list_.id,))

