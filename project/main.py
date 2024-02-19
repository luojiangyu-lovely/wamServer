from app import create_app
from app.settings import PORT, HOST
app = create_app()
if __name__ == '__main__':
    app.run(port=PORT, debug=True, host=HOST,threaded=True)
