# commonsmisc

This repo contains some scripts for using with Commons mobile app, in future maybe other ways too. All scripts reside in https://tools.wmflabs.org/wikimedia-commons-app/commonsmisc/, just append filename. 

## revertsbyuser.py

This script return a single number representing number of total uploads of certain given user. This includes reuploads of files either uploaded by the same user or by somebody else. 

### Overview
* HTTP method: GET
* Output - single number or nouser when no user was given
* Parameters
  * user - mandatory - string - username of user you want to examine - spaces doesn't matter, Vivek maskara and Vivek Maskara is the same
* Example request: http://tools.wmflabs.org/wikimedia-commons-app/commonsmisc/uploadsbyuser.py?user=Maskaravivek