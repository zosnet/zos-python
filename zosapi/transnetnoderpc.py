import re
import sys
import threading
import websocket
import ssl
import json
import time
from itertools import cycle
from grapheneapi.graphenewsrpc import GrapheneWebsocketRPC
from zosbase.chains import known_chains
from . import exceptions
import logging
log = logging.getLogger(__name__)


ZOS_ENABLE = True

class NumRetriesReached(Exception):
    pass


class TransnetNodeRPC(GrapheneWebsocketRPC):

    def __init__(self, *args, **kwargs):
        super(TransnetNodeRPC, self).__init__(*args, **kwargs)
        self.chain_params = self.get_network()

    @property
    def chain_params(self):
        return self._chain_params

    @chain_params.setter
    def chain_params(self, val):
        self._chain_params = val

    def register_apis(self):
        self.api_id["database"] = self.database(api_id=1)
        self.api_id["history"] = self.history(api_id=1)
        self.api_id["network_broadcast"] = self.network_broadcast(api_id=1)

        if ZOS_ENABLE:
            try:
                self.api_id["bitlender"] = self.bitlender(api_id=1)
                self.api_id["admin"] = self.admin(api_id=1)
                self.api_id["mobile"] = self.mobile(api_id=1)
            except Exception as e:
                print("bitlender exception, not zos chain")

    def rpcexec(self, payload):
        """ Execute a call by sending the payload.
            It makes use of the GrapheneRPC library.
            In here, we mostly deal with Transnet specific error handling

            :param json payload: Payload data
            :raises ValueError: if the server does not respond in proper JSON format
            :raises RPCError: if the server returns an error
        """
        # print(payload)
        try:
            # Forward call to GrapheneWebsocketRPC and catch+evaluate errors
            return super(TransnetNodeRPC, self).rpcexec(payload)
        except exceptions.RPCError as e:
            msg = exceptions.decodeRPCErrorMsg(e).strip()
            if msg == "missing required active authority":
                raise exceptions.MissingRequiredActiveAuthority
            elif re.match("^no method with name.*", msg):
                raise exceptions.NoMethodWithName(msg)
            elif msg:
                raise exceptions.UnhandledRPCError(msg)
            else:
                raise e
        except Exception as e:
            raise e

    def get_account(self, name, **kwargs):
        """ Get full account details from account name or id

            :param str name: Account name or account id
        """
        if len(name.split(".")) == 3:
            return self.get_objects([name])[0]
        else:
            return self.get_account_by_name(name, **kwargs)

    def get_asset(self, name, **kwargs):
        """ Get full asset from name of id

            :param str name: Symbol name or asset id (e.g. 1.3.0)
        """
        if len(name.split(".")) == 3:
            return self.get_objects([name], **kwargs)[0]
        else:
            return self.lookup_asset_symbols([name], **kwargs)[0]

    def get_object(self, o, **kwargs):
        """ Get object with id ``o``

            :param str o: Full object id
        """
        return self.get_objects([o], **kwargs)[0]

    def get_network(self):
        """ Identify the connected network. This call returns a
            dictionary with keys chain_id, core_symbol and prefix
        """
        props = self.get_chain_properties()
        #print(props)
        chain_id = props["chain_id"]
        for k, v in known_chains.items():
            # print(v)
            if v["chain_id"] == chain_id:
                return v

        # 找不到的链全当作ZOS链
        print("Can't find chain_id, used ZOS")
        return {"chain_id": props["chain_id"], "core_symbol": "ZOS", "prefix": "ZOS"}
        # raise("Connecting to unknown network!")
        # self.chain_params = {"chain_id": props["chain_id"], "core_symbol": "ZOS", "prefix": "ZOS"}
