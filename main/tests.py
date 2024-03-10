from django.test import TestCase

from .models import Pokemon, get_sprite_type


class PokemonTests(TestCase):
    def test_get_sprite_type(self):
        # Example sprite dicts
        complete_sprites = {
            "front_default": "front_default.png",
            "front_female": "front_female.png",
            "front_shiny": "front_shiny.png",
            "front_shiny_female": "front_shiny_female.png",
        }
        no_female_sprites = {
            "front_default": "front_default.png",
            "front_female": None,
            "front_shiny": "front_shiny.png",
            "front_shiny_female": None,
        }

        test_cases = [
            # Complete sprites
            (Pokemon(is_shiny=False, gender=2), complete_sprites, "front_default"),
            (Pokemon(is_shiny=True, gender=2), complete_sprites, "front_shiny"),
            (Pokemon(is_shiny=False, gender=1), complete_sprites, "front_female"),
            (Pokemon(is_shiny=True, gender=1), complete_sprites, "front_shiny_female"),
            (Pokemon(is_shiny=False, gender=3), complete_sprites, "front_default"),
            (Pokemon(is_shiny=True, gender=3), complete_sprites, "front_shiny"),
            # No female sprites
            (Pokemon(is_shiny=False, gender=1), no_female_sprites, "front_default"),
        ]

        for pokemon, api_sprites, expected in test_cases:
            actual = get_sprite_type(pokemon, api_sprites)
            self.assertEqual(
                actual,
                expected,
                f"A pokemon with shiny={pokemon.is_shiny}, gender={pokemon.display_gender()}, and available sprites: {api_sprites} should have a sprite '{expected}'",
            )
