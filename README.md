# 🏰 Project Hargrave: Autonomous Multi-Agent RPG Engine

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B.svg)](https://streamlit.io/)
[![LLM](https://img.shields.io/badge/LLM-Llama--3.3%20%7C%20Gemini%20%7C%20DeepSeek-orange.svg)](https://groq.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An advanced **Autonomous Multi-Agent System (MAS)** that orchestrates five distinct Large Language Models to play a persistent, rule-bound session of Dungeons & Dragons.

## 🚀 The Development Journey

This project evolved from a simple API wrapper into a full-stack, stateful AI engine.

1.  **Phase 1: PDF Data Modeling**
    - Transformed unstructured D&D Beyond character sheets and a 30-page campaign module (_The Haunting of House Hargrave_) into a structured Pythonic schema.
    - Mapped Difficulty Classes (DCs), room IDs, and monster stat blocks into a queryable dictionary.

2.  **Phase 2: Agentic Orchestration**
    - Engineered five specialized agents using **System Prompting**.
    - Implemented a "Game Loop" where the Dungeon Master agent evaluates player actions against the campaign's hidden data.

3.  **Phase 3: Hybrid Deterministic Engine**
    - Integrated a custom Python dice engine (`engine.py`) to move the system from "creative hallucination" to "rule-based logic."
    - Separated narrative generation (LLM) from mathematical resolution (Python).

4.  **Phase 4: Stateful Web Deployment**
    - Developed a real-time dashboard using **Streamlit**.
    - Managed persistent chat memory and session state across multiple LLM calls.

## 🧠 System Architecture

Project Hargrave utilizes a **Hub-and-Spoke Agent Model**:

- **The Dungeon Master (The Hub):** Injected with the full "Source of Truth" (Campaign Lore). It manages the world state and narrative progression.
- **The Players (The Spokes):** Four distinct agents with "Partial Knowledge." They only know their own character sheets and the DM's descriptions.
- **The Logic Layer:** A deterministic Python module that handles d20 rolls, damage calculations, and skill-check validation.

## 🛠️ Tech Stack

- **Language:** Python 3.12
- **AI Orchestration:** Groq / DeepSeek / Gemini (OpenAI-compatible SDK)
- **Frontend:** Streamlit
- **Data Modeling:** JSON / Dictionary-based RAG-lite
- **Environment:** Virtualenv, Dotenv for secret management

## 🕹️ Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Rajneessh/aiDnd.git](https://github.com/Rajneessh/aiDnd.git)
   cd aiDnd
   ```
