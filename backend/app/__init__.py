from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def get_welcome():
    return render_template('home.html')
    #return {
    #    'welcome': 'DroneKarta.com'
    #}


@app.route('/technology')
def get_technology():
    return render_template('technology.html')


@app.route('/support')
def get_support():
    return render_template('support.html')


@app.route('/information')
def get_information():
    return render_template('information.html')


@app.route('/test')
def test():
    return render_template('test.html')


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
