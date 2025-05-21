### Task: Simple API Calls and Save Results to JSON Files

**Objective**: Practice making simple API calls to the OpenWeather API then save the JSON responses to local files for further analysis.

---

#### **Instructions**

1. **Sign Up for OpenWeather API**:
   - Go to the [OpenWeather API website](https://openweathermap.org/api) and create a free account.
   - Generate your API key from your account dashboard.

2. **Set Up**:
   - **Browser**: Use your browser to make GET requests by entering the full URL with query parameters.
   - **POSTMAN**:
     - Install POSTMAN from [here](https://www.postman.com/downloads/).
     - Create a new GET request.

### Task Details

#### Part 1: Fetch Current Weather Data for Multiple Cities
1. **Endpoint**:  
   Use the **Current Weather Data** API:  
   ```
   https://api.openweathermap.org/data/2.5/weather
   ```

2. **Parameters**:  
   Pass the following query parameters:
   - `q` (City name): Add at least 3 cities (e.g., London, Paris, New York).
   - `appid` (Your API key)
   - `units` (Optional: Set to `metric` for temperatures in Celsius)

   **Example URL for London**:  
   ```
   https://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_API_KEY&units=metric
   ```

3. **Save Results**:
   - Save the JSON response for each city into a separate file named `cityname_weather.json`.
     - Example: `london_weather.json`, `paris_weather.json`, `newyork_weather.json`.

---

#### Part 2: Fetch 5-Day/3-Hour Weather Forecast for a Specific City
1. **Endpoint**:  
   Use the **5-Day/3-Hour Forecast** API:  
   ```
   https://api.openweathermap.org/data/2.5/forecast
   ```

2. **Parameters**:  
   Pass the following query parameters:
   - `q` (City name): Choose one city of your choice.
   - `appid` (Your API key)
   - `units` (Optional: Set to `metric` for temperatures in Celsius)

   **Example URL for New York**:  
   ```
   https://api.openweathermap.org/data/2.5/forecast?q=New York&appid=YOUR_API_KEY&units=metric
   ```

3. **Save Results**:
   - Save the JSON response into a file named `cityname_forecast.json`.  
     - Example: `newyork_forecast.json`.

---

### Steps for POSTMAN Users
1. **Create a Request**:
   - Open POSTMAN and create a new GET request.
   - Paste the API URL with parameters (e.g., `https://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_API_KEY&units=metric`).
2. **Send Request**:
   - Click the **Send** button to get the response.
3. **Save the Response**:
   - Click on the **Save Response** dropdown in the response section.
   - Choose "Download" to save the response as a JSON file.

---

### Steps for Browser Users
1. **Open API URL**:
   - Paste the full URL with query parameters (e.g., `https://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_API_KEY&units=metric`) into your browser's address bar.
2. **View the JSON Response**:
   - The browser will display the JSON response directly.
3. **Save the JSON**:
   - Copy the JSON response into a text editor and save it as a `.json` file with an appropriate name.

---

### Submission
- Submit the saved JSON files:
  - `cityname_weather.json` for each city.
  - `cityname_forecast.json` for the 5-day forecast.
- Add a self-reflection text that explains your understanding of these topics.

---
self reflection

there are several stages in experiment of scanning the weather pre-test in particular city using the API key from the weather API and testing with the postman application. there several results obtained from the process including (coordinate points, weather conditions, location base, wind speed, temperature, humidity, rain, clouds and time zone).

### Grading Criteria (Total: 10 Points)
1. Part 1: Fetch Current Weather Data for Multiple Cities (2 points)
2. Part 2: Fetch 5-Day/3-Hour Weather Forecast for a Specific City (2 points)
3. Successfully saved to file (2 points)
4. Screenshot of the implementation using POSTMAN (2 points)
5. Self-reflection (2 points)
