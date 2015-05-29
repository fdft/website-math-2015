from flask import Flask, request, jsonify
import json
from google.appengine.api import mail
import BeautifulSoup


app = Flask(__name__,static_url_path='')
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    print('got here')
    return app.send_static_file('index.html')

@app.route('/contactme', methods=['POST'])
def emailMe():
	
#https://cloud.google.com/appengine/docs/python/tools/libraries27	
#http://stackoverflow.com/questions/10434599/how-can-i-get-the-whole-request-post-body-in-python-with-flask
	name=request.form.get('name');
	phone = request.form.get('phone');
	email = request.form.get('email');
	message=request.form.get('message');
	#print name, phone, email, message;
	
	
	
	newMess = mail.EmailMessage();
	newMess.sender ="pizzaoptimization <pizzaoptimization@google.com>"
	newMess.subject = "Website Contact for tutoring:  "+ name
	newMess.to = "pizzaoptimization <pizzaoptimization@google.com>"
	newMess.body = "Name: " + name + "\nemail: " + email + "\nphone: " + phone + "\nmessage: " + message

	newMess.send()	
	
	return jsonify(success=1);
	


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
