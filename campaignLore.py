# campaign_lore.py

hargrave_lore = {
    "campaign_metadata": {
        "title": "The Haunting of House Hargrave",
        "level_range": "1-3",
        "primary_threat": "Psychological Horror / Necromancy",
        "world_state": "The island of Oakhaven is trapped in a temporal loop caused by Silas Hargrave’s failed ritual."
    },
    
    "global_mechanics": {
        "amnesia_curse": "Ghosts cannot perceive evidence of their own death. If they see their corpse, they see 'old rags' (DC 18 Investigation to break).",
        "environmental": "The Mist: Heavily Obscured. DC 12 CON save every hour or take 1 level of Exhaustion from the necrotic chill."
    },

    "rooms": {
        "A1_Iron_Gates": {
            "desc": "Rusted iron with weeping willow motifs. The crest is missing a small silver leaf.",
            "mechanics": {"athletics_dc": 12, "thieves_tools_dc": 15},
            "loot": None
        },
        "A2_The_Porch": {
            "desc": "Sagging floorboards. One specific board is a pressure plate.",
            "trap": {"name": "Board Snap", "detect_dc": 13, "save_dc": 12, "damage": "1d4 bludgeoning"}
        },
        "A3_Entrance_Hall": {
            "desc": "A grand foyer. A massive mirror sits on the east wall.",
            "mechanics": {"mirror_gimmick": "Reflects the room in 1842. No players are visible in the reflection."},
            "revelation_id": 1
        },
        "A4_Dining_Hall": {
            "desc": "A table set for 12. The food looks fresh but smells of wet earth.",
            "trap": {"name": "Grave Feast", "save": "WIS DC 14", "fail": "Poisoned for 1 hour"}
        },
        "A12_The_Kitchen": {
            "desc": "Meat hooks swing rhythmically. A cold iron stove sits in the corner.",
            "secret": {"detect_dc": 15, "find": "Hatch to the Cellar (C1)"}
        },
        "B2_Master_Suite": {
            "desc": "Dusty blue velvet hangings. A heavy oak wardrobe.",
            "combat": "Opening the wardrobe triggers the Animated Armor.",
            "loot": "Silas's Journal (Page 12)"
        },
        "C1_The_Cellar": {
            "desc": "Flooded with 2 inches of black water. Smells of ozone.",
            "combat_encounter": "3x Skeleton (Submerged)",
            "boss": "Elara Hargrave (Banshee/Ghost variant)"
        }
    },

    "revelations_track": {
        "1": "Mirrors do not show your reflection.",
        "2": "You realize your wounds don't bleed; they just puff gray smoke.",
        "3": "You find your own name on a 'Missing Persons' poster from 20 years ago.",
        "4": "The 'weeping' sound is actually your own voice echoing from the future."
    },

    "monsters": {
        "Animated Armor": {"ac": 18, "hp": 33, "str": 14, "attacks": [{"name": "Slam", "bonus": 4, "dmg": "1d6+2"}]},
        "Skeleton": {"ac": 13, "hp": 13, "dex": 14, "attacks": [{"name": "Shortsword", "bonus": 4, "dmg": "1d6+2"}]},
        "Elara_Ghost": {"ac": 11, "hp": 45, "wis": 12, "ability": "Horrifying Visage (DC 13 WIS save)"}
    }
}