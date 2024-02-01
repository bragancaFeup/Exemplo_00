import sys
from flask import Flask, render_template, request, g
from classes.person import Person
from datafile import filename

app = Flask(__name__)

Person.read(filename)
prev_option = ""

@app.route("/", methods=["post","get"])
def index():
    global prev_option
    butshow = "enabled"
    butedit = "disabled"
    option = request.args.get("option")
    if option == "edit":
        butshow = "disabled"
        butedit = "enabled"
    elif option == "delete":
        obj = Person.current()
        Person.remove(obj.code)
        if not Person.previous():
            Person.first()
        Person.write(filename)
    elif option == "insert":
        butshow = "disabled"
        butedit = "enabled"
    elif option == 'cancel':
        pass
    elif prev_option == 'insert':
        strobj = request.form["code"] + ';' + request.form["name"] + ';' + \
        request.form["dob"] + ';' + request.form["salary"]
        Person.from_string(strobj)
        Person.write(filename)
        Person.last()
    elif prev_option == 'edit':
        obj = Person.current()
        obj.code = request.form["code"]
        obj.name = request.form["name"]
        obj.dob = request.form["dob"]
        obj.salary = float(request.form["salary"])
        Person.write(filename)
    elif option == "first":
        Person.first()
    elif option == "previous":
        Person.previous()
    elif option == "next":
        Person.nextrec()
    elif option == "last":
        Person.last()
    elif option == 'exit':
        db = getattr(g, '_database', None)
        if db is not None:
            db.close()
        sys.exit()
    prev_option = option
    obj = Person.current()
    if option == 'insert':
        code = ""
        name = ""
        dob = ""
        salary = ""
    else:
        code = obj.code
        name = obj.name
        dob = obj.dob
        salary = obj.salary

    return render_template("index.html", butshow=butshow, butedit=butedit, code=code,name = name,dob=dob,salary=salary)

if __name__ == '__main__':
    app.run()