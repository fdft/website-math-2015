from flask import Flask, request, jsonify
import json
from google.appengine.api import mail

from django.utils.html import strip_tags
from django.utils.html import escape
from lxml.html.clean import Cleaner
import urllib2
import urllib

app = Flask(__name__,static_url_path='')
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return app.send_static_file('index.html')

@app.route('/contactme', methods=['POST'])
def emailMe():
	"""Get form data and forward the message to me."""
	
	
	#https://cloud.google.com/appengine/docs/python/tools/libraries27	
	#http://stackoverflow.com/questions/10434599/how-can-i-get-the-whole-request-post-body-in-python-with-flask
	name=request.form.get('name');
	phone = request.form.get('phone');
	email = request.form.get('email');
	message=request.form.get('message');
	cap = request.form.get('g-recaptcha-response');
	
	#print name, phone, email, message;
	#print cap
	
	

	#first check the Google recaptcha
	url = "https://www.google.com/recaptcha/api/siteverify"
	form_fields = {
	  "secret": "6Lc7kQcTAAAAABhFDnbFI8euTPUyApj4_B43Gy87",
	  "response": cap,
	}
		
	form_data = urllib.urlencode(form_fields)
	try:
		req = urllib2.Request(url, form_data)
		response = urllib2.urlopen(req)
		the_page = json.loads(response.read())
		print("cap response is " + str(the_page));
		print(the_page['success']);
		print("what");
		if ( the_page['success'] != True):
			return jsonify(success=False);#return empty object		
	except urllib2.URLError, e:
		return jsonify(success=False); #return empty object
		

	#so the captcha is valid. Now clean the user data
	cleaner = Cleaner()
	cleaner.javascript = True # This is True because we want to activate the javascript filter
	cleaner.style = True      # This is True because we want to activate the styles & stylesheet filter
	cleaner.scripts = True
	cleaner.links = True
	cleaner.allow_tags = None
	
	
	name = cleaner.clean_html(name)
	phone = cleaner.clean_html(phone)
	email = cleaner.clean_html(email)
	message = cleaner.clean_html(message)
	
	#build the email
	newMess = mail.EmailMessage();
	newMess.sender ="pizzaoptimization <pizzaoptimization@gmail.com>"
	newMess.subject = escape(strip_tags("Website Contact for tutoring:  "+ name))
	newMess.to = "pizzaoptimization <pizzaoptimization@gmail.com>"
	newMess.body = escape(strip_tags("Name: " + name + "\nemail: " + email + "\nphone: " + phone + "\nmessage: " + message))
	
	#send the email
	newMess.send()	
	
	return jsonify(success=True);
	


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
