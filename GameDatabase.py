#GameDatabase.py

# Each class will have a list of skills and spells that unlock at each level up to level 10.

game_database_python_extended = {
    "classes": {
        "Warrior": {
            "base_hp": 30,
            "base_attack": 5,
            "base_defense": 5,
            "level_up_skills": {
                "1": ["Charge", "Defend"],
                "2": ["Whirlwind"],
                "3": ["Cleave"],
                "4": ["Berserk"],
                "5": ["Armor Up"],
                "6": ["War Cry"],
                "7": ["Execute"],
                "8": ["Earthquake"],
                "9": ["Crushing Blow"],
                "10": ["Bladestorm"]
            }
        },
        "Mage": {
            "base_hp": 20,
            "base_attack": 7,
            "base_defense": 3,
            "level_up_skills": {
                "1": ["Fireball", "Teleport"],
                "2": ["Frostbolt"],
                "3": ["Arcane Blast"],
                "4": ["Lightning Bolt"],
                "5": ["Meteor"],
                "6": ["Polymorph"],
                "7": ["Arcane Explosion"],
                "8": ["Chain Lightning"],
                "9": ["Mana Shield"],
                "10": ["Pyroblast"]
            }
        },
        "Rogue": {
            "base_hp": 25,
            "base_attack": 6,
            "base_defense": 4,
            "skills": {
                1: ["Stealth", "Backstab"],
                2: ["Pick Lock"],
                3: ["Eviscerate"],
                4: ["Vanish"],
                5: ["Poison"],
                6: ["Cheap Shot"],
                7: ["Shadowstep"],
                8: ["Slice and Dice"],
                9: ["Fan of Knives"],
                10: ["Assassinate"]
            }
        },
        "Paladin": {
            "base_hp": 35,
            "base_attack": 4,
            "base_defense": 6,
            "skills": {
                1: ["Heal", "Smite"],
                2: ["Divine Shield"],
                3: ["Seal of Righteousness"],
                4: ["Judgment"],
                5: ["Lay on Hands"],
                6: ["Hammer of Justice"],
                7: ["Consecration"],
                8: ["Redemption"],
                9: ["Divine Storm"],
                10: ["Avenging Wrath"]
            }
        },
        "Ranger": {
            "base_hp": 28,
            "base_attack": 6,
            "base_defense": 4,
            "skills": {
                1: ["Bow Shot", "Find Path"],
                2: ["Trap Setting"],
                3: ["Animal Companion"],
                4: ["Eagle Eye"],
                5: ["Snipe"],
                6: ["Cover Fire"],
                7: ["Forest Stealth"],
                8: ["Volley"],
                9: ["Mark Target"],
                10: ["Deadly Aim"]
            }
        },
        "Cleric": {
            "base_hp": 30,
            "base_attack": 4,
            "base_defense": 5,
            "skills": {
                1: ["Heal", "Bless"],
                2: ["Prayer"],
                3: ["Smite Evil"],
                4: ["Sanctuary"],
                5: ["Divine Intervention"],
                6: ["Purge"],
                7: ["Holy Light"],
                8: ["Resurrect"],
                9: ["Angelic Shield"],
                10: ["Judgement"]
            }
        },
        "Monk": {
            "base_hp": 25,
            "base_attack": 6,
            "base_defense": 5,
            "skills": {
                1: ["Meditate", "Punch"],
                2: ["Quick Reflexes"],
                3: ["Dragon Kick"],
                4: ["Inner Peace"],
                5: ["Wind Walk"],
                6: ["Ki Strike"],
                7: ["Zen Focus"],
                8: ["Flurry of Blows"],
                9: ["Serenity"],
                10: ["Enlightenment"]
            }
        },
        "Bard": {
            "base_hp": 24,
            "base_attack": 5,
            "base_defense": 4,
            "skills": {
                1: ["Sing", "Inspire"],
                2: ["Lute Smash"],
                3: ["Ballad of Heroes"],
                4: ["Soothing Melody"],
                5: ["Distract"],
                6: ["Charm"],
                7: ["Harmony"],
                8: ["Crescendo"],
                9: ["Lullaby"],
                10: ["Masterpiece"]
            }
        }
    }
}


skill_descriptions = {
    "Charge": "Rush towards an enemy, dealing extra damage on the next attack.",
    "Defend": "Increase your defense, reducing damage from the next attack against you.",
    "Fireball": "Cast a fireball that deals AoE (Area of Effect) damage.",
    "Teleport": "Instantly move to a different location within a short distance.",
    "Stealth": "Become invisible to enemies, making it easier to avoid combat or land the first strike.",
    "Backstab": "Perform a sneak attack that deals critical damage.",
    "Heal": "Restore a portion of HP to yourself or an ally.",
    "Smite": "Channel divine energy to deal extra damage on your next attack.",
    "Bow Shot": "Shoot an arrow from a distance, dealing damage to a single enemy.",
    "Find Path": "Discover hidden paths or shortcuts, reducing the time spent on travel.",
    "Bless": "Bless an ally, granting them a temporary boost to their abilities.",
    "Meditate": "Enter a state of deep focus, restoring some HP and Mana.",
    "Punch": "A quick and basic melee attack.",
    "Sing": "Perform a song that grants temporary bonuses to your party.",
    "Inspire": "Motivate your allies, granting them a temporary boost in combat effectiveness.",
    "Shield Bash": "Use your shield to bash an enemy, causing a stun effect.",
    "Whirlwind": "Perform a spinning attack that hits multiple enemies around you.",
    "Counter": "Prepare to counter the next attack against you, dealing damage back to the attacker.",
    "Arcane Blast": "Release a burst of arcane energy, damaging enemies in a radius.",
    "Elemental Shield": "Summon a shield of elemental energy, reducing incoming elemental damage.",
    "Shadow Strike": "Strike from the shadows, dealing extra damage and applying a bleed effect.",
    "Evasion": "Dodge the next attack against you, avoiding its damage.",
    "Holy Light": "Summon a beam of holy light, healing allies and damaging undead enemies.",
    "Divine Protection": "Grant an ally a shield that absorbs a certain amount of damage.",
    "Snipe": "Take careful aim, dealing extra damage on your next bow shot.",
    "Animal Companion": "Summon an animal companion to assist you in combat.",
    "Prayer": "Say a prayer, granting a temporary buff to all party members.",
    "Curse": "Curse an enemy, reducing their combat effectiveness for a short time.",
    "Focus": "Enter a focused state, increasing your next attack's damage.",
    "Flurry": "Perform a series of quick punches, dealing damage to a single enemy.",
    "Harmony": "Play a harmonious tune, removing negative status effects from your party.",
    "Dissonance": "Play a dissonant tune, causing confusion among enemy ranks.",
    "Fortify": "Strengthen your armor, reducing incoming physical damage.",
    "Cleave": "Swing your weapon in a wide arc, hitting multiple enemies.",
    "Mana Burn": "Burn an enemy's mana, dealing damage equal to the amount burned.",
    "Blink": "Teleport a short distance, even through walls.",
    "Ambush": "Set up an ambush, gaining the initiative in the next combat.",
    "Assassinate": "Attempt to kill an enemy in one shot. Higher success rate on weaker enemies.",
    "Lay Hands": "Lay your hands on an ally, fully restoring their HP.",
    "Judgment": "Pass divine judgment on an enemy, dealing heavy damage.",
    "Precise Shot": "Your next bow shot has increased accuracy and damage.",
    "Camouflage": "Blend into your surroundings, becoming nearly invisible.",
    "Resurrect": "Bring an ally back to life with a portion of their HP.",
    "Ward": "Place a magical ward on an ally, granting resistance to magical attacks.",
    "Zen": "Enter a Zen state, regaining full HP and Mana.",
    "Triple Punch": "Perform a triple punch combo, dealing heavy damage.",
    "Ballad": "Play a ballad that heals your party over time.",
    "Serenade": "Perform a serenade, charming an enemy to fight for you temporarily.",
    "Lacerate": "Cause a deep wound on the enemy, causing them to bleed over time.",
    "Guardian Angel": "Summon a guardian angel that protects an ally from the next fatal attack.",
    "Thunder Strike": "Call down a bolt of lightning, dealing heavy damage to a single enemy.",
    "Summon Elemental": "Summon an elemental to fight for you.",
    "Shadowstep": "Step through the shadows to appear behind an enemy.",
    "Siphon Life": "Steal life from an enemy, healing yourself.",
    "Holy Nova": "Emit a burst of holy light, healing allies and damaging enemies.",
    "Consecrate": "Consecrate the ground, causing damage to enemies who step on it.",
    "Quick Shot": "Shoot an arrow quickly, reducing the time before your next action.",
    "Track": "Track an enemy, revealing their location.",
    "Divine Favor": "Gain the favor of the gods, increasing the effectiveness of your next spell.",
    "Doom": "Curse an enemy with impending doom, causing a delayed burst of damage.",
    "Inner Peace": "Find inner peace, rapidly regenerating HP and Mana for a short time.",
    "Roundhouse Kick": "Perform a roundhouse kick, hitting multiple enemies.",
    "Requiem": "Play a haunting melody, putting enemies to sleep.",
    "Charm": "Charm an enemy, making them fight for you for a short time."
    "Blinding Light": "Emit a flash of light, blinding enemies and reducing their accuracy.",
    "Summon Familiar": "Summon a small creature to assist you in various ways.",
    "Spectral Blade": "Conjure a blade of spectral energy, bypassing enemy armor.",
    "Trap": "Set a trap that will immobilize the first enemy to walk over it.",
    "Vanish": "Disappear from sight, avoiding all attacks for a short time.",
    "Divine Wrath": "Unleash the wrath of the gods, dealing massive damage to multiple enemies.",
    "Long Shot": "Take a long-distance shot with your bow, dealing damage based on distance.",
    "Aura of Healing": "Create an aura that continuously heals nearby allies.",
    "Banish": "Send an enemy to another plane of existence for a short time, removing them from battle.",
    "Serenity": "Enter a state of complete serenity, making you immune to all negative effects.",
    "Quadruple Punch": "Unleash a flurry of four punches in quick succession.",
    "Aria": "Perform an aria that grants long-lasting buffs to your team.",
    "Duet": "Perform a duet with another Bard, combining the effects of both songs.",
    "Stone Skin": "Transform your skin into stone, massively boosting your defense for a short time.",
    "Blade Dance": "Engage in a deadly dance, striking all enemies around you multiple times.",
    "Nether Portal": "Open a portal to the nether realm, summoning demons to aid you.",
    "Phase": "Phase out of reality, avoiding all damage for a short time.",
    "Invisibility": "Become invisible, allowing you to bypass enemies or get the jump on them.",
    "Life Link": "Link your life force with an ally, sharing damage and healing.",
    "Reflect": "Create a magical barrier that reflects spells back at the caster.",
    "Zen Mastery": "Achieve the pinnacle of Zen mastery, making all your skills more potent.",
    "Fist of the Heavens": "Summon a giant fist from the heavens to smash your enemies.",
    "Epic Ballad": "Perform an epic ballad that grants a powerful buff to all party members.",
    "Soul Swap": "Swap positions with an ally or enemy, taking on their status effects as well."
    "Time Warp": "Manipulate time to take an extra turn.",
    "Summon Undead": "Summon an undead minion to aid you in battle.",
    "Gale Force": "Summon a powerful wind that pushes enemies back and disrupts their actions.",
    "Divine Intervention": "Call upon divine powers to save you or an ally from a fatal blow.",
    "Mirror Image": "Create duplicates of yourself to confuse enemies.",
    "Vampiric Touch": "Steal health from an enemy to heal yourself.",
    "Mana Shield": "Use your Mana to absorb incoming damage."
}
