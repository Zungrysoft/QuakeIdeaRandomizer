import random

REQUIREMENT_COUNT = 3

def main():
    print("=========================")
    print("SM225 Map Idea Generator:")
    print("=========================")
    print()

    requirements_finished = []
    while len(requirements_finished) < REQUIREMENT_COUNT:
        # Pick which requirement
        r = weighted_choice(requirements)

        # Pick content for requirements
        r = r.replace("[entity]", weighted_choice(entities))
        r = r.replace("[theme]", weighted_choice(themes))
        r = r.replace("[shape]", weighted_choice(shapes))
        r = r.replace("[special]", weighted_choice(special_requirements))

        # Make sure this requirement hasn't been done before
        if not r in requirements_finished:
            requirements_finished.append(r)
            print(r)

def weighted_choice(list):
    # Figure out the total weight of the list
    total_weight = 0
    for elem in list:
        total_weight += elem["weight"]

    # Select one at random
    rand = random.random() * total_weight
    for elem in list:
        rand -= elem["weight"]
        if rand < 0:
            return elem.get("value")

    # This base case shouldn't be needed, but is here just in case
    return list[0]["value"]

requirements = [
    {
        "value": "Your map should make ample use of the [entity] entity.",
        "weight": 200,
    },
    {
        "value": "Your map should be [theme] themed.",
        "weight": 20,
    },
    {
        "value": "Your map's geometry should have many [shape] elements.",
        "weight": 30,
    },
    {
        "value": "[special]",
        "weight": 100,
    },
]

special_requirements = [
    {
        "value": "Your map may not have any item_health entities.",
        "weight": 100,
    },
    {
        "value": "Your map should have some sort of puzzle in it.",
        "weight": 100,
    },
    {
        "value": "Your map must have at least 3 pools of lava.",
        "weight": 20,
    },
    {
        "value": "Your map's exit should be near the start point.",
        "weight": 100,
    },
    {
        "value": "Your map may only have two monster types.",
        "weight": 100,
    },
    {
        "value": "Your map should involve the player climbing up the map a distance of 1500 units or more.",
        "weight": 100,
    },
    {
        "value": "Your map should have some platforming in it.",
        "weight": 100,
    },
    {
        "value": "Your map should be shaped like something when viewed from above or from a certain angle. (Like e3m2 from Doom.)",
        "weight": 100,
    },
    {
        "value": "Your map must use switchable lights somehow.",
        "weight": 300,
    },
    {
        "value": "Your map should be playable in both Singleplayer and Deathmatch.",
        "weight": 100,
    },
    {
        "value": "The playable area of your map must fit within a 768x768 horizontal area. It can be as tall as you wish.",
        "weight": 100,
    },
    {
        "value": "Your map must use at least one custom texture you created.",
        "weight": 70,
    },
    {
        "value": "Your map should have some sort of time-sensitive element in it.",
        "weight": 100,
    },
    {
        "value": "Your map should have non-linear progression.",
        "weight": 140,
    },
    {
        "value": "Your map should have func_doors in it that can crush players and/or monsters.",
        "weight": 100,
    },
    {
        "value": "Your map may not have any weapons aside from weapon_grenadelauncher and weapon_rocketlauncher",
        "weight": 40,
    },
    {
        "value": "Tell a story with your map's environment design.",
        "weight": 30,
    },
    {
        "value": "Your map may have no more than 30 monsters in it.",
        "weight": 13,
    },
]

entities = [
    # Monsters
    {
        "value": "monster_tarbaby",
        "weight": 30,
    },
    {
        "value": "monster_shambler",
        "weight": 100,
    },
    {
        "value": "monster_shalrath",
        "weight": 100,
    },
    {
        "value": "monster_ogre",
        "weight": 100,
    },
    {
        "value": "monster_fish",
        "weight": 100,
    },
    {
        "value": "monster_enforcer",
        "weight": 100,
    },
    {
        "value": "monster_demon1",
        "weight": 100,
    },
    {
        "value": "monster_wizard",
        "weight": 100,
    },
    {
        "value": "monster_zombie",
        "weight": 100,
    },

    # Brushes
    {
        "value": "trigger_push",
        "weight": 140,
    },
    {
        "value": "trigger_teleport",
        "weight": 140,
    },
    {
        "value": "trigger_monsterjump",
        "weight": 140,
    },
    {
        "value": "trigger_secret",
        "weight": 90,
    },
    {
        "value": "func_button",
        "weight": 140,
    },
    {
        "value": "func_train",
        "weight": 140,
    },
    {
        "value": "func_plat",
        "weight": 140,
    },

    # Misc
    {
        "value": "trigger_counter",
        "weight": 90,
    },
    {
        "value": "misc_fireball",
        "weight": 90,
    },
    {
        "value": "misc_explobox/misc_explobox2",
        "weight": 90,
    },
    {
        "value": "trap_shooter/trap_spikeshooter",
        "weight": 90,
    },

    # Items
    {
        "value": "item_armorInv",
        "weight": 40,
    },
    {
        "value": "item_artifact_super_damage",
        "weight": 40,
    },
    {
        "value": "item_artifact_invulnerability",
        "weight": 40,
    },
    {
        "value": "item_artifact_invisibility",
        "weight": 40,
    },
    {
        "value": "item_artifact_envirosuit",
        "weight": 40,
    },

    # Weapons
    {
        "value": "weapon_rocketlauncher",
        "weight": 200,
    },
    {
        "value": "weapon_grenadelauncher",
        "weight": 200,
    },
]

themes = [
    {
        "value": "Techbase",
        "weight": 100,
    },
    {
        "value": "Medieval",
        "weight": 100,
    },
    {
        "value": "Runic",
        "weight": 100,
    },
    {
        "value": "Egyptian",
        "weight": 20,
    },
    {
        "value": "City",
        "weight": 20,
    },
    {
        "value": "Void",
        "weight": 20,
    },
    {
        "value": "Knave",
        "weight": 10,
    },
    {
        "value": "Insomnia",
        "weight": 10,
    },
    {
        "value": "Koohoo",
        "weight": 10,
    },
    {
        "value": "Rubicon",
        "weight": 10,
    },
    {
        "value": "Honey",
        "weight": 10,
    },
]

shapes = [
    {
        "value": "circular",
        "weight": 100,
    },
    {
        "value": "triangular",
        "weight": 100,
    },
    {
        "value": "spherical",
        "weight": 40,
    },
    {
        "value": "cube-shaped",
        "weight": 10,
    },
    {
        "value": "polyhedral",
        "weight": 60,
    },
    {
        "value": "pentagon-shaped",
        "weight": 15,
    },
    {
        "value": "hexagon-shaped",
        "weight": 6,
    },
]

main()