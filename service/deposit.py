import sword2
from service import xwalk, models
from octopus.modules.store import store
from StringIO import StringIO
from octopus.modules.swordv2 import client_http

class DepositException(Exception):
    pass

def metadata_deposit(note, acc, deposit_record, complete=False):
    # create a connection object
    conn = sword2.Connection(user_name=acc.sword_username, user_pass=acc.sword_password, error_response_raises_exceptions=False, http_impl=client_http.OctopusHttpLayer())

    # storage manager instance for use later
    sm = store.StoreFactory.get()

    # assemble the atom entry for deposit
    entry = sword2.Entry()
    xwalk.to_dc_rioxx(note, entry)

    # do the deposit
    receipt = conn.create(col_iri=acc.sword_collection, metadata_entry=entry, in_progress=not complete)

    # if the receipt has a dom object, store it (it may be a deposit receipt or an error)
    if receipt.dom is not None:
        content = receipt.to_xml()
        sm.store(deposit_record.id, "metadata_deposit_response.xml", source_stream=StringIO(content))

    # find out if this was an error document, and throw an error if so
    # (recording deposited/failed on the deposit_record along the way)
    if isinstance(receipt, sword2.Error_Document):
        deposit_record.metadata_status = "failed"
        msg = "Metadata deposit failed with status {x}".format(x=receipt.code)
        sm.store(deposit_record.id, "metadata_deposit.txt", source_stream=StringIO(msg))
        raise DepositException(msg)
    else:
        msg = "Metadata deposit was successful"
        sm.store(deposit_record.id, "metadata_deposit.txt", source_stream=StringIO(msg))
        deposit_record.metadata_status = "deposited"

    # if this wasn't an error document, then we have a legitimate response, but we need the deposit receipt
    # so get it explicitly, and store it
    if receipt.dom is None:
        dr = conn.get_deposit_receipt(receipt.edit)
        content = dr.to_xml()
        sm.store(deposit_record.id, "metadata_deposit_response.xml", source_stream=StringIO(content))

    return