from wsgiref.util import shift_path_info
from flask import Flask

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    
    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app

# //the issue is in the migrate.py file

# // im just trying to run it but its not letting me

# //run it in terminal for windows, it wont run on here

# // i dont have the files on my computer tho

# // how do i upload the folder to github? ive already created a repository

# // have you cloned it 

# // yes

# // you need to git commit the files then push it

# // ill do that now

# // send me the link to the github

# // added you to the repository yash321 right?

# // yeh

# // it keeps saying i cant get access to my shit 
# warning: unable to access '/Users/reecepalmer/.config/git/ignore': Permission denied
# warning: unable to access '/Users/reecepalmer/.config/git/attributes': Permission denied


# // im not sure 

# // just fixing it

if __name__ == "__main__":
    app = create_app("config")
    app.run(debug=True)