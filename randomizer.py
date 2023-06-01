import random

REQUIREMENT_COUNT = 3

def main():
    print("=========================")
    print("SM225 Map Idea Generator:")
    print("=========================")
    print()

    for _ in range(REQUIREMENT_COUNT):
        # Pick which requirement
        r = weighted_choice(requirements)

        # Pick content for requirements
        r = r.replace("[theme]", weighted_choice(themes))

        # Entity count content has some special rules
        entity_data = weighted_choice(entities)
        r = r.replace("[entity]", entity_data["classname"])
        r = r.replace("[entity_count]", str(entity_data["count"]))
        r = r.replace("[entity_plural]", "" if entity_data["count"] == 1 else "s")

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
    
    # This base shouldn't be needed, but is here just in case
    return list[0]["value"]

requirements = [
    {
        "value": "Your map must contain at least [entity_count] instance[entity_plural] of [entity] on all difficulties.",
        "weight": 100,
    },
    {
        "value": "Your map's theme must be [theme].",
        "weight": 100,
    },
    {
        "value": "Your map's geometry should have many [shape] elements.",
        "weight": 60,
    },
]

entities = [
    {
        "value": {
            "classname": "monster_ogre",
            "count": 10,
        },
        "weight": 100,
    },
    {
        "value": {
            "classname": "weapon_rocketlauncher",
            "count": 1,
        },
        "weight": 100,
    },
]

themes = [
    {
        "value": "Techbase",
        "weight": 100,
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
        "value": "pentagon-shaped",
        "weight": 15,
    },
]

main()