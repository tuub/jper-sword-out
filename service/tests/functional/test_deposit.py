from unittest import TestCase
from service import deposit, models
from service.tests import fixtures
from octopus.modules.jper import models as jper
from octopus.modules.store import store
from octopus.core import app
from lxml import etree

# NOTE: you need to be running a SWORD server for these tests to operate.
# Recommend just starting an instance of SSS, then picking a collection
# and sticking it here:

COL = "http://localhost:8080/col-uri/4d410b73-39ff-4088-8409-ebe89dc7ff2f"
ERR_COL = "http://localhost:8080/col-uri/thisdoesntexist"
UN = "sword"
PW = "sword"

PACKAGING = "http://purl.org/net/sword/package/SimpleZip"

class TestDeposit(TestCase):
    def setUp(self):
        super(TestDeposit, self).setUp()
        self.stored = []
        self.store_impl = app.config.get("STORE_IMPL")
        app.config["STORE_IMPL"] = "octopus.modules.store.store.TempStore"

    def tearDown(self):
        super(TestDeposit, self).tearDown()
        sm = store.StoreFactory.get()
        for s in self.stored:
            sm.delete(s)
        app.config["STORE_IMPL"] = self.store_impl

    def test_01_metadata_deposit_success(self):
        note = jper.OutgoingNotification(fixtures.NotificationFactory.outgoing_notification())

        acc = models.Account()
        acc.add_sword_credentials(UN, PW, COL)

        deposit_record = models.DepositRecord()
        deposit_record.id = deposit_record.makeid()
        self.stored.append(deposit_record.id)

        receipt = deposit.metadata_deposit(note, acc, deposit_record, complete=True)

        assert receipt is not None
        # check the properties of the deposit_record
        assert deposit_record.metadata_status == "deposited"

        # check that a copy has been kept in the local store
        sm = store.StoreFactory.get()
        assert sm.exists(deposit_record.id)
        files = sm.list(deposit_record.id)
        assert len(files) == 2
        assert "metadata_deposit_response.xml" in files
        assert "metadata_deposit.txt" in files
        f = sm.get(deposit_record.id, "metadata_deposit_response.xml")
        xml = etree.parse(f)
        assert xml is not None

    def test_02_metadata_deposit_fail(self):
        note = jper.OutgoingNotification(fixtures.NotificationFactory.outgoing_notification())

        acc = models.Account()
        acc.add_sword_credentials(UN, PW, ERR_COL)

        deposit_record = models.DepositRecord()
        deposit_record.id = deposit_record.makeid()
        self.stored.append(deposit_record.id)

        with self.assertRaises(deposit.DepositException):
            deposit.metadata_deposit(note, acc, deposit_record, complete=True)

        # check the properties of the deposit_record
        assert deposit_record.metadata_status == "failed"

        # check that a copy has been kept in the local store
        sm = store.StoreFactory.get()
        assert sm.exists(deposit_record.id)
        files = sm.list(deposit_record.id)
        assert len(files) == 1
        assert "metadata_deposit.txt" in files

    def test_03_content_deposit_success(self):
        # first do a successful metadata deposit
        note = jper.OutgoingNotification(fixtures.NotificationFactory.outgoing_notification())

        acc = models.Account()
        acc.add_sword_credentials(UN, PW, COL)

        deposit_record = models.DepositRecord()
        deposit_record.id = deposit_record.makeid()
        self.stored.append(deposit_record.id)

        receipt = deposit.metadata_deposit(note, acc, deposit_record, complete=False)

        path = fixtures.NotificationFactory.example_package_path()
        with open(path) as f:
            deposit.package_deposit(receipt, f, PACKAGING, acc, deposit_record)

        # check the properties of the deposit_record
        assert deposit_record.metadata_status == "deposited"
        assert deposit_record.content_status == "deposited"

        # check that a copy has been kept in the local store
        sm = store.StoreFactory.get()
        assert sm.exists(deposit_record.id)
        files = sm.list(deposit_record.id)
        assert len(files) == 3
        assert "metadata_deposit.txt" in files
        assert "content_deposit.txt" in files

    def test_04_content_deposit_fail(self):
        note = jper.OutgoingNotification(fixtures.NotificationFactory.outgoing_notification())

        # first a successful deposit of metadata
        acc = models.Account()
        acc.add_sword_credentials(UN, PW, COL)

        deposit_record = models.DepositRecord()
        deposit_record.id = deposit_record.makeid()
        self.stored.append(deposit_record.id)

        receipt = deposit.metadata_deposit(note, acc, deposit_record, complete=False)

        # now mess with the receipt to generate a failure
        em = receipt.edit_media
        bits = em.split("/")
        bits[len(bits) - 1] = "randomobjectidentifier"
        receipt.edit_media = "/".join(bits)

        path = fixtures.NotificationFactory.example_package_path()
        with open(path) as f:
            with self.assertRaises(deposit.DepositException):
                deposit.package_deposit(receipt, f, PACKAGING, acc, deposit_record)

        # check the properties of the deposit_record
        assert deposit_record.metadata_status == "deposited"
        assert deposit_record.content_status == "failed"

        # check that a copy has been kept in the local store
        sm = store.StoreFactory.get()
        assert sm.exists(deposit_record.id)
        files = sm.list(deposit_record.id)
        assert len(files) == 3
        assert "metadata_deposit.txt" in files
        assert "content_deposit.txt" in files