# Django
from django.test import TestCase

# Python
import json

# Django Rest Framework
from rest_framework.test import APIClient
from rest_framework import status


class FilmTestCase(TestCase):
    """
    Test to check the proper functioning of the list and create movies function

    """
    def setUp(self):
        client = APIClient()

        response_planets = client.post(
            '/movies/planets/', {"state": True,
                                 "name": "Naboo",
                                 "location": "Territorios del Borde Medio"}, format='json')

        result_planets = json.loads(response_planets.content)
        self.result_planets = result_planets

    def test_create_film(self):
        client = APIClient()

        film_data = {"state": True,
                     "name": "Rogue One: una historia de Star Wars",
                     "productor": "Kathleen Kennedy",
                     "director": "Gareth Edwards",
                     "company_producer": "The Walt Disney Company",
                     "release_date": "2022-11-15",
                     "planets": [1]}

        response = client.post('/movies/movies/', film_data, format='json')

        content = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertIn('id', content)
        self.assertIn('name', content)
        self.assertIn('state', content)
        self.assertIn('director', content)
        self.assertIn('productor', content)
        self.assertIn('release_date', content)
        self.assertIn('company_producer', content)
        self.assertIn('planets', content)
        self.assertIs(type(content.get('planets')), list)

        if 'id' in content and 'created_date' in content:
            del content['id']
            del content['created_date']

        if 'open_text' not in film_data and 'open_text' in content:
            self.assertEqual(content.get('open_text'), '')
            del content['open_text']

        self.assertEqual(content, film_data)

    def test_get_by_list_film(self):

        client = APIClient()

        response = client.get('/movies/movies/')

        result = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIs(type(result), list)

        for character in result:
            self.assertIn('id', character)
            self.assertIn('name', character)
            self.assertIn('state', character)
            self.assertIn('director', character)
            self.assertIn('productor', character)
            self.assertIn('release_date', character)
            self.assertIn('company_producer', character)
            self.assertIn('planets', character)
            self.assertIs(type(character.get('planets')), list)
            break


class PlanetTestCase(TestCase):
    """
    Test to check the proper functioning of the list and create planets function
    """
    def test_create_planet(self):
        client = APIClient()

        planet_data = {
            "state": True,
            "name": "Naboo",
            "location": "Territorios del Borde Medio"
        }

        response = client.post('/movies/planets/', planet_data, format='json')

        content = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertIn('id', content)
        self.assertIn('name', content)
        self.assertIn('state', content)
        self.assertIn('location', content)

        if 'id' in content and 'created_date' in content:
            del content['id']
            del content['created_date']

        self.assertEqual(content, planet_data)

    def test_get_by_list_planet(self):

        client = APIClient()

        response = client.get('/movies/planets/')

        result = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIs(type(result), list)

        for character in result:
            self.assertIn('id', character)
            self.assertIn('name', character)
            self.assertIn('state', character)
            self.assertIn('location', character)
            break
