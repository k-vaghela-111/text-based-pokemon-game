<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Text-Based Pokémon Battle Game</title>
  <style>
    body {
      font-family: 'Segoe UI', sans-serif;
      background: linear-gradient(to right, #fceabb, #f8b500);
      color: #333;
      margin: 0;
      padding: 2rem;
    }
    h1, h2 {
      color: #d62828;
      text-shadow: 1px 1px #fff;
    }
    .section {
      background: #fff;
      border-radius: 10px;
      padding: 1.5rem;
      margin-bottom: 2rem;
      box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    code {
      background: #eee;
      padding: 0.2rem 0.4rem;
      border-radius: 4px;
      font-family: monospace;
    }
    pre {
      background: #f4f4f4;
      padding: 1rem;
      border-radius: 8px;
      overflow-x: auto;
    }
    .footer {
      text-align: center;
      font-size: 0.9rem;
      color: #555;
    }
    a {
      color: #d62828;
      text-decoration: none;
    }
    a:hover {
      text-decoration: underline;
    }
  </style>
</head>
<body>

  <h1>🐉 Text-Based Pokémon Battle Game</h1>

  <div class="section">
    <h2>🎮 Features</h2>
    <ul>
      <li>⚔️ Turn-Based Battles with attack selection and type advantages</li>
      <li>🔁 Switch Pokémon mid-battle for tactical advantage</li>
      <li>🔥 Type Advantage System boosts or reduces attack power</li>
      <li>🤖 Computer AI selects attacks and counters your moves</li>
      <li>🧠 50 Unique Pokémon with custom stats and moves</li>
      <li>🎲 Randomized team selection for both player and computer</li>
      <li>🧪 Modular Codebase with clean separation of logic</li>
    </ul>
  </div>

  <div class="section">
    <h2>🧩 How to Play</h2>
    <ol>
      <li>Run the game: <code>python Main.py</code></li>
      <li>Your team of Pokémon is randomly selected from a pool of 50</li>
      <li>Battle begins: choose <code>[A]</code> to attack or <code>[S]</code> to switch</li>
      <li>Win by defeating all computer Pokémon!</li>
    </ol>
  </div>

  <div class="section">
    <h2>🗂️ File Structure</h2>
    <pre>
Pokemon-game/
├── Main.py
├── battle.py
├── data.py
├── utils.py
├── __pycache__/
├── .gitignore
└── README.html
    </pre>
  </div>

  <div class="section">
    <h2>🛠️ Requirements</h2>
    <ul>
      <li>Python 3.10+</li>
      <li>No external libraries required</li>
    </ul>
  </div>

  <div class="section">
    <h2>✨ Sample Gameplay</h2>
    <pre>
You were assigned Pikachu (Electric)
Computer was assigned Gyarados (Water/Flying)

🔄 Pikachu HP: 100 | Gyarados HP: 120
Choose action: [A] Attack or [S] Switch: a
🔥 Type advantage! Power boosted.
Pikachu used Thunderbolt! Gyarados HP is now 80
Gyarados used Hydro Pump! Pikachu HP is now 60
    </pre>
  </div>

  <div class="section">
    <h2>📦 Future Plans</h2>
    <ul>
      <li>Add status effects (burn, paralyze, etc.)</li>
      <li>Implement leveling and experience</li>
      <li>Save/load team selections</li>
      <li>Add ASCII art for Pokémon</li>
    </ul>
  </div>

  <div class="section">
    <h2>🧑‍💻 Author</h2>
    <p><strong>Karmrajsinh Vaghela</strong><br>
    MSc IT @ GLS University<br>
    GitHub: <a href="https://github.com/k-vaghela-111" target="_blank">k-vaghela-111</a></p>
  </div>

</body>
</html>
