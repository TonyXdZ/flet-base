# Flet-Base

This repository contains a basic Flet application built using the Flet-model module. It demonstrates core functionalities like:
![Flet-base app preview screenshots](https://raw.githubusercontent.com/TonyXdZ/flet-base/main/flet-base-preview.png?v=1)
- **User Authentication:**

    - Login page with username and password input fields.
    - Signup page with email, username, password, and confirm password fields.
    - Basic user authentication logic (replace with your own implementation).
    
    ***The app does not send any requests you will be redirected to Home page after you enter random username and password in Login page or random info in Sign up page***
    
- **Navigation in home page:**
 
    - Bottom navigation bar with Home, Messages, and Profile views.


**Getting Started**

1. **Clone the repository:**
   ```bash
   git clone git@github.com:TonyXdZ/flet-base.git
   ```

2. **Install dependencies:**

After activating your virtual environment :
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   flet run app.py 
   ```
# Network Utilities Documentation

## HTTP Request Builders

### `build_request(page, url, data=None, authenticated=True)`
Synchronous HTTP request handler with JWT authentication support.

**Parameters:**
| Parameter     | Type    | Description                                  |
|---------------|---------|----------------------------------------------|
| `page`        | `Page`  | Flet page object                             |
| `url`         | `str`   | Target endpoint URL                          |
| `data`        | `dict`  | POST data payload (optional)                 |
| `authenticated` | `bool` | Auto-inject JWT from storage (default: True) |

**Returns:**  
`requests.Response` object

**Usage:**
```python
# Unauthenticated GET request
response = build_request(page, 
  "https://api.example.com/protected", 
    authenticated=False)

if response.status_code == 200:
    print(response.json())

# Authenticated POST request
response = build_request(
    page, 
    "https://api.example.com/public",
    data={"key": "value"},
)
```

---

### `async_build_request(page, url, data=None, authenticated=True)`
Asynchronous HTTP client with enhanced error handling.

**Returns:**  
`dict` with structure:
```python
{
    'status': int,        # HTTP status code
    'data': dict,         # Parsed JSON response
    'headers': dict,      # Response headers
    'error': str (optional)  # Error message if any
}
```

**Special Features:**
- Automatic JSON response parsing
- Built-in error handling for:
  - Network failures
  - Invalid JSON responses
  - Timeouts

**Async Usage:**
```python
#GET request with authentication
async def fetch_data():
    response = await async_build_request(
        page,
        "https://api.example.com/async-data"
    )
    if response['status'] == 200:
        print(response['data'])
```

---

## Authentication Verification
Some times you might need to check authentication before you redirect or send requests
### `check_auth(page) -> bool`
Synchronous authentication validator.

**Flow:**
1. Checks for stored access token
2. Tests token against `TEST_URL` endpoint
3. Returns validation status

**Usage:**
```python
if check_auth(page):
    show_protected_content()
else:
    page.go("/login")
```

### `async_check_auth(page) -> bool`
Asynchronous version with full async stack.

**Typical Use Case:**
```python
async def load_protected_page():
    if await async_check_auth(page):
        await load_private_data()
    else:
        page.go("/login")
```

---

## Server Status Checks

### `check_server_connection(timeout: float = 5.0) -> bool`
Synchronous server reachability test.

**Implementation:**
```python
def check_server_connection(timeout=5.0):
    try:
        requests.get(TEST_URL, timeout=timeout)
        return True
    except RequestException:
        return False
```

### `async_check_server_connection(timeout: float = 5.0) -> bool`
Async server ping with aiohttp.

**Usage Example:**
```python
async def startup_check():
    if not await async_check_server_connection():
        show_connection_error()
```

---

## Configuration Notes

1. **Endpoint Configuration**  
   Set the `TEST_URL` at the top of utils.py to your actual authentication endpoint:
   ```python
   TEST_URL = "http://your-api.com/auth-check-endpoint"
   ```

2. **Response Handling**  
   For async requests, always check the response dictionary structure:
   ```python
   response = await async_build_request(...)
   if response['status'] == 200:
       handle_data(response['data'])
   elif 'error' in response:
       handle_error(response['error'])
   ```

3. **Error Types**  
   Common error sources:
   - `401 Unauthorized`: Invalid/missing JWT
   - `500` status: Network errors or invalid JSON
   - Timeout errors: Server unreachable

---

## Best Practices

1. **Use async versions** when:
   - Making multiple sequential requests
   - Handling large file uploads/downloads
   - Working in async Flet environments

2. **Sync versions** are suitable for:
   - Simple single requests
   - Background operations
   - Non-UI blocking tasks

3. **Token Management**  
   The functions automatically handle:
   - JWT retrieval from client storage
   - Bearer token header injection
   - Storage cleanup for invalid tokens
---

**Project Structure**

```
flet-base/
├── app.py             # Main application file
├── pages/
│   ├── login.py       # Login page view
│   ├── signup.py      # Signup page view
│   ├── home.py        # Home page view
└── ...                 # Other files 
```

**Contributing**

Contributions are welcome! Please feel free to fork this repository and submit pull requests.

**License**

This project is licensed under the [MIT License](https://tlo.mit.edu/resources/open-source-initiative).

**Note:**

This is a basic example. You should adapt and extend it to fit your specific needs. Consider adding features like:

- **Sending requests:** Requests using requests python module to your api enpoint to get data like JWT token for user and user data.
- **Error handling and user feedback:** Check if server is alive and user is connected and provide human readable errors.
- **Improved UI/UX:** Enhance the visual appeal and user experience.
- **Security measures:** Implement robust security measures to protect user data by using client encrypt and decrypt from flet.security before saving it to client storage.
