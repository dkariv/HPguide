from flask import Flask, request, jsonify
from flask_cors import CORS # To handle Cross-Origin Resource Sharing if frontend and backend are on different ports during dev

app = Flask(__name__)
CORS(app) # This will allow all origins. For production, configure it more securely.

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message')

        if not user_message:
            return jsonify({'error': 'No message provided'}), 400

        # TODO: In a real application, you would process the user_message
        # and interact with a language model here.
        # For now, we'll just echo the message or send a fixed reply.

        # Example: Simple echo response for demonstration
        # ai_reply = f"קיבלתי את הודעתך: \"{user_message}\". אני עדיין בפיתוח."

        # Example: Fixed response
        ai_reply = "סוכן AI: תודה על פנייתך! אני עדיין בשלבי פיתוח. בקרוב אוכל לענות על שאלותיך בנוגע למערכת HomePay."

        if "שלום" in user_message.lower() or "היי" in user_message.lower():
            ai_reply = "סוכן AI: שלום! איך אני יכול לעזור לך היום עם מערכת HomePay?"
        elif "תודה" in user_message.lower():
            ai_reply = "סוכן AI: בשמחה! אם יש לך שאלות נוספות, אני כאן."
        elif "מידע על" in user_message or "איך" in user_message or "מה זה" in user_message:
            ai_reply = "סוכן AI: אני עדיין לומד על מערכת HomePay. כרגע, אני יכול להמליץ לעיין במדריך למשתמש הרלוונטי או לשאול שאלה כללית יותר."


        return jsonify({'reply': ai_reply})

    except Exception as e:
        app.logger.error(f"Error in /api/chat: {e}")
        return jsonify({'error': 'An internal server error occurred'}), 500

if __name__ == '__main__':
    # When running locally for development:
    # 1. Make sure Flask is installed: pip install Flask Flask-CORS
    # 2. Run this script: python app.py
    # 3. The Flask server will start (usually on http://127.0.0.1:5000).
    # 4. Ensure your HTML guide (e.g., homepay_guide_developer.html) is also served,
    #    perhaps using Python's http.server on a DIFFERENT port (e.g., 8000) in the directory
    #    containing all HTML, XML, CSS, and image files.
    #    Open http://localhost:8000/homepay_guide_developer.html in your browser,
    #    then click the "תמיכה עם סוכן AI" link which should go to http://localhost:8000/ai_support_agent.html.
    #    The JavaScript in ai_support_agent.html will then make requests to this Flask server (http://localhost:5000/api/chat).

    # For a more integrated setup where Flask serves everything:
    # You would typically configure Flask to serve static files (HTML, CSS, JS, images, XML)
    # from a 'static' folder and templates from a 'templates' folder.
    # This example keeps the Python server minimal and focused on the API.

    app.run(debug=True, port=5000) # Runs on http://127.0.0.1:5000/
    # Use debug=False in a production environment

# Instructions for running:
# 1. Save this file as app.py in your project root.
# 2. Install Flask and Flask-CORS:
#    pip install Flask Flask-CORS
# 3. Run the server:
#    python app.py
# 4. Serve your HTML/XML/Image files using another local server (e.g., `python -m http.server 8000` in the same directory)
#    or integrate static file serving into Flask for a more robust setup.
# 5. Access ai_support_agent.html through the server that serves the HTML files (e.g., http://localhost:8000/ai_support_agent.html).
#    The chat should then communicate with this Flask app on port 5000.
