from flask import Flask, render_template, jsonify

app = Flask(__name__)

# making changes to HTML doc can be trick
# job data is stored some where else in a database
# what is done is    1. information is fetch from a database
#                    2. entered in to html file and then displayed on screen

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': "Banglore India",
  'salary': 'Rs 10,00,000'
}, {
  'id': 2,
  'title': 'Data Scientist',
  'location': "Delhi India",
  'salary': 'Rs 15,00,000'
}, {
  'id': 3,
  'title': 'Frontend Engineer',
  'location': "Remote",
  'salary': 'Rs 12,00,000'
}, {
  'id': 4,
  'title': 'Backend Engineer',
  'location': "San Fransisco USA",
  'salary': '$120,000'
}]


@app.route('/')
def hello():
  return render_template('home.html', jobs=JOBS, company_name='VISH')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
