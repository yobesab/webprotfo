from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)  # instance of flask app - main
print(__name__)


# @app.route('/<username>/<int:post_id>')  # decortor for home route rquest
# def hello_world(username=None, post_id = None):
#     return render_template('index.html', name = username, post_id=post_id)


@app.route('/')  # decortor for blog rquest
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')  # decortor for html pages rquest
def html_pages(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:  # append mode
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')  # write in a new line every time I have a data


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:  # append mode, and add newline
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            # data = request.form['email']
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong'
