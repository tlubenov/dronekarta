from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def get_welcome():
    render_template('home.html')
    #return {
    #    'welcome': 'DroneKarta.com'
    #}


@app.route('/technology')
def get_technology():
    render_template('technology.html')


@app.route('/support')
def get_support():
    render_template('support.html')


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
