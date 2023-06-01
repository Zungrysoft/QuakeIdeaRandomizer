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
        r = r.replace("[theme]", weighted_choice(themes))
        r = r.replace("[shape]", weighted_choice(shapes))
        r = r.replace("[special]", weighted_choice(special_requirements))

        # Entity count content has some special rules
        entity_data = weighted_choice(entities)
        r = r.replace("[entity]", entity_data["classname"])
        r = r.replace("[entity_count]", str(entity_data["count"]))
        r = r.replace("[entity_plural]", "" if entity_data["count"] == 1 else "s")

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
        "value": "Your map must contain at least [entity_count] instance[entity_plural] of [entity] on all difficulties.",
        "weight": 200,
    },
    {
        "value": "Your map must be [theme] themed.",
        "weight": 30,
    },
    {
        "value": "Your map's geometry must have many [shape] elements.",
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
        "value": "Your map must have some sort of puzzle in it.",
        "weight": 100,
    },
    {
        "value": "Your map must have at least 3 pools of lava.",
        "weight": 100,
    },
    {
        "value": "Your map's exit must be near the start point.",
        "weight": 100,
    },
    {
        "value": "Your map may only have two monster types.",
        "weight": 100,
    },
    {
        "value": "Your map must involve the player climbing up the map a distance of 1500 units or more.",
        "weight": 100,
    },
    {
        "value": "Your map must have some platforming in it.",
        "weight": 100,
    },
    {
        "value": "Your map must be shaped like something when viewed from above or from a certain angle. (Like e3m2 from Doom.)",
        "weight": 100,
    },
    {
        "value": "Your map must use switchable lights somehow.",
        "weight": 300,
    },
    {
        "value": "Your map must be playable in both Singleplayer and Deathmatch.",
        "weight": 100,
    },
    {
        "value": "The playable area of your map must fit within a 768x768 horizontal area. It can be as tall as you wish.",
        "weight": 100,
    },
    {
        "value": "Your map must use at least one custom texture you created.",
        "weight": 100,
    },
    {
        "value": "Your map must have some sort of time-sensitive element in it.",
        "weight": 100,
    },
    {
        "value": "Your map must have non-linear progression.",
        "weight": 100,
    },
    {
        "value": "Your map must have func_doors in it that can crush players and/or monsters.",
        "weight": 100,
    },
]

entities = [
    # Monsters
    {
        "value": {
            "classname": "monster_tarbaby",
            "count": 6,
        },
        "weight": 30,
    },
    {
        "value": {
            "classname": "monster_shambler",
            "count": 3,
        },
        "weight": 100,
    },
    {
        "value": {
            "classname": "monster_shalrath",
            "count": 4,
        },
        "weight": 100,
    },
    {
        "value": {
            "classname": "monster_ogre",
            "count": 10,
        },
        "weight": 100,
    },
    {
        "value": {
            "classname": "monster_fish",
            "count": 8,
        },
        "weight": 100,
    },
    # {
    #     "value": {
    #         "classname": "monster_dog",
    #         "count": 12,
    #     },
    #     "weight": 100,
    # },
    {
        "value": {
            "classname": "monster_enforcer",
            "count": 12,
        },
        "weight": 100,
    },
    {
        "value": {
            "classname": "monster_demon1",
            "count": 7,
        },
        "weight": 100,
    },
    {
        "value": {
            "classname": "monster_wizard",
            "count": 10,
        },
        "weight": 100,
    },
    {
        "value": {
            "classname": "monster_zombie",
            "count": 15,
        },
        "weight": 100,
    },

    # Brushes
    {
        "value": {
            "classname": "trigger_push",
            "count": 7,
        },
        "weight": 140,
    },
    {
        "value": {
            "classname": "trigger_teleport",
            "count": 7,
        },
        "weight": 140,
    },
    {
        "value": {
            "classname": "trigger_monsterjump",
            "count": 6,
        },
        "weight": 140,
    },
    {
        "value": {
            "classname": "trigger_secret",
            "count": 12,
        },
        "weight": 90,
    },
    {
        "value": {
            "classname": "func_button",
            "count": 12,
        },
        "weight": 140,
    },
    {
        "value": {
            "classname": "func_train",
            "count": 5,
        },
        "weight": 140,
    },
    {
        "value": {
            "classname": "func_plat",
            "count": 8,
        },
        "weight": 140,
    },

    # Misc
    {
        "value": {
            "classname": "trigger_counter",
            "count": 4,
        },
        "weight": 90,
    },
    {
        "value": {
            "classname": "misc_fireball",
            "count": 8,
        },
        "weight": 90,
    },
    {
        "value": {
            "classname": "misc_explobox/misc_explobox2",
            "count": 8,
        },
        "weight": 90,
    },
    {
        "value": {
            "classname": "trap_shooter/trap_spikeshooter",
            "count": 10,
        },
        "weight": 90,
    },

    # Items
    {
        "value": {
            "classname": "item_armorInv",
            "count": 3,
        },
        "weight": 40,
    },
    {
        "value": {
            "classname": "item_artifact_super_damage",
            "count": 2,
        },
        "weight": 40,
    },
    {
        "value": {
            "classname": "item_artifact_invulnerability",
            "count": 2,
        },
        "weight": 40,
    },
    {
        "value": {
            "classname": "item_artifact_invisibility",
            "count": 2,
        },
        "weight": 40,
    },
    {
        "value": {
            "classname": "item_artifact_envirosuit",
            "count": 3,
        },
        "weight": 40,
    },

    # Weapons
    {
        "value": {
            "classname": "weapon_rocketlauncher",
            "count": 1,
        },
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
        "weight": 50,
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