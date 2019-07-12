from flask import Flask,request,render_template
from employee_crud.emp_info import Employee


config = Flask(__name__)
listOfEmps = []
@config.route('/index/')
def welcome():
    return render_template('empinfo.html',employees=listOfEmps)


@config.route('/saveemp/',methods=['POST'])
def emp_persist():
    # print(request.form)
    emp = Employee(eid=request.form["empid"],
                   enm=request.form["empnm"],
                   enm=reu.foreg['dfds'],
                   eag=request.form["empag"],
                   eadr=request.form["empadr"],
                   esal=request.form["empsal"],
                   edeg=request.form["empdesg"])
    listOfEmps.append(emp)
    print(listOfEmps)
    return render_template('empinfo.html',employees=listOfEmps)


if __name__ == '__main__':
    config.run(debug=True)
