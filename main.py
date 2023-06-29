from flask import Flask, render_template, jsonify
from database import load_jobs_from_db

app = Flask(__name__)

# making changes to HTML doc can be trick
# job data is stored some where else in a database
# what is done is    1. information is fetch from a database
#                    2. entered in to html file and then displayed on screen

# excalidraw to draw
# use upsplash for images
# use ipsum lorem for text generation -->
# to write mail links use https://mailtolink.me/


@app.route('/')
def hello():
  jobs = load_jobs_from_db()
  return render_template('home.html', jobs=jobs, company_name='VISH')


@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)

# database: vish_database
# username: em1g69p3rxw5tkr2anl0
# host: aws.connect.psdb.cloud
# password: pscale_pw_VeOSfNfu90mCv6VQzKIFkVVlQEd1LL5b9iO1nHDPEE0
