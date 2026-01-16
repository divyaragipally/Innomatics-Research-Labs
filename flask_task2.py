from flask import Flask, request, render_template
import re

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def regex_matcher():
    matches = []
    error = None
    count = 0

    if request.method == 'POST':
        test_string = request.form.get('test_string', '')
        pattern = request.form.get('regex_pattern', '')

        try:
            matches = re.findall(pattern, test_string)
            count = len(matches)   # ✅ COUNT
        except re.error as e:
            error = f"Invalid regex: {str(e)}"

    return render_template(
        'regex.html',
        matches=matches,
        count=count,
        error=error
    )

if __name__ == '__main__':
    app.run(debug=True)
