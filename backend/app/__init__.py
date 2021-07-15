from flask import Flask

app = Flask(__name__)


@app.route('/')
def get_welcome():
    return {
        'welcome': 'DroneKarta.com'
    }

@app.route('/service')
def get_service():
    return {
        'service': 'dronekarta',
        'type': 'restful',
        'status': 'available',
        'version': 'v202107',
        'license': 'Closed'
    }


if __name__ == '__main__':
    app.run(host='0.0.0.0')
