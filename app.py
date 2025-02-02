from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
import shutil
import time
from flask import jsonify


app = Flask(__name__)



# Configure upload folder (use tmp directory for Heroku)
UPLOAD_FOLDER = os.path.join(app.instance_path, 'uploads')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Home route
@app.route('/')
def index():
    return render_template('index2.html')

# Upload route
@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Save the file properly
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    # Wait for the file to be completely written (optional but useful)
    time.sleep(1)

    return jsonify({"filename": file.filename})


# Video processing route (for duplication in this case)
@app.route('/process_video/<filename>', methods=['GET'])
def process_video(filename):
    # Simulate video processing (e.g., creating a duplicate)
    original_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    # Create a duplicate by copying the original video
    timestamp = int(time.time())  # To ensure a unique filename
    duplicate_filename = f"duplicate_{timestamp}_{filename}"
    duplicate_path = os.path.join(app.config['UPLOAD_FOLDER'], duplicate_filename)

    # Simulate processing (copying the video file)
    shutil.copy(original_path, duplicate_path)

    # After processing, return the filename of the duplicate to be used for download
    return jsonify({"status": "complete", "filename": duplicate_filename})


# Route to serve uploaded files (both original and duplicate)
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)