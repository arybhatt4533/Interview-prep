# 🤖 AI Interview Pro

### *Your Personal AI Technical Interviewer*

---

## 🌟 Overview

**AI Interview Pro** is an advanced AI-powered platform that simulates real-world technical interviews based on your resume. Unlike traditional mock interview tools, this system dynamically adapts questions to your **skills, projects, and experience**, creating a highly personalized and realistic interview environment.

Whether you're preparing for placements, internships, or professional roles, this tool helps you **practice smarter, not harder**.

---

## 🎯 Key Features

### 🧠 Intelligent Resume Analysis

* Extracts skills, projects, and experience from your resume (PDF supported)
* Understands context rather than just keywords

### 💬 Real-Time AI Interview Simulation

* Conducts interactive technical interviews
* Uses **context-aware questioning** with follow-ups
* Adapts difficulty level based on your responses

### 🔍 Deep Skill Evaluation

* Focuses on areas where you claim expertise
* Challenges you with real interview-level questions

### 📊 Gap Detection

* Identifies weak areas in your understanding
* Helps you improve before actual interviews

### 😌 Confidence Building

* Practice in a safe, pressure-free environment
* Improve communication and explanation skills

---

## ⚙️ Tech Stack

| Component      | Technology Used         |
| -------------- | ----------------------- |
| AI Engine      | Google Gemini 1.5 Flash |
| Backend        | Flask (Python 3.13)     |
| Environment    | python-dotenv           |
| Resume Parsing | Custom PDF Extraction   |

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/arybhatt4533/Interview-prep.git
cd Interview-prep
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Setup Environment Variables

Create a `.env` file in the root directory and add:

```
GEMINI_API_KEY=your_api_key_here
```

### 4️⃣ Run the Application

```bash
python app.py
```

---

## 📂 Project Structure

```
Interview-prep/
│
├── app.py           # Main application and AI integration
├── parsing.py       # Resume parsing logic
├── requirements.txt # Dependencies
├── .env             # API keys (ignored in Git)
├── .gitignore       # Security for sensitive files
└── README.md        # Project documentation
```

---

## 🧪 How It Works

1. Upload your resume (PDF)
2. AI extracts key details (skills, projects, tools)
3. Interview session begins
4. AI asks personalized technical questions
5. Follow-up questions are generated dynamically
6. You improve based on your responses

---

## 💡 Example Use Case

If your resume includes:

* Python
* SQL
* Cybersecurity
* Projects like *Omni-Eye* or *STDAMS*

👉 The AI will ask:

* "Explain how you implemented authentication in Omni-Eye"
* "Write an optimized SQL query for..."
* "How would you prevent SQL Injection in your system?"

---

## 🔐 Security Considerations

* API keys are stored securely using `.env`
* `.gitignore` prevents sensitive data exposure
* No user data is permanently stored

---

## 📈 Future Enhancements

* 🎤 Voice-based interview mode
* 📊 Performance analytics dashboard
* 🌐 Web-based UI (React frontend)
* 🧾 Answer evaluation with scoring system

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

---

## 📜 License

This project is open-source and available under the **MIT License**.

---

## 👨‍💻 Author

**Aryabhatt**
Cybersecurity & AI Enthusiast

---

## ⭐ Support

If you found this project useful:

* ⭐ Star the repository
* 🍴 Fork it
* 📢 Share with others

---

> "Practice like it's real, so the real interview feels easy." 🚀
