import os
from flask_wtf import FlaskForm
from flask import Flask, render_template, session,request, send_from_directory
from wtforms.validators import InputRequired, Email, Length, AnyOf
from wtforms import StringField, PasswordField, StringField, FileField
from werkzeug.utils import secure_filename
from forms import LoginForm, UploadForm
from pages import form_page

app = Flask(__name__)
UPLOAD_FOLDER = r'C:\Users\Yasch\Desktop\my_apps\master_flask\files'


app.config['SECRET_KEY']='Thisisasecret!'
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER

@app.route('/form', methods= ['GET', 'POST'])
def form_page():
    # creates the form object
    form = LoginForm()
    # makes sure logged_in is False to keep pages that require
    # logged_in to be proteced
    session['logged_in'] = False
    # makes sure form has valid entries or returns false
    if form.validate_on_submit():
        # accesses the form username and password values
        #  and sets the session values
        session['username'] = form.username.data
        session['password'] = form.password.data
        #need to address this!!!!
        if (session['username'] == ) and (session['password'] == ):
            session['logged_in'] = True
            return go_to_routman_home_page()
    #if login didn't occur displays login page
    return render_template('login.html',form = form)

@app.route('/file_upload',methods =['GET','POST'])
def get_file():
    # gets the UploadForm that allows to upload file
    form = UploadForm()
    #if file is attached
    if form.validate_on_submit():
        # gets the file
        file = (request.files['file'])
        #gets the filename
        filename = secure_filename(file.filename)
        #saves the file to path of UPLOAD_FOLDER
        file.save(os.path.join(UPLOAD_FOLDER,filename))
    # renders the file_upload page attaches the UploadForm and lists all files
    # saved in the folder
    return render_template('file_upload.html',form = form,files_list  =os.listdir(UPLOAD_FOLDER))

if __name__ == '__main__':
    app.run(debug=True)