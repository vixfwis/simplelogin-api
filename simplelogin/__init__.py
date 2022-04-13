from simplelogin.definitions import data as ddefs
from simplelogin.definitions import endpoints as eps
from simplelogin.client import BaseClient
from simplelogin import exceptions as exc


class SimpleLoginApi:
    def __init__(self, client: BaseClient, base_url: str = 'https://app.simplelogin.io'):
        self._client = client
        self._base_url = base_url

    def get_user_info(self) -> ddefs.UserInfo:
        return self._client.make_request(self._base_url, eps.GetUser())

    def get_alias_options(self, hostname: str = None) -> ddefs.AliasOptions:
        params = {
            'hostname': hostname,
        }
        return self._client.make_request(self._base_url, eps.GetAliasOptions(), params=params)

    def get_alias_list(self, page: int, pinned: bool = False) -> ddefs.AliasInfoList:
        params = {
            'page_id': page,
        }
        if pinned:
            params['pinned'] = True
        return self._client.make_request(self._base_url, eps.GetAliasList(), params=params)

    def create_random_alias(self, hostname: str = None, mode: str = None, note: str = None) -> ddefs.AliasInfo:
        """
        :param mode: either 'uuid' or 'word'
        """
        params = {
            'hostname': hostname,
            'mode': mode,
        }
        data = {
            'note': note,
        }
        return self._client.make_request(self._base_url, eps.CreateRandomAlias(), params=params, data=data)

    def create_custom_alias(self,
                            alias_prefix: str,
                            signed_suffix: str,
                            mailbox_ids: list[int],
                            hostname: str = None,
                            name: str = None,
                            note: str = None) -> ddefs.AliasInfo:
        params = {
            'hostname': hostname,
        }
        data = {
            'alias_prefix': alias_prefix,
            'signed_suffix': signed_suffix,
            'mailbox_ids': mailbox_ids,
            'note': note,
            'name': name,
        }
        return self._client.make_request(self._base_url, eps.CreateCustomAlias(), params=params, data=data)

    def update_alias(self,
                     alias_id: int,
                     note: str = None,
                     name: str = None,
                     mailbox_ids: list[int] = None,
                     disable_pgp: bool = None,
                     pinned: bool = None,
                     ):
        data = {
            'note': note,
            'name': name,
            'mailbox_ids': mailbox_ids,
            'disable_pgp': disable_pgp,
            'pinned': pinned,
        }
        return self._client.make_request(self._base_url, eps.UpdateAlias({'alias_id': alias_id}), data=data)

    def get_alias(self, alias_id: int) -> ddefs.AliasInfo:
        return self._client.make_request(self._base_url, eps.GetAlias({'alias_id': alias_id}))

    def delete_alias(self, alias_id: int) -> ddefs.DeleteAlias:
        return self._client.make_request(self._base_url, eps.DeleteAlias({'alias_id': alias_id}))

    def toggle_alias(self, alias_id: int) -> ddefs.ToggleAlias:
        return self._client.make_request(self._base_url, eps.ToggleAlias({'alias_id': alias_id}))
