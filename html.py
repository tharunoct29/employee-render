"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>NovaTech Leave Tracker</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f4f6f8;
            margin: 0;
        
            padding: 40px;
        }

        .container {
            max-width: 900px;
            margin: auto;
            background: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        }

        h1 {
            color: #1f2937;
        }

        .subtitle {
            color: #6b7280;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 25px;
        }

        th, td {
            padding: 12px;
            border-bottom: 1px solid #ddd;
            text-align: left;
        }

        th {
            background: #2563eb;
            color: white;
        }

        form {
            margin-top: 30px;
            padding: 20px;
            background: #f8fafc;
            border-radius: 8px;
        }

        input, select, button {
            padding: 10px;
            margin: 5px;
        }

        button {
            background: #2563eb;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        button:hover {
            background: #1d4ed8;
        }

        .message {
            margin-top: 20px;
            padding: 12px;
            background: #dcfce7;
            color: #166534;
            border-radius: 5px;
        }
    </style>
</head>

<body>

<div class="container">

    <h1>NovaTech Solutions</h1>
    <p class="subtitle">Employee Leave Tracker</p>

    {% if message %}
        <div class="message">
            {{ message }}
        </div>
    {% endif %}

    <h2>Employee Leave Balance</h2>

    <table>
        <tr>
            <th>Name</th>
            <th>Department</th>
            <th>Remaining Leave</th>
        </tr>

        {% for employee in employees %}
        <tr>
            <td>{{ employee.name }}</td>
            <td>{{ employee.department }}</td>
            <td>{{ employee.leave_days }} days</td>
        </tr>
        {% endfor %}
    </table>

    <form action="/apply-leave" method="POST">

        <h2>Apply for Leave</h2>

        <select name="employee_id" required>
            <option value="">Select Employee</option>

            {% for employee in employees %}
                <option value="{{ employee.id }}">
                    {{ employee.name }}
                </option>
            {% endfor %}
        </select>

        <input
            type="number"
            name="days"
            min="1"
            placeholder="Number of days"
            required
        >

        <button type="submit">
            Apply Leave
        </button>

    </form>

</div>

</body>
</html>"""