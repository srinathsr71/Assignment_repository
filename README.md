
Assingnment Overview Steps:-
---

### Task 1: Handling POST Requests with JSON Data (Option 1)

#### Setup Instructions:
1. Install Python by using following steps:-
   - Visit the official Python website: [Python Downloads](https://www.python.org/downloads/).
   - Download the latest version of Python for Windows.
   - Run the installer.
   - Check the box that says "Add Python to Path" during installation.
   - Click "Install Now" and follow the prompts to complete the installation.

2. Install virtualenv by using following command:-
   
   ```
   pip install virtualenv
   ```

3. create a python virtual environment by using following command:-
   
   ```
   virtualenv venv
   ```

4. Activate virtual environment by using following path:-

   ```
   C:\Users\Admin\venv\Scripts\Activate.bat
   ```

5. Install python package Flask by using following command:-
   
   ```
   pip install Flask
   ```
6.Flask server running on the default url & portNo  is:-**http://127.0.0.1:5000**

#### Test Instruction Steps:
1. In `submit-json.py`, set up a Flask server with a route for `/submit-json` to handle POST requests.
2. Access and process JSON data using `request.json`.
3. Respond with appropriate status codes/messages.
4. Use `send_request.py` to pass JSON data to the Flask server at `/submit-json`.
5. In `send_request.py`, specify the local host URL: `http://localhost:5000/submit-json`.

#### Test Execution Steps:
1. Run the Flask server by executing `submit-json.py`.
2. Open a terminal and navigate to the directory containing `submit-json.py`.
3. Start the Flask server by using following command:-
   
   ```
   python submit-json.py
   ```
5. Once the server is running, open another terminal.
6. Navigate to the directory containing `send_request.py`.
7. Execute the script to send JSON data to the Flask server by using following command:-
   
   ```
   python send_request.py
   ```
8. Verify the server's response to the JSON data sent.

### Task 1: Handling POST Requests with JSON Data (Option 2)

#### Test Instruction Steps:
1. In `submit_json.py`, set up a Flask server with a route for `/submit-json` to handle POST requests.
2. Access and process JSON data using `request.json`.
3. Respond with appropriate status codes/messages.
4. Use `send_reqres.py` to pass JSON data to the Flask server at `/submit-json`.
5. In `send_request.py`, specify the localhost URL: `http://reqres/api/users`.

#### Test Execution Steps:
1. Run the Flask server by executing `submit_json.py`.
2. Open a terminal and navigate to the directory containing `submit_json.py`.
3. Start the Flask server by using following command:-
   
   ```
   python submit_json.py
   ```
4. Once the server is running, open another terminal.
5. Navigate to the directory containing `send_reqres.py`.
6. Execute the script to send JSON data to the Flask server by using following command:-
   
   ```
   python send_reqres.py
   ```
7. Verify the server's response to the JSON data sent.

### Task 2: Automation Testing for JSON Requests

#### Setup Instructions:
1. Install Robot Framework and requests library  by using following commands:-
   ```
   pip install robotframework
   pip install robotframework-requests
   ```

#### Test Instructions:
- Created test cases to validate JSON POST, GET, PATCH, DELETE requests handling.
- Covered scenarios like valid JSON data, invalid data, and valid status codes.

#### Test Execution:
1. Test cases were created in `Handling_requests.robot`.
2. Run the test  by using following command:-
   ```
   robot Handling_requests.robot
   ```
3. Review the automatically generated test report.

### Task 3: Basic Load Testing for JSON Requests

#### Setup Instructions:
1. Install Locust by using following command:-
   
   ```
   pip install locust
   ```

#### Test Instructions:
- Created Locust file `load_testing.py` to define scenarios and load testing parameters.
- Implemented sending POST requests with valid JSON payloads.

#### Test Execution:
1. Run `load_test.py` file by using following command:-
   
   ```
   locust -f load_test.py
   ```
2. Open Locust web interface at [http://localhost:8089].
3. Configure parameters like number of users, ramp up, host (`http://reqres.in/api/users`), and click Start.
4. Monitor test results to assess system response under load.
5. Download the report to see performance graphs and detailed performance report.

### Task 3.1: Load Testing for JSON Requests & Handling Form Data

#### Test Instructions:
- Created Locust file `load_test_json_form.py` to include scenarios for both form data and JSON data submissions.
- Defined scenarios for submitting form data with name and email fields, along with scenarios for submitting JSON data.
- Ensured correct handling of both form data and JSON data by the endpoint (`http://localhost:5000/submit-json`).
- Implemented sending POST requests with valid JSON and form payloads.

#### Test Execution:
1. Run the Flask server by executing `submit_json_form.py`.
2. Open a terminal and navigate to the directory containing `submit_json_form.py`.
3. Start the Flask server by using following command:-
   
   ```
   python submit_json_form.py
   ```
4. Once the server is running, open another terminal.
5. Navigate to the directory containing `load_test_json_form.py`.
6. Execute the script to send JSON data to Locust file `load_test_json_form.py` to Flask server by using following command:-
   
   ```
   locust -f load_test_json_form.py
   ```
7. Open the Locust web interface at [http://localhost:8089](http://localhost:8089).
8. Configure parameters like number of users, Ramp up,Host(http://localhost:5000) and click Start.
9. Monitor the test results to assess system response under load.
10. Download the report and see the performance graphs and detailed report of performance.
