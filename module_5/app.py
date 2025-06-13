"""Flask app to display applicant query data in a dashboard."""
#code converted from module_3 to get a 10/10 Lint Score
from flask import Flask, render_template
from query_data import get_all_query_results


def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)

    @app.route("/")
    def dashboard():
        """Route to display applicant statistics on a dashboard."""
        data = get_all_query_results()
        questions = [
            (
                "1. How many entries do you have in your database who have applied for Fall 2025?",
                data["q1"]
            ),
            (
                "2. What percentage of entries are from international students "
                "(not American or Other)?",
                f"{data['q2']}%"
            ),
            (
                "3. What is the average GPA, GRE, GRE V, GRE AW of applicants "
                "who provide these metrics?",
                f"{data['q3'][0]}, {data['q3'][1]}, {data['q3'][2]}, {data['q3'][3]}"
            ),
            (
                "4. What is the average GPA of American students in Fall 2025?",
                data["q4"]
            ),
            (
                "5. What percent of entries for Fall 2025 are Acceptances "
                "(to two decimal places)?",
                f"{data['q5']}%"
            ),
            (
                "6. What is the average GPA of applicants who applied for Fall 2025 "
                "and were accepted?",
                data["q6"]
            ),
            (
                "7. How many entries are from applicants who applied to "
                "Johns Hopkins University for a master's degree in Computer Science?",
                data["q7"]
            ),
        ]
        return render_template("dashboard.html", questions=questions)

    return app


if __name__ == "__main__":
    APP = create_app()
    APP.run(port=8001, debug=True)
