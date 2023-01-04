from flask import Flask , redirect, url_for, request, render_template, make_response, session
app = Flask(__name__)

#for sessions

from flask import Flask, session, redirect, url_for, escape, request, render_template
app = Flask(__name__)
app.secret_key = "ANY RENDOM STRING"



# @app.route('/')
# def hello_world():
#    return "<h1>Hello World. This to be a wonderful. Hai </h1>"


# @app.route('/admin')
# def hello_admin():
#    return 'Hello Admin'

# @app.route('/guest/<guest>')
# def hello_guest(guest):
#    return 'Hello %s as Guest' % guest

# @app.route('/user/<name>')
# def hello_user(name):
#    if name =='admin':
#       return redirect(url_for('hello_admin'))
#    else:
#       return redirect(url_for('hello_guest',guest = name))




# @app.route('/success/<name>')
# def success(name):
#    return 'welcome %s' % name

# @app.route('/login',methods = ['POST', 'GET'])
# def login():
#    if request.method == 'POST':
#       user = request.form['nm']
#       return redirect(url_for('success',name = user))
#    else:
#       user = request.args.get('nm')
#       return redirect(url_for('success',name = user))

# @app.route('/home')
# def home():
#     return render_template('home1.html')

# @app.route('/home/<user>')
# def hello_name(user):
#    return render_template('home.html', name = user)

# @app.route('/hello/<int:score>')
# def hello_name1(score):
#    return render_template('home.html', marks = score)


# @app.route('/result')
# def result():
#    dict = {'phy':50,'che':60,'maths':70}
#    return render_template('result.html', result = dict)

###==================================================================================


##sending Form data to templates. 
# @app.route('/')
# def student():
#    return render_template('student.html')

# @app.route('/result',methods = ['POST', 'GET'])
# def result():
#    if request.method == 'POST':
#       result = request.form
#       print(result)
#       return render_template("result1.html",result = result)



#########=====================================================================================

#Cookies

# @app.route('/')
# def index():
#    return render_template('cookies/index.html')


# @app.route('/setcookie', methods = ['POST', 'GET'])
# def setcookie():
#     if request.method == 'POST':
#         user = request.form['nm']
   
#         resp = make_response(render_template('cookies/readcookie.html'))
#         resp.set_cookie('userID', user)
        
#     return resp

# @app.route('/getcookie')
# def getcookie():
#     name = request.cookies.get('userID')
#     return '<h1>welcome '+name+'</h1>'

###============================================================


###Sessions

# @app.route('/')
# def index():
#     if 'username' in session:
#         username = session['username']
#         return 'Logged in as ' + username + '<br>' + "<b><a href = '/logout'>click here to log out</a></b>"
#     return "You are not logged in <br><a href = '/login'></b>" + \
#       "click here to log in</b></a>"

# @app.route('/login', methods = ['GET', 'POST'])
# def login():
#    if request.method == 'POST':
#       session['username'] = request.form['username']
#       return redirect(url_for('index'))
#    return render_template('sessions/login.html')
	
   
# @app.route('/logout')
# def logout():
#    # remove the username from the session if it is there
#    session.pop('username', None)
#    return redirect(url_for('index'))


####  +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#### for redirect and errorss


# from flask import Flask, redirect, url_for, render_template, request, abort
# app = Flask(__name__)

# @app.route('/')
# def index():
#    return render_template('redirect/login.html')

# @app.route('/login',methods = ['POST', 'GET'])
# def login():
#     if request.method == 'POST':
#         if request.form['username'] == 'admin' :
#             return redirect(url_for('success'))
#         else:
#             abort(401)
#     else:
#         return redirect(url_for('index'))



# @app.route('/success')
# def success():
    
#    return f'logged in successfully.'

########==========================================================================================================================================================


#### for message flashing...........................................................................

# from flask import Flask, flash, redirect, render_template, request, url_for
# app = Flask(__name__)
# app.secret_key = 'random string'

# @app.route('/')
# def index():
#    return render_template('messageflashing/index.html')

# @app.route('/login', methods = ['GET', 'POST'])
# def login():
#    error = None
   
#    if request.method == 'POST':
#       if request.form['username'] != 'admin' or \
#          request.form['password'] != 'admin':
#          error = 'Invalid username or password. Please try again!'
#       else:
#          flash('You were successfully logged in')
#          return redirect(url_for('index'))
			
#    return render_template('messageflashing/login.html', error = error)

# if __name__ == "__main__":
#    app.run(debug = True)

##################-------------------------------------------------------------------------------

### for file uploading----This one not working--------------------------


# from flask import Flask, render_template, request
# from werkzeug import secure_filename
# app = Flask(__name__)

# @app.route('/upload')
# def upload_file():
#    return render_template('fileuploading/upload.html')
	
# @app.route('/uploader', methods = ['GET', 'POST'])
# def upload_file():
#    if request.method == 'POST':
#       f = request.files['file']
#       f.save(secure_filename(f.filename))
#       return 'file uploaded successfully'
		
# if __name__ == '__main__':
#    app.run(debug = True)

#####   ===============================================================================================

### for flask mail

# from flask import Flask
# from flask_mail import Mail, Message

# app =Flask(__name__)
# mail=Mail(app)

# app.config['MAIL_SERVER']='smtp.gmail.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USERNAME'] = 'yourId@gmail.com'
# app.config['MAIL_PASSWORD'] = '*****'
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True
# mail = Mail(app)

# @app.route("/")
# def index():
#    msg = Message('Hello', sender = 'yourId@gmail.com', recipients = ['id1@gmail.com'])
#    msg.body = "Hello Flask message sent from Flask-Mail"
#    mail.send(msg)
#    return "Sent"

# if __name__ == '__main__':
#    app.run(debug = True)


#############                  ++++++++++++++++++++++


#################### Flask Forms - not running

# from flask import Flask, render_template, request, flash
# from forms import ContactForm
# app = Flask(__name__)
# app.secret_key = 'development key'

# @app.route('/contact', methods = ['GET', 'POST'])
# def contact():
#    form = ContactForm()
   
#    if request.method == 'POST':
#         if form.validate() == False:
#             flash('All fields are required.')
#             return render_template('forms/contact.html', form = form)
        
#         else:
#              return render_template('forms/success.html')
    

#    elif request.method == 'GET':
#         return render_template('forms/contact.html', form = form)
    

# if __name__ == '__main__':
#    app.run(debug = True)



###########################################################################################################################

### FLASL SQLITE
### for this programme to work we need to db first. 
### so run the database.py first before running this programme.



# from flask import Flask, render_template, request
# ## from flask_sqlalchemy import SQLAlchemy
# import sqlite3 as sql

# app = Flask(__name__)

# @app.route('/')
# def home():
#    return render_template('sqlite/home.html')

# @app.route('/enternew')
# def new_student():
#    return render_template('sqlite/student.html')

# @app.route('/addrec',methods = ['POST', 'GET'])
# def addrec():
#     print(request.method)
#     if request.method == 'POST':
#         try:
#             nm = request.form['nm']
#             addr = request.form['add']
#             city = request.form['city']
#             pin = request.form['pin']
#             print(nm, addr, city, pin)
         
#             with sql.connect("database.db") as con:
#                 cur = con.cursor()                
#                 cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)" ,(nm,addr,city,pin))
#                 con.commit()
#                 msg = "Record successfully added"

#         except:
#             con.rollback()
#             msg = "error in insert operation"
      
#         finally:
#             con.close()
#             return render_template("sqlite/result.html",msg = msg)
            
# @app.route('/list')
# def list():
#    con = sql.connect("database.db")
#    con.row_factory = sql.Row
   
#    cur = con.cursor()
#    cur.execute("select * from students")
   
#    rows = cur.fetchall();
#    return render_template("sqlite/list.html",rows = rows)

# if __name__ == '__main__':
#    app.run(debug = True)


################################################################################3333333333333333333333333



### FLASK SQLALCHEMY

# from flask import Flask, request, flash, url_for, redirect, render_template
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
# app.config['SECRET_KEY'] = "random string"

# db = SQLAlchemy(app)

# class students(db.Model):
#    id = db.Column('student_id', db.Integer, primary_key = True)
#    name = db.Column(db.String(100))
#    city = db.Column(db.String(50))
#    addr = db.Column(db.String(200)) 
#    pin = db.Column(db.String(10))

# def __init__(self, name, city, addr,pin):
#    self.name = name
#    self.city = city
#    self.addr = addr
#    self.pin = pin

# @app.route('/')
# def show_all():
#    return render_template('sqlalchemy/show_all.html', students = students.query.all() )

# @app.route('/new', methods = ['GET', 'POST'])
# def new():
#     if request.method == 'POST':
#         if not request.form['name'] or not request.form['city'] or not request.form['addr']:
#             flash('Please enter all the fields', 'error')
#         else:
#             student = students(name = request.form['name'], city = request.form['city'],addr =  request.form['addr'],pin =  request.form['pin'])         
#             # student = students(name = request.form['name'], request.form['city'], request.form['addr'], request.form['pin'])         
            
#             db.session.add(student)
#             db.session.commit()
#             flash('Record was successfully added')
#             return redirect(url_for('show_all'))
#     return render_template('sqlalchemy/new.html')

# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()
#         app.run(debug = True)


####=========================================================================================================================================================================



####################  Flask Sijax


# import os , flask_sijax
# from flask import Flask, g , render_template
# from flask_sijax import sijax

# app = Flask(__name__)

# ## sijax setup and config
# path = os.path.join('.', os.path.dirname(__file__), 'static/js/sijax/')
# app.config['SIJAX_STATIC_PATH'] = path
# app.config['SIJAX_JSON_URI'] = '/static/js/sijax/json2.js'
# flask_sijax.Sijax(app)

# @app.route('/')
# def index():
#    return 'Index'

# #sijax index route	
# @flask_sijax.route(app, '/hello')
# def hello():
#     def say_hi(obj_response):
#         obj_response.alert('This is my first application.!')
#     if g.sijax.is_sijax_request:

#     # #   # Sijax request detected - let Sijax handle it
#         g.sijax.register_callback('say_hi', say_hi)
#         return g.sijax.process_request()
    
#     return render_template('sijax/sijaxexample.html')

# if __name__ == '__main__':
#    app.run(debug = True)

####################################================================================================================================




##### Integration of Sijax with database.


from flask import Flask, request, flash, url_for, redirect, render_template 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

#sijax setup and config.
import os, flask_sijax
from flask import Flask, g
from flask_sijax import sijax

path = os.path.join('.', os.path.dirname(__file__), 'static/js/sijax/')
# app = Flask(__name__)

app.config['SIJAX_STATIC_PATH'] = path
app.config['SIJAX_JSON_URI'] = '/static/js/sijax/json2.js'
flask_sijax.Sijax(app)

class students(db.Model):
   id = db.Column('student_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   city = db.Column(db.String(50))
   addr = db.Column(db.String(200)) 
   pin = db.Column(db.String(10))

def __init__(self, name, city, addr,pin):
   self.name = name
   self.city = city
   self.addr = addr
   self.pin = pin

@app.route('/')
def show_all():
   return render_template('sijaxdatabase/show_all.html', students = students.query.all() )

@app.route('/new', methods = ['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['city'] or not request.form['addr']:
            flash('Please enter all the fields', 'error')
        else:
            student = students(name = request.form['name'], city = request.form['city'],addr =  request.form['addr'],pin =  request.form['pin'])         
            # student = students(name = request.form['name'], request.form['city'], request.form['addr'], request.form['pin'])         
            
            db.session.add(student)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('sijax_search1'))
    return render_template('sijaxdatabase/new.html')




#sijax index route	
@flask_sijax.route(app, '/sijax_search1')
def sijax_search1():
    if request.form == 'POST':
        print(request.form)
        Message = {"Message": "Python says Hello."}
        return Message

    def sijax_search_function(obj_response, search_text):
        obj_response.alert("Search text box value goofey: " + search_text)
        
    
    # check if its sijax request
    if g.sijax.is_sijax_request:
        g.sijax.register_callback('sijax_search', sijax_search_function)
        return g.sijax.process_request() 


        

    def say_hi(obj_response):
        obj_response.alert('This is my first application.!')
    if g.sijax.is_sijax_request:

    # #   # Sijax request detected - let Sijax handle it
        g.sijax.register_callback('say_hi', say_hi)
        return g.sijax.process_request()

    ## to render all the objects of  the students database.
    
    
    return render_template('sijaxdatabase/new.html', students = students.query.all(), )

if __name__ == '__main__':
   app.run(debug = True)














if __name__ == '__main__':
    app.run(debug=True)  
