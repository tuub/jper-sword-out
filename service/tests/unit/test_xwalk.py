# from octopus.modules.es.testindex import ESTestCase
from unittest import TestCase
from service.tests import fixtures
import sword2
from service import xwalk
from octopus.modules.jper import models

TERMS = "http://purl.org/dc/terms/"
DC = "http://purl.org/dc/elements/"
ALI = "http://www.niso.org/schemas/ali/1.0/"
RIOXX = "http://www.rioxx.net/schema/v2.0/rioxx/"

class TestModels(TestCase):
    def setUp(self):
        super(TestModels, self).setUp()

    def tearDown(self):
        super(TestModels, self).tearDown()

    def test_01_xwalk(self):
        e = sword2.Entry()
        n = models.OutgoingNotification(fixtures.NotificationFactory.outgoing_notification())
        xwalk.to_dc_rioxx(n, e)

        def _texts(ns, field):
            return [el.text for el in e.entry.findall("{" + ns + "}" + field)]

        def _attr(ns, field, att):
            return [el.get(att) for el in e.entry.findall("{" + ns + "}" + field)]

        identifiers = _texts(DC, "identifier")
        assert len(identifiers) == 5

        assert "http://router.jisc.ac.uk/api/v1/notification/1234567890/content/1" in identifiers
        assert "http://router.jisc.ac.uk/api/v1/notification/1234567890/content/2" in identifiers
        assert "http://router.jisc.ac.uk/api/v1/notification/1234567890/content/SimpleZip" in identifiers
        assert "http://router.jisc.ac.uk/api/v1/notification/1234567890/content" in identifiers
        assert "doi:10.pp/jit.1" in identifiers

        available = _texts(TERMS, "available")
        assert len(available) == 1
        assert "2016-01-01T00:00:00Z" in available

        titles = _texts(DC, "title")
        assert len(titles) == 1
        assert "Test Article" in titles

        vers = _texts(RIOXX, "version")
        assert len(vers) == 1
        assert "AAM" in vers

        pubs = _texts(DC, "publisher")
        assert len(pubs) == 1
        assert "Premier Publisher" in pubs

        sources = _texts(DC, "source")
        assert len(sources) == 5
        assert "Journal of Important Things" in sources
        assert "issn:1234-5678" in sources
        assert "eissn:1234-5678" in sources
        assert "pissn:9876-5432" in sources
        assert "doi:10.pp/jit" in sources

        vor = _texts(RIOXX, "version_of_record")
        assert len(vor) == 1
        assert "doi:10.pp/jit.1" in vor

        type = _texts(DC, "type")
        assert len(type) == 1
        assert "article" in type

        creator = _texts(DC, "creator")
        assert len(creator) == 6
        assert "Richard Jones" in creator
        assert "orcid:aaaa-0000-1111-bbbb" in creator
        assert "email:richard@example.com" in creator
        assert "Mark MacGillivray" in creator
        assert "orcid:dddd-2222-3333-cccc" in creator
        assert "email:mark@example.com" in creator

        ra = _texts(RIOXX, "author")
        assert len(ra) == 2
        assert "Richard Jones" in ra
        assert "Mark MacGillivray" in ra

        ratts = _attr(RIOXX, "author", "id")
        assert len(ratts) == 2

        affs = _texts(DC, "contributor")
        assert len(affs) == 1
        assert "Cottage Labs" in affs

        langs = _texts(DC, "language")
        assert len(langs) == 1
        assert "eng" in langs

        pubd = _texts(DC, "date")
        assert len(pubd) == 1
        assert "2015-01-01T00:00:00Z" in pubd

        rpubd = _texts(RIOXX, "publication_date")
        assert len(rpubd) == 1
        assert "2015-01-01T00:00:00Z" in rpubd

        accd = _texts(TERMS, "dateAccepted")
        assert len(accd) == 1
        assert "2014-09-01T00:00:00Z" in accd

        subd = _texts(TERMS, "dateSubmitted")
        assert len(subd) == 1
        assert "2014-07-03T00:00:00Z" in subd

        licref = _texts(ALI, "license_ref")
        assert len(licref) == 1
        assert "http://creativecommons.org/cc-by" in licref

        startd = _attr(ALI, "license_ref", "start_date")
        assert len(startd) == 1
        assert "2016-01-01T00:00:00Z" in startd

        rights = _texts(DC, "rights")
        assert len(rights) == 1
        assert "http://creativecommons.org/cc-by" in rights

        projs = _texts(RIOXX, "project")
        assert len(projs) == 1
        assert "BB/34/juwef" in projs

        funders = _attr(RIOXX, "project", "funder_name")
        assert len(funders) == 1
        assert "BBSRC" in funders

        fids = _attr(RIOXX, "project", "funder_id")
        assert len(fids) == 1
        assert "ringold:bbsrcid" in fids

        subs = _texts(DC, "subject")
        assert len(subs) == 4









