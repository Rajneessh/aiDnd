# character_data.py

party_data = {
    "Rogue": {
        "name": "Half-Elf Rogue",
        "class": "Rogue 3 (Thief)",
        "background": "Archaeologist",
        "hp": 24, "ac": 14, "speed": 30,
        "stats": "STR 10 (+0), DEX 16 (+3), CON 14 (+2), INT 14 (+2), WIS 12 (+1), CHA 10 (+0)",
        "saving_throws": "DEX (+5), INT (+4)",
        "skills": "Acrobatics +5, Arcana +2, Deception +2, History +4, Investigation +6, Perception +3, Persuasion +2, Sleight of Hand +5, Stealth +5, Survival +3",
        "weapons": [
            "Shortsword: +5 to hit, 1d6+3 Piercing (Finesse, Light)",
            "Dagger: +5 to hit, 1d4+3 Piercing (Finesse, Thrown)"
        ],
        "features": [
            "Sneak Attack: 2d6 extra damage once per turn with advantage or ally nearby",
            "Cunning Action: Bonus Action to Dash, Disengage, or Hide",
            "Thief Archetype - Fast Hands: Bonus Action to pick locks, disarm traps, or Use Object",
            "Thief Archetype - Second-Story Work: Climbing costs no extra movement; running jump distance increases by +3 feet",
            "Expertise: Proficiency bonus doubled for two chosen proficiencies",
            "Thieves' Cant: Secret mix of dialect, jargon, and code",
            "Half-Elf - Darkvision: 60 ft.",
            "Half-Elf - Fey Ancestry: Advantage on saves against being charmed, magic can't put you to sleep",
            "Half-Elf - Skill Versatility: Proficiency in two skills"
        ],
        "equipment": "Leather armor, Thieves' Tools, Cartographer's Tools, Bullseye Lantern, Miner's Pick, Shovel, 50ft Hempen Rope, 10 Torches.",
        "personality": "I'm a pack rat who never throws anything away. I am always thirsty.",
        "ideal": "You believe no history should remain hidden.",
        "flaw": "You are uncomfortable in cramped places."
    },
    
    "Bard": {
        "name": "Elf Bard",
        "class": "Bard 3 (College of Glamour)",
        "background": "Entertainer",
        "hp": 21, "ac": 14, "speed": 30,
        "stats": "STR 13 (+1), DEX 17 (+3), CON 14 (+2), INT 11 (+0), WIS 8 (-1), CHA 14 (+2)",
        "saving_throws": "DEX (+5), CHA (+4)",
        "skills": "Acrobatics +5, Arcana +4, Athletics +2, Deception +3, History +1, Intimidation +3, Investigation +1, Nature +1, Perception +1, Performance +4, Persuasion +4, Religion +1, Sleight of Hand +4, Stealth +7",
        "weapons": [
            "Rapier: +5 to hit, 1d8+3 Piercing (Finesse)",
            "Dagger: +5 to hit, 1d4+3 Piercing (Finesse, Thrown)"
        ],
        "features": [
            "Bardic Inspiration: 2/Long Rest, 1d6 to ally's roll",
            "Jack of All Trades: +1 to non-proficient ability checks",
            "Song of Rest: +1d6 HP during short rests",
            "Expertise: Proficiency bonus doubled for chosen proficiencies",
            "College of Glamour - Mantle of Inspiration: Bonus Action, spend Inspiration to give 5 Temp HP and reaction movement to 2 allies",
            "College of Glamour - Enthralling Performance: Charm audience for 1 hour",
            "High Elf - Darkvision: 60 ft.",
            "High Elf - Keen Senses: Proficiency in Perception",
            "High Elf - Fey Ancestry: Advantage on saves against being charmed, magic can't put you to sleep",
            "High Elf - Trance: Meditate for 4 hours instead of sleeping for 8",
            "High Elf - Elf Weapon Training: Proficiency with longsword, shortsword, shortbow, longbow"
        ],
        "spells": "Cantrips: Vicious Mockery, Mage Hand, Prestidigitation. 1st Level: Identify, Healing Word, Tasha's Hideous Laughter, Earth Tremor. 2nd Level: Suggestion, Invisibility.",
        "equipment": "Leather armor, Lute, Flute, Disguise Kit, Costume Clothes, Map/Scroll Cases, Perfume.",
        "personality": "You don't believe in ghosts.",
        "ideal": "You believe new experiences are the only way to truly live.",
        "flaw": "You want to know what everyone else thinks about everything you do."
    },

    "Cleric": {
        "name": "Gnome Cleric",
        "class": "Cleric 3 (Peace Domain)",
        "background": "Courtier",
        "hp": 24, "ac": 15, "speed": 25,
        "stats": "STR 10 (+0), DEX 8 (-1), CON 15 (+2), INT 14 (+2), WIS 15 (+2), CHA 13 (+1)",
        "saving_throws": "WIS (+4), CHA (+3). Advantage on INT/WIS/CHA against magic.",
        "skills": "Animal Handling +2, Arcana +2, History +4, Insight +4, Medicine +2, Nature +2, Perception +2, Performance +3, Persuasion +3, Religion +2",
        "weapons": [
            "Mace: +2 to hit, 1d6 Bludgeoning",
            "Light Crossbow: +1 to hit, 1d8-1 Piercing (Range 80/220)"
        ],
        "features": [
            "Peace Domain - Implement of Peace: Proficiency in Insight, Performance, or Persuasion",
            "Peace Domain - Emboldening Bond: Action, 2 allies get +1d4 to attack/save/check once per turn for 10 mins",
            "Channel Divinity: 1/Short Rest",
            "Channel Divinity - Turn Undead: Action to turn undead creatures",
            "Channel Divinity - Balm of Peace: Move without provoking attacks, heal allies passed for 2d6+2 HP",
            "Rock Gnome - Darkvision: 60 ft.",
            "Rock Gnome - Gnome Cunning: Advantage on all Intelligence, Wisdom, and Charisma saving throws against magic",
            "Rock Gnome - Artificer's Lore: Add twice your proficiency bonus to History checks related to magic items, alchemical objects, or technological devices",
            "Rock Gnome - Tinker: Construct tiny clockwork devices"
        ],
        "spells": "Cantrips: Spare the Dying, Sacred Flame, Mending. 1st Level: Command, Guiding Bolt, Cure Wounds, Inflict Wounds, Heroism, Sanctuary, Bane, Bless. 2nd Level: Aid, Warding Bond, Locate Object, Blindness/Deafness, Calm Emotions.",
        "equipment": "Scale Mail, Shield, Amulet (Holy Symbol), Tinker's Tools, Fine Clothes, 50ft Hempen Rope.",
        "personality": "You view everything through the lens of storytelling, even sometimes narrating aloud your and others' experiences.",
        "ideal": "You believe one must experience the world in order to write about it.",
        "flaw": "You exaggerate everything."
    },

    "Druid": {
        "name": "Elf Druid",
        "class": "Druid 3 (Circle of the Land - Mountain)",
        "background": "Hermit",
        "hp": 21, "ac": 14, "speed": 35,
        "stats": "STR 14 (+2), DEX 12 (+1), CON 14 (+2), INT 13 (+1), WIS 16 (+3), CHA 8 (-1)",
        "saving_throws": "INT (+3), WIS (+5)",
        "skills": "Animal Handling +3, Arcana +3, Insight +5, Medicine +5, Perception +5, Religion +3, Survival +5",
        "weapons": [
            "Scimitar: +4 to hit, 1d6+2 Slashing (Finesse, Light)",
            "Thorn Whip: +5 to hit, 1d6 Piercing (Pull 10ft)"
        ],
        "features": [
            "Druidic: Secret language of druids",
            "Wild Shape: 2/Short Rest, Max CR 1/4, No flying/swimming",
            "Natural Recovery: Once per long rest during a short rest, choose expended spell slots to recover",
            "Circle Spells: Access to circle spells for associated land",
            "Wood Elf - Darkvision: 60 ft.",
            "Wood Elf - Keen Senses: Proficiency in Perception",
            "Wood Elf - Fey Ancestry: Advantage against charmed, immune to magical sleep",
            "Wood Elf - Trance: Meditate for 4 hours a day",
            "Wood Elf - Elf Weapon Training: Proficiency with longsword, shortsword, shortbow, and longbow",
            "Wood Elf - Fleet of Foot: Base walking speed increases to 35 feet",
            "Wood Elf - Mask of the Wild: Attempt to hide even when only lightly obscured"
        ],
        "spells": "Cantrips: Mending, Thorn Whip, Druidcraft. 1st Level: Cure Wounds, Entangle, Faerie Fire, Thunderwave, Healing Word, Animal Friendship. 2nd Level: Spider Climb, Spike Growth, Flaming Sphere.",
        "equipment": "Leather Armor, Shield, Herbalism Kit, Sprig of Mistletoe, 50ft Hempen Rope.",
        "personality": "You stop and smell the roses, both literally and figuratively.",
        "ideal": "You believe the life of plants is as precious as the life of anything else.",
        "flaw": "You tend to touch things you probably shouldn't."
    }
}