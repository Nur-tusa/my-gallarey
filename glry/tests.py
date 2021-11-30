
  
from django.test import TestCase
from .models import photos, gallery_category, Location

# Create your tests here.
class TestImage(TestCase):
    def setUp(self):
        self.location = Location(name='Town')
        self.location.save_location()

        self.category = gallery_category(name='Home')
        self.category.save_category()

        self.image_test = photos(id=1, name='image', description='this is a test image', location=self.location, category=self.category)

    def test_instance(self):
        self.assertTrue(isinstance(self.image_test, photos))

    def test_save_image(self):
        self.image_test.save_image()
        after = photos.objects.all()
        self.assertTrue(len(after) > 0)

    def test_delete_image(self):
        self.image_test.delete_image()
        images = photos.objects.all()
        self.assertTrue(len(images) == 0)

    def test_update_image(self):
        self.image_test.save_image()
        self.image_test.update_image(self.image_test.id, 'images/oar.jpg')
        changed_img = photos.objects.filter(image='images/oar.jpg')
        self.assertTrue(len(changed_img) > 0)

    def test_get_image_by_id(self):
        found_image = self.image_test.get_image_by_id(self.image_test.id)
        image = photos.objects.filter(id=self.image_test.id)
        self.assertTrue(found_image, image)

    def test_search_image_by_location(self):
        self.image_test.save_image()
        found_images = self.image_test.filter_by_location(location='Town')
        self.assertTrue(len(found_images) == 1)

    def test_search_image_by_category(self):
        category = 'Home'
        found_img = self.image_test.search_by_category(category)
        self.assertTrue(len(found_img) > 1)

    def tearDown(self):
        photos.objects.all().delete()
        Location.objects.all().delete()
        gallery_category.objects.all().delete()

