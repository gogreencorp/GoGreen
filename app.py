from flask import Flask, make_response, render_template, redirect, request
import sql

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("form.html")


@app.route('/info', methods=['post', 'get'])
def info_page():
    message = ''
    if request.method == 'POST':
        soil_type = request.form.get('soil_type')  # access the data inside
        area_temp = request.form.get('area_temp')
        soil_ph = request.form.get('soil_ph')
        topography = request.form.get('topography')

        if (soil_type == "1" and area_temp == "1" \
        and soil_ph == "1" and topography == "1"):
            message = "Recommended plant for this area: Cereals"
        else:
            message = "More plants coming up"

    return render_template('info.html', message=message)


@app.route('/transfer')
@app.route('/transfer/')
def transfer():
    # return "", 302, {'location': 'http://localhost:5000/login'}
    # return redirect("http://localhost:5000/login")

    # By default, redirect() performs a HTTP 302 redirect, to
    # perform a HTTP 301 redirect pass the HTTP status code of 301
    # to the redirect() function as follows:
    return redirect("http://localhost:5000/login", code=301)


if __name__ == "__main__":
    app.run(debug=True)
