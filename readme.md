# Script Updater
A script that allows you to update other scripts. Uses **Python 3.6+** and **Bash**.  
  
The script makes a request to your domain and check the latest version in file *version.html*.  
If the user’s version is less than indicated on the server, then the script will be updated.  

## File structure
```
│── updater.py
│── config.py  # The path to the script, the user writes for himself
│── const.py  # The current version of the script,  
URL to the archive with the latest update,  
URL to the HTML file with the latest version of the script.
```

### How to use
* Specify the *URLs* and *version* in the file **const.py**
* On the server, create a file **version.html**, so that it is available at the link **https://domain.com/version.html**  
Write the latest version of your script in it.
* Put the archive with the latest version of your script next and call **last_update.tar.xz**