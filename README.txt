This the the google app engine + flask website for tutoring.


Notes to self:

Installing Google Cloud SDK
- https://console.developers.google.com/start/appengine
- (the Cloud SDK) curl https://sdk.cloud.google.com/ | bash
- (App Engine SDKs) (like appcfg/dev_appserver) 
  https://cloud.google.com/appengine/downloads
- gcloud auth login
- gcloud components update gae-python

Getting the Code
- Get from github
- or the more complicated way: developers console > source code > browse > settings for instructions on how to pull it from GAE and commit it back into github. 

Starting Local Dev server
- dev_appserver.py . (note where the dot/current directory is the top level folder of the project)

Adding 3rd party Python packages for local/live dev?
- modify requirements.txt
- pip install -r requirements.txt -t lib
- some popular ones Google will do for you: https://developers.google.com/appengine/docs/python/tools/libraries27

Update the project
- appcfg.py -A <your-project-id> --oauth2 update .
- If you bump the version number in the app.yaml file, you have to change the default serving app number in developers console > compute >  app engine > versions
- Don't forget to push to github


See the GoogleReadme folder for their readmes.
