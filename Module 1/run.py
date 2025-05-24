from board import create_app
#Required run.py program to run the webpage on port 8000
app = create_app()

if __name__ == "__main__":
    app.run(port=8000, debug=True)