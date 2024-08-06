# Frontend (HTML/CSS/JavaScript)
# Use a simple HTML form to interact with the Flask API.

### index.html

<!DOCTYPE html>
<html>
<head>
    <title>Timesheets</title>
    <script>
        async function submitTimesheet() {
            const employeeId = document.getElementById('employee_id').value;
            const weekEnding = document.getElementById('week_ending').value;
            const hoursWorked = document.getElementById('hours_worked').value;
            const tasks = document.getElementById('tasks').value;

            const response = await fetch('/timesheet', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    employee_id: employeeId,
                    week_ending: weekEnding,
                    hours_worked: hoursWorked,
                    tasks: tasks,
                }),
            });

            const result = await response.json();
            console.log(result);
        }
    </script>
</head>
<body>
    <h1>Submit Timesheet</h1>
    <form onsubmit="event.preventDefault(); submitTimesheet();">
        <label for="employee_id">Employee ID:</label><br>
        <input type="text" id="employee_id" name="employee_id"><br>
        <input type="text" id="employee_name" name="employee_name"><br>
        <label for="week_ending">Week Ending:</label><br>
        <input type="text" id="week_ending" name="week_ending"><br>
        <label for="hours_worked">Hours Worked:</label><br>
        <input type="number" id="hours_worked" name="hours_worked"><br>
        <label for="client">Tasks:</label><br>
        <input type="text" id="client" name="client"><br><br>
        <label for="engagement_name">Tasks:</label><br>
        <input type="text" id="engagement_name" name="engagement_name"><br><br>
        <label for="engagement_activity">Tasks:</label><br>
        <input type="text" id="engagement_activity" name="engagement_activity"><br><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>

### To serve this HTML file, update the Flask app:

### from flask import render_template

@app.route('/')
def home():
    return render_template('index.html')

# Running the Application
### Run your Flask server:
python app.py

Open your browser and navigate to http://localhost:5000.
