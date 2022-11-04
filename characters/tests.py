# Django
from django.test import TestCase

# Python
import json

# Django Rest Framework
from rest_framework.test import APIClient
from rest_framework import status

from characters.models import Character


# Models


class CharacterTestCase(TestCase):
    def setUp(self):
        client = APIClient()

        response_planets = client.post(
            '/movies/planets/', {"state": True,
                                 "name": "Naboo",
                                 "location": "Territorios del Borde Medio"}, format='json')

        result_planets = json.loads(response_planets.content)
        self.result_planets = result_planets

        film_data = {"state": True,
                     "created_date": "2022-11-03",
                     "name": "Rogue One: una historia de Star Wars",
                     "productor": "Kathleen Kennedy",
                     "director": "Gareth Edwards",
                     "company_producer": "The Walt Disney Company",
                     "release_date": "2022-11-15",
                     "planets": [1]}

        response_film = client.post(
            '/movies/movies/', film_data, format='json')

        character_data_1 = {
            "movies": [1],
            "state": True,
            "name": "Luke Skywalker",
            "performer": "Mark Hamill"
        }

        character_data_2 = {
            "movies": [1],
            "state": True,
            "name": "Anakin Skywalker",
            "performer": "Hayden Christensen"
        }

        response_character_1 = client.post(
            '/characters/characters/',
            character_data_1,
            format='json'
        )

        character_id = json.loads(response_character_1.content).get('content')
        if 'id' in character_id:
            self.character_id = character_id['id']

        _ = client.post(
            '/characters/characters/',
            character_data_2,
            format='json'
        )

        result_movies = json.loads(response_film.content)
        self.result_movies = result_movies

    def test_create_character(self):
        client = APIClient()

        character_data = {
            "movies": [1],
            "state": True,
            "name": "Conde Dooku",
            "performer": "Christopher Lee"
        }
        response = client.post(
            '/characters/characters/',
            character_data,
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        content = result.get('content')
        self.assertIn('id', content)
        self.assertIn('movies', content)
        self.assertIn('state', content)
        self.assertIn('performer', content)

        if 'id' in content and 'created_date' in content:
            del content['id']
            del content['created_date']

        self.assertEqual(content, character_data)

    def test_get_by_list_character(self):

        client = APIClient()

        response = client.get('/characters/characters/')

        result = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIs(type(result), list)

        for character in result:
            self.assertIn('id', character)
            self.assertIn('movies', character)
            self.assertIn('name', character)
            self.assertIn('performer', character)
            break

    def test_get_by_filter_character(self):

        client = APIClient()

        response = client.get('/characters/characters/?search=Anakin')

        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for character in result:
            self.assertIn('id', character)
            self.assertIn('movies', character)
            self.assertIn('name', character)
            self.assertIn('performer', character)
            break

    def test_get_character(self):

        client = APIClient()

        response = client.get(f'/characters/characters/{self.character_id}/')

        character = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIs(type(character), dict)

        self.assertIn('id', character)
        self.assertIn('movies', character)
        self.assertIn('name', character)
        self.assertIn('performer', character)

    def test_update_character(self):
        client = APIClient()

        character_data = {
            "movies": [1],
            "state": True,
            "name": "Dark Tyranus",
            "performer": "Christopher Lee"
        }
        response = client.put(
            f'/characters/characters/{self.character_id}/',
            character_data,
            format='json'
        )

        result = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('id', result)
        self.assertIn('movies', result)
        self.assertIn('state', result)
        self.assertIn('performer', result)

    def test_delete_character(self):

        client = APIClient()

        response = client.delete(
            f'/characters/characters/{self.character_id}/',
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        character_exists = Character.objects.filter(pk=self.character_id)
        self.assertFalse(character_exists)
