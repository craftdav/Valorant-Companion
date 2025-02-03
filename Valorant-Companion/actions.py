def setup_agent_action(ui, showLineups):
    """
    Beállítja az agent line-up gombok eseményeit.
    """
    agents=["Astra","Breach","Brimstone","Chamber","clove","Cypher","Deadlock","Fade","Gekko","Harbor","Iso","Jett","Kayo","Killjoy","Neon","Omen","Phoenix","Raze","Reyna","Sage","Skye","Sova","Tejo","Viper","Vyse","Yoru"]
    maps = {
        "Abyss": ["A", "Mid", "B"],
        "Ascent": ["A", "Mid", "B"],
        "Bind": ["A", "B"],
        "Breeze": ["A", "Mid", "B"],
        "Fracture": ["A", "Mid", "B"],
        "Haven": ["A", "B", "C"],
        "Icebox": ["A", "Mid", "B"],
        "Lotus": ["A", "B", "C"],
        "Pearl": ["A", "Mid", "B"],
        "Split": ["A", "Mid", "B"],
        "Sunset": ["A", "Mid", "B"],
    }
    for agent in agents:
        for map_name, sites in maps.items():
            for site in sites:
                action_name = f"action{agent}{map_name}{site}"
                if hasattr(ui, action_name):
                    getattr(ui, action_name).triggered.connect(lambda _,a=agent, m=map_name, s=site: showLineups(a, m, s))

