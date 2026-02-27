# main.py
import time
from agents import dm_chat, rogue_chat, bard_chat, cleric_chat, druid_chat

print("Setting up the virtual table...")
print("--------------------------------------------------")

initial_prompt = """
Start the campaign. The party has just arrived at the rusted iron gates of the abandoned House Hargrave on a foggy night. 
Describe the eerie scene, set the spooky atmosphere, and ask the party what they want to do.
"""

print("DM is setting the scene...\n")
dm_response = dm_chat.send_message(initial_prompt)
print(f"🐉 DUNGEON MASTER:\n{dm_response.text}\n")
print("--------------------------------------------------\n")

rounds = 10

for i in range(rounds):
    print(f"=== ROUND {i+1} ===")
    print("Players are deciding their actions...\n")
    
    # Increased all sleep timers to 6 seconds to stay safely under the API rate limit!
    rogue_action = rogue_chat.send_message(f"The DM says: {dm_response.text}\nWhat does your character do?").text
    print(f"🗡️ ROGUE:\n{rogue_action}\n")
    time.sleep(6) 
    
    bard_action = bard_chat.send_message(f"The DM says: {dm_response.text}\nWhat does your character do?").text
    print(f"🪕 BARD:\n{bard_action}\n")
    time.sleep(6)
    
    cleric_action = cleric_chat.send_message(f"The DM says: {dm_response.text}\nWhat does your character do?").text
    print(f"🛡️ CLERIC:\n{cleric_action}\n")
    time.sleep(6)
    
    druid_action = druid_chat.send_message(f"The DM says: {dm_response.text}\nWhat does your character do?").text
    print(f"🌿 DRUID:\n{druid_action}\n")
    time.sleep(6)
    
    combined_actions = f"""
    The players have taken the following actions:
    Rogue: {rogue_action}
    Bard: {bard_action}
    Cleric: {cleric_action}
    Druid: {druid_action}
    
    Resolve these actions based on their character sheets, describe the outcome, drop a very subtle creepy clue, and ask what they do next.
    """
    
    print("DM is resolving the round...\n")
    dm_response = dm_chat.send_message(combined_actions)
    print(f"🐉 DUNGEON MASTER:\n{dm_response.text}\n")
    print("--------------------------------------------------\n")
    
    # Give the API a nice long 10-second break before starting the next round
    time.sleep(10)
    
print("Simulation paused. You can increase the 'rounds' variable in main.py to keep playing!")