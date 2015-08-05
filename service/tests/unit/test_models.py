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
