from flask import Flask, render_template, request

app = Flask(__name__)

employees = [
    {"id": 1, "name": "Rahul", "department": "IT", "leave_days": 12},
    {"id": 2, "name": "Anjali", "department": "HR", "leave_days": 8},
    {"id": 3, "name": "Arjun", "department": "Finance", "leave_days": 15},
]


@app.route("/")
def home():
    return render_template("index.html", employees=employees)


@app.route("/apply-leave", methods=["POST"])
def apply_leave():
    employee_id = int(request.form["employee_id"])
    days = int(request.form["days"])

    for employee in employees:
        if employee["id"] == employee_id:
            if employee["leave_days"] >= days:
                employee["leave_days"] -= days
                message = f"Leave approved for {employee['name']}."
            else:
                message = "Not enough leave balance."
            break
    else:
        message = "Employee not found."

    return render_template(
        "index.html",
        employees=employees,
        message=message
    )


if __name__ == "__main__":
    app.run(debug=True)