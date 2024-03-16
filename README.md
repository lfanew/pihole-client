## Installation

Before using this Pihole API client, ensure you have Python and the `requests` library installed. You can install `requests` using pip:

```bash
pip install requests
```

or use the requirements file

```bash
pip install -r requirements.txt
```

## Usage

First, import the `PiholeClient` from the module:

```python
from pihole_client import PiholeClient
```

Then, create an instance of the `PiholeClient` by providing the address of your Pihole server and, optionally, your API token:

```python
client = PiholeClient('http://pi.hole', api_token='YourApiToken')
```

### Filtering Control

These methods are used to enable or disable the Pihole ad filtering.

#### `enable()`

Enables the Pihole filtering.

Example:
```python
client.enable()
```

#### `disable(seconds=0)`

Disables the Pihole filtering for a specified duration. If no duration is provided, filtering is disabled indefinitely.

Example:
```python
client.disable(300)  # Disables for 5 minutes
```

### Update Checks

This method checks for updates to the Pihole software.

#### `check_updates()`

Example:
```python
client.check_updates()
```

### Temperature Unit Setting

This method sets the temperature unit displayed in the Pihole interface.

#### `set_temperature_unit(unit)`

Valid units are `'c'`, `'f'`, and `'k'`.

Example:
```python
client.set_temperature_unit('f')
```

### List Management

These methods are used to add, remove, and retrieve domains from Pihole's various lists.

#### `add_to_list(list_type, domain)`

Adds a domain to one of the specified lists: `'black'`, `'regex_black'`, `'white'`, or `'regex_white'`.

Example:
```python
client.add_to_list('black', 'example.com')
```

#### `remove_from_list(list_type, domain)`

Removes a domain from one of the specified lists.

Example:
```python
client.remove_from_list('white', 'example.com')
```

#### `get_lists(list_type)`

Retrieves all domains in a specified list.

Example:
```python
domains = client.get_lists('black')
```

### Custom DNS Management

These methods are used to manage custom DNS settings, allowing for specific domain-to-IP address mappings.

#### `get_custom_dns()`

Retrieves all custom DNS settings.

Example:
```python
custom_dns = client.get_custom_dns()
```

#### `add_custom_dns(domain, ip)`

Adds a custom DNS entry.

Example:
```python
client.add_custom_dns('example.com', '192.168.1.100')
```

#### `delete_custom_dns(domain, ip)`

Deletes a custom DNS entry.

Example:
```python
client.delete_custom_dns('example.com', '192.168.1.100')
```

### Custom CNAME Management

These methods are used to manage custom CNAME records, facilitating domain aliasing within the network.

#### `get_custom_cname()`

Retrieves all custom CNAME settings.

Example:
```python
custom_cname = client.get_custom_cname()
```

#### `add_custom_cname(domain, target)`

Adds a custom CNAME entry.

Example:
```python
client.add_custom_cname('portal.example.com', 'internal.example.com')
```

#### `delete_custom_cname(domain, target)`

Deletes a custom CNAME entry.

Example:
```python
client.delete_custom_cname('portal.example.com', 'internal.example.com')
```

Each of these groups provides a coherent set of functionalities that you can use to manage your Pihole's behavior and settings effectively. Remember to handle any exceptions these methods may throw, especially when dealing with network or API issues.

## License

The software is released under the MIT License. See the LICENSE file for more details.
