This the the google app engine + flask website for tutoring.


Notes to self:

Installing Google Cloud SDK
- https://console.developers.google.com/start/appengine
- curl https://sdk.cloud.google.com/ | bash
- gcloud auth login
- gcloud components update gae-python

Getting the Code
- Get from github

Starting Local Dev server
- dev_appserver.py . (note where the dot/current directory is the top level folder of the project)

Adding 3rd party Python packages for local/live dev?
- modify requirements.txt
- pip install -r requirements.txt -t lib
- some popular ones Google will do for you: https://developers.google.com/appengine/docs/python/tools/libraries27

Update the project
- appcfg.py -A <your-project-id> --oauth2 update .
- Don't forget to push to gitup


See the GoogleReadme folder for their readmes.
