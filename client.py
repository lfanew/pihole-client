import requests

class PiholeClient:
    """
    A client for interacting with the Pihole API.
    
    Attributes:
        server_address (str): The address of the Pihole server.
        api_token (str, optional): The API token for authentication with the Pihole server.
    """

    def __init__(self, server_address, api_token=None):
        """
        Initializes the PiholeClient with a server address and an optional API token.

        Args:
            server_address (str): The address of the Pihole server. (e.g. http://192.168.0.5)
            api_token (str, optional): The API token for authentication. Default is None.
        """

        self.server_address = server_address
        self.api_token = api_token

    def _send_request(self, endpoint, params=None):
        """
        Sends a request to the Pihole server.

        Args:
            endpoint (str): The API endpoint to call.
            params (dict, optional): The query parameters to include in the request. Default is None.

        Returns:
            dict: The JSON response from the server.

        Raises:
            HTTPError: If the request fails for any reason.
        """

        if params is None:
            params = {}
        if self.api_token:
            params['auth'] = self.api_token
        response = requests.get(f"{self.server_address}/admin/api.php{endpoint}", params=params)
        response.raise_for_status()

        return response.json()

    def enable(self):
        """Enables the Pihole filtering."""
        return self._send_request('?enable')

    def disable(self, seconds=0):
        """
        Disables the Pihole filtering.

        Args:
            seconds (int, optional): The number of seconds to disable filtering. Default is 0 (indefinite).
        """

        return self._send_request('?disable', params={'disable': seconds})

    def check_updates(self):
        """Checks for updates to the Pihole software."""
        return self._send_request('?versions')

    def get_list(self, list_type):
        """
        Retrieves the domains in a specified list.

        Args:
            list_type (str): The type of list to retrieve ('black', 'regex_black', 'white', 'regex_white').
        
        Returns:
            list: The domains in the specified list.
        
        Raises:
            ValueError: If an invalid list type is specified.
        """

        if list_type not in ['black', 'regex_black', 'white', 'regex_white']:
            raise ValueError("Invalid list type")

        # Note: Actual parameter might vary based on Pi-hole's API implementation for this functionality.
        response = self._send_request('', params={'list': list_type, 'action': 'get_domains'})

        return response['data']

    def add_to_list(self, list_type, domain):
        """
        Adds a domain to a specified list.

        Args:
            list_type (str): The type of list to add to ('black', 'regex_black', 'white', 'regex_white').
            domain (str): The domain to add to the list.
        
        Raises:
            ValueError: If an invalid list type is specified.
        """

        if list_type not in ['black', 'regex_black', 'white', 'regex_white']:
            raise ValueError("Invalid list type")

        return self._send_request(f'?list={list_type}&add', params={'add': domain})

    def remove_from_list(self, list_type, domain):
        """
        Removes a domain from a specified list.

        Args:
            list_type (str): The type of list to remove from ('black', 'regex_black', 'white', 'regex_white').
            domain (str): The domain to remove from the list.
        
        Raises:
            ValueError: If an invalid list type is specified.
        """

        if list_type not in ['black', 'regex_black', 'white', 'regex_white']:
            raise ValueError("Invalid list type")

        return self._send_request(f'?list={list_type}&sub', params={'sub': domain})

    def get_custom_dns(self):
        """Retrieves custom DNS entries."""
        return self._send_request('?customdns&action=get')

    def add_custom_dns(self, domain, ip):
        """
        Adds a custom DNS entry.

        Args:
            domain (str): The domain for the DNS entry.
            ip (str): The IP address associated with the domain.
        """

        params = {
            'domain': domain,
            'ip': ip
        }

        return self._send_request('?customdns&action=add', params=params)

    def delete_custom_dns(self, domain, ip):
        """
        Deletes a custom DNS entry.

        Args:
            domain (str): The domain for the DNS entry to delete.
            ip (str): The IP address associated with the domain to delete.
        """

        params = {
            'domain': domain,
            'ip': ip
        }

        return self._send_request('?customdns&action=delete', params=params)

    def get_custom_cname(self):
        """Retrieves custom CNAME entries."""
        return self._send_request('?customcname&action=get')

    def add_custom_cname(self, domain, target):
        """
        Adds a custom CNAME entry.

        Args:
            domain (str): The domain for the CNAME entry.
            target (str): The target domain for the CNAME.
        """

        params = {
            'domain': domain,
            'target': target
        }

        return self._send_request('?customcname&action=add', params=params)

    def delete_custom_cname(self, domain, target):
        """
        Deletes a custom CNAME entry.

        Args:
            domain (str): The domain for the CNAME entry to delete.
            target (str): The target domain for the CNAME to delete.
        """

        params = {
            'domain': domain,
            'target': target
        }

        return self._send_request('?customcname&action=delete', params=params)

    def set_temperature_unit(self, unit):
        """
        Sets the temperature unit used in the Pihole interface.

        Args:
            unit (str): The temperature unit to set ('c', 'f', or 'k').
        
        Raises:
            ValueError: If an invalid temperature unit is specified.
        """

        if unit.lower() not in ['c', 'f', 'k']:
            raise ValueError("Invalid temperature unit")

        return self._send_request('?setTempUnit', params={'setTempUnit': unit.lower()})

