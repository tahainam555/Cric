# 🏏 CricLenZ – AI Meets Cricket  
**Facial Recognition for Cricketers with Real-Time Info Retrieval**

---

## 📌 Project Description

**CricLenZ** is a unique blend of my two passions — **Cricket** and **Artificial Intelligence**.  
After gaining solid foundations in Machine Learning, I wanted to challenge myself with something beyond tutorials. That’s when I thought:

> _“Why not build a real-time face recognition app for cricketers?”_

So I did.

Using Deep Learning and the **DeepFace** library, this project can recognize cricketers' faces and instantly return their basic bio, team, role, and stats — all in real time. The system is currently scaled for **10 players**, with plans for a full-scale release featuring an extended database and a sleek user interface.

---

## 🚀 Features

- 🎯 **Face Recognition** using DeepFace (VGG-Face backend)  
- 🧠 **Deep Learning powered** – no manual feature extraction  
- 📄 **Structured JSON Data** for each player (team, role, jersey, bio, etc.)  
- ⚙️ **Local Processing** – runs on your own machine  
- 📸 **Live Webcam Detection** support  
- 📦 Designed for **modular expansion** to 100+ players  

---

## 🔍 Sample Output

When a player is recognized, the system returns:

```json
"Babar_Azam": {
  "team": "Pakistan",
  "role": "Batsman",
  "jersey no.": 56,
  "batting_style": "Right-hand bat",
  "bio": "Babar Azam is the back-bone of the Pakistan cricket team known for his elegant batting."
}
