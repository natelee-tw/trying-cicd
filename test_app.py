import unittest
from unittest.mock import patch, Mock
from app import get_greeting, get_random_pokemon

class TestApp(unittest.TestCase):
    def test_get_greeting(self):
        self.assertEqual(get_greeting(), "Hello, world! This is a Streamlit app.")
    
    @patch('app.requests.get')
    def test_get_random_pokemon(self, mock_get):
        # Mock successful API response
        mock_response = Mock()
        mock_response.json.return_value = {
            'name': 'pikachu',
            'id': 25,
            'sprites': {'front_default': 'https://example.com/pikachu.png'},
            'types': [{'type': {'name': 'electric'}}]
        }
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response
        
        pokemon = get_random_pokemon()
        
        self.assertIsNotNone(pokemon)
        if pokemon:  # Add null check to satisfy linter
            self.assertEqual(pokemon['name'], 'Pikachu')
            self.assertEqual(pokemon['id'], 25)
            self.assertEqual(pokemon['types'], ['Electric'])

if __name__ == "__main__":
    unittest.main()
