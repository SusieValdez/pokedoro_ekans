from django.db import models
from django.contrib.auth.models import User


class Trainer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"<User: {self.user}>"


class Pokemon(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    is_shiny = models.BooleanField()
    # 1 = female, 2 = male, 3 = genderless
    gender = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"<Pokemon: {self.name} (shiny: {self.is_shiny}, gender: {self.display_gender()})>"

    def display_gender(self):
        if self.gender == 1:
            return "Female"
        if self.gender == 2:
            return "Male"
        if self.gender == 3:
            return "Genderless"


def get_sprite_type(pokemon, api_sprites):
    if pokemon.gender == 1 and api_sprites["front_female"] is not None:
        if pokemon.is_shiny:
            return "front_shiny_female"
        return "front_female"
    if pokemon.is_shiny:
        return "front_shiny"
    return "front_default"


def get_pokemon_sprite(pokemon, api_sprites):
    sprite_type = get_sprite_type(pokemon, api_sprites)
    return api_sprites[sprite_type]
