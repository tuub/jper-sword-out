from octopus.modules.es.testindex import ESTestCase
from service import models
from service.tests import fixtures
from octopus.lib import dataobj

class TestModels(ESTestCase):
    def setUp(self):
        super(TestModels, self).setUp()

    def tearDown(self):
        super(TestModels, self).tearDown()

    def test_01_account(self):
        # first load some accounts into the system, some with and some without sword support
        acc1 = models.Account()
        acc1.add_sword_credentials("acc1", "pass1", "http://sword/1")
        acc1.save()

        acc2 = models.Account()
        acc2.add_sword_credentials("acc2", "pass2", "http://sword/2")
        acc2.save()

        acc3 = models.Account()
        acc3.save()

        acc4 = models.Account()
        acc4.save(blocking=True)

        accs = models.Account.with_sword_activated()
        assert len(accs) == 2
        for acc in accs:
            assert acc.sword_collection in ["http://sword/1", "http://sword/2"]

    def test_02_repository_status(self):
        # make a blank one
        rs = models.RepositoryStatus()

        # test all its methods
        dataobj.test_dataobj(rs, fixtures.SwordFactory.repository_status_do_test())

        # make a new one around some existing data
        rs = models.RepositoryStatus(fixtures.SwordFactory.repository_status())

    def test_03_deposit_record(self):
        # make a blank one
        dr = models.DepositRecord()

        # test all its methods
        dataobj.test_dataobj(dr, fixtures.SwordFactory.deposit_record_do_test())

        # make a new one around some existing data
        dr = models.DepositRecord(fixtures.SwordFactory.deposit_record())