from flask import Flask, request, send_file, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_readme', methods=['POST'])
def generate_readme():
    data = request.json
    repo_link = data['repoLink']
    sections = data['sections']
    
    # Dummy data for illustration; fetch and process real data from GitHub
    description = "Project description from GitHub."
    installation = "Installation instructions from GitHub."
    usage = "Usage instructions from GitHub."
    contributing = "Contribution guidelines from GitHub."
    license_info = "License information from GitHub."

    content = "# Project Title\n\n"

    if 'description' in sections:
        content += f"## Description\n{description}\n\n"
    if 'installation' in sections:
        content += f"## Installation\n{installation}\n\n"
    if 'usage' in sections:
        content += f"## Usage\n{usage}\n\n"
    if 'contributing' in sections:
        content += f"## Contributing\n{contributing}\n\n"
    if 'license' in sections:
        content += f"## License\n{license_info}\n"

    with open('README.md', 'w') as file:
        file.write(content)

    return send_file('README.md', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
