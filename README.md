# 🐍 Classic Snake Game - Days 20 & 21 of #100DaysOfCode

<div align="center">

![Python](https://img.shields.io/badge/Python-3.13.1-blue.svg)
![GUI](https://img.shields.io/badge/GUI-Turtle%20Graphics-yellow)
![OOP](https://img.shields.io/badge/OOP-Clean%20Structure-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Last Updated](https://img.shields.io/badge/Updated-June%202025-brightgreen)

A fully functional **Snake Game** built with Python’s turtle module using **Object-Oriented Programming** principles 🧠🎮

> Control the snake, eat food, grow longer… and avoid hitting walls or yourself!

</div>

---

## 📸 Preview

![image](https://github.com/user-attachments/assets/e0f923ac-6c88-4b1c-b3d6-bcb565fb6266)


---

## ✨ Features

- 🎮 Classic snake movement & growth
- 🧱 Collision detection with walls & self
- 🍎 Random food generation
- 💯 Score tracking with dynamic UI
- 🔁 Smooth movement using `screen.tracer(0)`
- 🎯 OOP: organized into multiple classes

---

## 📂 Project Structure

```bash
snake-game/
├── main.py              # Entry point - game loop
├── snake.py             # Snake behavior & controls
├── food.py              # Food object
├── scoreboard.py        # Score handling and display
├── assets/
│   └── snake-game-preview.png
├── README.md
└── LICENSE
```
🧠 How It Works
Snake class: creates and moves the snake

Food class: handles food spawn with .refresh()

Score class: displays and updates score

Arrow keys to control direction (with heading limits)

Game over when snake hits wall or itself

💻 Run it Locally
bash
نسخ
تحرير
python main.py
✅ No external packages
✅ Cross-platform
✅ Pure Turtle magic 🐢

🔧 Customize
Change speed: modify time.sleep(0.1)

Grid size: edit screen.setup()

Colors, fonts, dot shapes — go wild! 🎨

📝 License
MIT License — use it, tweak it, share it 💚

🙏 Credits
Project by @Mohammed23200

Based on #100DaysOfCode with Dr. Angela Yu

Inspired by the OG snake game we all loved 🕹️

<div align="center"> Made with ❤️, 🐍, and good old Python </div> ```
