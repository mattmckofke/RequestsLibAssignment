### Practical Exercises 🧰

1. **Fetching Data from a Public API:**

   - **Task:** Write a Python script using the `requests` library to send a GET request to a public API (e.g., OpenWeatherMap, GitHub API).
   - **Objective:**
     - Retrieve data from the API.
     - Parse the JSON response.
     - Display specific information extracted from the data.
   - **Example:** Fetch the current weather data for a specific city and print the temperature and weather description.

2. **Creating and Updating Resources:**

   - **Task:** Use the `requests` library to interact with a mock RESTful API (e.g., [JSONPlaceholder](https://jsonplaceholder.typicode.com/)).
     - **Part A:** Send a POST request to create a new resource (e.g., a new post).
     - **Part B:** Send a PUT or PATCH request to update the resource you just created.
   - **Objective:**
     - Understand how to send data in the request body.
     - Handle the API's response to confirm the creation and update.

3. **Error Handling and Status Codes:**

   - **Task:** Modify your scripts to include error handling.
     - Check the response's `status_code`.
     - Use `try-except` blocks to catch exceptions (e.g., `requests.exceptions.HTTPError`, `requests.exceptions.ConnectionError`).
   - **Objective:**
     - Ensure your script can handle different HTTP status codes appropriately.
     - Provide meaningful error messages to the user.

4. **Implementing Timeouts and Retries:**

   - **Task:** Adjust your requests to include a timeout parameter and implement a retry mechanism for failed requests.
   - **Objective:**
     - Prevent your script from hanging indefinitely.
     - Handle transient network errors by retrying failed requests.
