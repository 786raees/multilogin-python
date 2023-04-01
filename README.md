# Multilogin Python Client

A Python client for the Multilogin API, created by Waqar Khan.

This library provides an easy-to-use interface for interacting with the Multilogin API. You can manage and control browser profiles programmatically using the provided `MultiloginClient` class.

## Installation

To install the Multilogin Python Client, run the following command:

```bash
pip install multilogin-python
```

# Usage
Here's a simple example demonstrating how to use the MultiloginClient class:

```
from multilogin.client import MultiloginClient

# Replace this with your Multilogin API token
API_TOKEN = "your_api_token"

# Initialize the Multilogin client
client = MultiloginClient(API_TOKEN)

# Get a list of all profiles
profiles = client.get_all_profiles()
print("All profiles:", profiles)

# Get a profile by its ID
profile_id = "example_profile_id"
profile = client.get_profile_by_id(profile_id)
print(f"Profile with ID {profile_id}:", profile)
```

# Available Methods

The MultiloginClient class provides methods for the following Multilogin API endpoints:

`get_all_profiles()`
`get_profile_by_id(profile_id)`
`create_profile(profile_data)`
`update_profile(profile_id, profile_data)`
`delete_profile(profile_id)`
`start_profile(profile_id)`
`stop_profile(profile_id)`

Please refer to the Multilogin API documentation for more information on the available endpoints, required parameters, and expected responses.

# Contributing

Contributions are welcome! If you find a bug or have a feature request, please open an issue on the project's GitHub repository. If you'd like to contribute code, feel free to fork the repository, make your changes, and submit a pull request.

# License

This project is licensed under the MIT License.

