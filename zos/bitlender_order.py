from zos.instance import shared_transnet_instance
from .blockchainobject import BlockchainObject
from .exceptions import BitlenderOrderNotFoundException


class Bitlender_Order(BlockchainObject):
    """ Read data about a witness in the chain

        :param str account_name: Name of the witness
        :param transnet transnet_instance: Transnet() instance to use when
               accesing a RPC

    """
    type_ids = 17

    def refresh(self):
        order = self.transnet.rpc.get_object(self.identifier)
        if not order:
            raise BitlenderOrderNotFoundException(self.identifier)
        super(Bitlender_Order, self).__init__(order, transnet_instance=self.transnet)

