 <h1>Project Setup Instructions</h1>

  <h2>1. Setup Virtual Environment</h2>
  <pre>
python -m venv venv
venv\Scripts\activate   # For Windows
source venv/bin/activate   # For Linux/Mac
  </pre>

  <h2>2. Install Libraries and Dependencies</h2>
  <pre>
pip install -r requirements.txt
  </pre>

  <h2>3. Update requirements.txt</h2>
  <pre>
pip freeze > requirements.txt
  </pre>

  <h2>4. Database Connection</h2>
  <p>
    Create a <code>.env</code> file in the project root and add the following variables:
  </p>
  <pre>
DB_NAME=your_database_name
DB_PASSWORD=your_password
  </pre>

  <h2>5. How to Run the Project</h2>
  <p>After setting up everything, run the project with:</p>
  <pre>
python manage.py runserver   <!-- For Django -->
uvicorn main:app --reload    <!-- For FastAPI -->
  </pre>

  <h2>6. Notes</h2>
  <ul>
    <li>Always activate the virtual environment before running the project.</li>
    <li>Update <code>requirements.txt</code> if new dependencies are added.</li>
    <li>Do not commit <code>.env</code> or <code>venv</code> to version control.</li>
  </ul>
