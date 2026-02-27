# engine.py
import random
import re

def roll_d20(modifier=0):
    """Rolls a d20 and returns the raw roll and the total."""
    roll = random.randint(1, 20)
    return roll, roll + modifier

def parse_damage(damage_str):
    """Parses strings like '1d6+2' and returns the result."""
    try:
        # Using regex to find the numbers
        match = re.match(r"(\d+)d(\d+)(?:\+(\d+))?", damage_str)
        if not match: return 0
        num_dice, sides, bonus = match.groups()
        total = sum(random.randint(1, int(sides)) for _ in range(int(num_dice)))
        if bonus: total += int(bonus)
        return total
    except:
        return 0