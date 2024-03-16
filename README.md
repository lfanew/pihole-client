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

### Methods

The following sections detail the available methods in the `PiholeClient`.

#### `enable()`

Enables the Pihole filtering.

```python
client.enable()
```

#### `disable(seconds=0)`

Disables the Pihole filtering for a specified duration. If no duration is provided, filtering is disabled indefinitely.

```python
client.disable(300)  # Disables for 5 minutes
```

#### `check_updates()`

Checks for updates to the Pihole software.

```python
client.check_updates()
```

#### `set_temperature_unit(unit)`

Sets the temperature unit displayed in the Pihole interface. Valid units are `'c'`, `'f'`, and `'k'`.

```python
client.set_temperature_unit('f')
```

#### `add_to_list(list_type, domain)`

Adds a domain to one of the specified lists: `'black'`, `'regex_black'`, `'white'`, or `'regex_white'`.

```python
client.add_to_list('black', 'example.com')
```

#### `remove_from_list(list_type, domain)`

Removes a domain from one of the specified lists.

```python
client.remove_from_list('white', 'example.com')
```

#### `get_lists(list_type)`

Retrieves all domains in a specified list.

```python
domains = client.get_lists('black')
```

#### `get_custom_dns()`

Retrieves all custom DNS settings.

```python
custom_dns = client.get_custom_dns()
```

#### `add_custom_dns(domain, ip)`

Adds a custom DNS entry.

```python
client.add_custom_dns('example.com', '192.168.1.100')
```

#### `delete_custom_dns(domain, ip)`

Deletes a custom DNS entry.

```python
client.delete_custom_dns('example.com', '192.168.1.100')
```

#### `get_custom_cname()`

Retrieves all custom CNAME settings.

```python
custom_cname = client.get_custom_cname()
```

#### `add_custom_cname(domain, target)`

Adds a custom CNAME entry.

```python
client.add_custom_cname('portal.example.com', 'internal.example.com')
```

#### `delete_custom_cname(domain, target)`

Deletes a custom CNAME entry.

```python
client.delete_custom_cname('portal.example.com', 'internal.example.com')
```

## Error Handling

All methods are designed to raise an `HTTPError` if the API request fails for any reason. Ensure your code properly handles these exceptions.

## Contributing

Contributions to the Pihole API Wrapper are welcome! Please feel free to submit pull requests or report any issues you encounter.

## License

The Pihole API Wrapper is released under the MIT License. See the LICENSE file for more details.
