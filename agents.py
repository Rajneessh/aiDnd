import os
from dotenv import load_dotenv
from openai import OpenAI
from characterData import party_data
from campaignLore import hargrave_lore

load_dotenv()

# Using Groq/DeepSeek (OpenAI-compatible) for speed and higher rate limits
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"), 
    base_url="https://api.groq.com/openai/v1"
)
MODEL_NAME = "llama-3.3-70b-versatile"

class DndAgent:
    def __init__(self, name, system_instruction):
        self.name = name
        self.history = [{"role": "system", "content": system_instruction}]

    def send_message(self, prompt):
        self.history.append({"role": "user", "content": prompt})
        
        completion = client.chat.completions.create(
            model=MODEL_NAME,
            messages=self.history,
            temperature=0.7 # Balanced for roleplay and logic
        )
        
        response_text = completion.choices[0].message.content
        self.history.append({"role": "assistant", "content": response_text})
        return response_text

def create_player_agents():
    agents = {}
    for key, data in party_data.items():
        instruction = f"""You are {data['name']}, a {data['class']}.
        STATS: {data['stats']} | SKILLS: {data['skills']}
        FEATURES: {data['features']} | HP: {data['hp']}
        PERSONALITY: {data['personality']} | FLAW: {data['flaw']}
        
        RULES: 
        1. Stay in character. 2. Be concise. 3. Describe ACTIONS, not rolls.
        4. You are exploring House Hargrave. You feel a strange sense of deja vu."""
        
        agents[key] = DndAgent(data['name'], instruction)
    return agents

def create_dm_agent():
    instruction = f"""You are the Dungeon Master for {hargrave_lore['campaign_metadata']['title']}.
    WORLD LOGIC: {hargrave_lore['global_mechanics']}
    FULL ROOM DATA: {hargrave_lore['rooms']}
    REVELATIONS: {hargrave_lore['revelations_track']}
    
    GOAL: Lead the 4 AI players through the house. 
    1. Reference the DC checks in the room data.
    2. Drop subtle hints about the 'Ghost' twist.
    3. Keep descriptions high-horror and atmospheric."""
    
    return DndAgent("Dungeon Master", instruction)