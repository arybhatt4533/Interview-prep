import os
from google import genai
from flask import Flask, render_template, request, jsonify
from parsing import extract_text_from_pdf
from dotenv import load_dotenv  # Naya import

# .env file se variables load karo
load_dotenv()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

resume_data = {"text": ""}

# API Key ab environmental variable se aa rahi hai
# Ye GitHub par leak nahi hogi
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("WARNING: API Key nahi mili! .env file check karo.")

client = genai.Client(api_key=api_key)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_page')
def upload_page():
    return render_template('upload.html')

@app.route('/interview')
def interview():
    return render_template('interview.html')

@app.route('/upload', methods=['POST'])
def handle_upload():
    try:
        file = request.files.get('resume')
        if file:
            if not os.path.exists(app.config['UPLOAD_FOLDER']):
                os.makedirs(app.config['UPLOAD_FOLDER'])
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            
            # Resume parsing (PSRIET college content, projects like Omni-Eye etc.)
            resume_data["text"] = extract_text_from_pdf(file_path)
            print("--- RESUME PARSED SUCCESSFULLY ---")
            return jsonify({"status": "success"}), 200
        return jsonify({"status": "error", "message": "No file selected"}), 400
    except Exception as e:
        print(f"Upload Error: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/ask_gemini', methods=['POST'])
def ask_gemini():
    try:
        data = request.json or {}
        user_msg = data.get("message", "Start the interview")
        
        # BCA student context load karo
        context = resume_data["text"] if resume_data["text"] else "A BCA student from Uttar Pradesh."
        
        prompt = (
            f"You are a professional technical interviewer.\n"
            f"Candidate Context: {context}\n"
            f"User says: {user_msg}\n"
            f"Instruction: Ask one deep technical question based on their skills (Python, SQL, Cybersecurity)."
        )

        # Naya SDK call
        response = client.models.generate_content(
            model="gemini-1.5-flash", 
            contents=prompt
        )
        
        return jsonify({"bot_response": response.text})

    except Exception as e:
        print(f"DEBUG ERROR: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)