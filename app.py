# app.py
import streamlit as st
import time
from agents import create_player_agents, create_dm_agent
from campaignLore import hargrave_lore
from engine import roll_d20

# --- 1. Page Configuration ---
st.set_page_config(
    page_title="Hargrave AI Tabletop", 
    page_icon="🎲", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. Session State Initialization ---
if "initialized" not in st.session_state:
    with st.spinner("Waking up the Dungeon Master and gathering the party..."):
        st.session_state.dm = create_dm_agent()
        st.session_state.players = create_player_agents()
        st.session_state.log = []
        st.session_state.current_room = "A1_Iron_Gates"
        st.session_state.last_roll = None
        st.session_state.initialized = True

# --- 3. Sidebar: DM Screen & Party Status ---
with st.sidebar:
    st.title("🛡️ DM Command Center")
    
    # Party Status Dashboard
    st.subheader("👥 Party Status")
    cols = st.columns(2)
    cols[0].metric("Rogue HP", "24/24")
    cols[1].metric("Bard HP", "21/21")
    cols[0].metric("Cleric HP", "24/24")
    cols[1].metric("Druid HP", "21/21")
    
    st.divider()

    # Manual Dice Tray
   

    # Location Intel
    st.subheader("📍 Location Intel")
    room_id = st.session_state.current_room
    room_data = hargrave_lore['rooms'].get(room_id, {})
    st.write(f"**Room:** {room_id.replace('_', ' ')}")
    st.info(f"**Secret Notes:** {room_data.get('desc', 'Inky darkness.')}")
    
    if st.button("♻️ Reset Campaign", type="secondary", use_container_width=True):
        st.session_state.clear()
        st.rerun()

# --- 4. Main UI Rendering ---
st.title("🏰 The Haunting of House Hargrave")
st.markdown("#### *A Multi-Agent Autonomous RPG Engine*")
st.divider()

# Display the Adventure Log
if not st.session_state.log:
    st.info("The iron gates loom before you. Click 'Start Turn' to begin.")
else:
    for entry in st.session_state.log:
        with st.chat_message(entry["role"], avatar=entry["avatar"]):
            st.markdown(f"**{entry['name']}**")
            st.write(entry['content'])

# --- 5. Game Loop Controls ---
st.divider()
col_action, col_download = st.columns([1, 1])

if col_action.button("▶️ Start / Next Turn", type="primary", use_container_width=True):
    roll_context = ""
    if st.session_state.last_roll:
        roll_context = f"\n[SYSTEM: A manual d20 roll was made. Result: {st.session_state.last_roll}]"
        st.session_state.last_roll = None 

    # DM Resolution
    with st.spinner("The Dungeon Master is narrating..."):
        if not st.session_state.log:
            dm_input = "Start the campaign. The party is at the gates of House Hargrave."
        else:
            dm_input = f"Resolve the player actions. Current Room: {st.session_state.current_room}. {roll_context}"
        
        dm_response = st.session_state.dm.send_message(dm_input)
        st.session_state.log.append({
            "role": "assistant", 
            "name": "DUNGEON MASTER", 
            "avatar": "🐉", 
            "content": dm_response
        })

    # Player Reactions
    for key, agent in st.session_state.players.items():
        with st.spinner(f"{agent.name} is deciding..."):
            p_response = agent.send_message(f"The DM says: {dm_response}. What is your concise action?")
            st.session_state.log.append({
                "role": "user", 
                "name": key, 
                "avatar": "⚔️", 
                "content": p_response
            })
            time.sleep(0.1)
            
    st.rerun()

# --- 6. Export Functionality ---
if st.session_state.log:
    full_text = ""
    for entry in st.session_state.log:
        full_text += f"{entry['name']}: {entry['content']}\n\n"
    
    col_download.download_button(
        label="💾 Download Adventure Log",
        data=full_text,
        file_name="hargrave_adventure.txt",
        mime="text/plain",
        use_container_width=True
    )

# Fixed Anchor
st.markdown("<div id='end'></div>", unsafe_allow_html=True)
