from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>CI/CD Pipeline</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #8e0e00, #1f1c18); 
                color: white;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                text-align: center;
            }
            .card {
                background: rgba(255, 255, 255, 0.1);
                padding: 40px;
                border-radius: 16px;
                box-shadow: 0 8px 20px rgba(0,0,0,0.3);
                backdrop-filter: blur(10px);
            }
            h1 {
                color: #ffcc00; 
                margin-bottom: 10px;
            }
            p {
                font-size: 18px;
                opacity: 0.9;
            }
            .emoji {
                font-size: 40px;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <div class="emoji">🚀</div>
            <h1>CI/CD Pipeline Success!</h1>
            <p>Welcome to your first Flask App.</p>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)