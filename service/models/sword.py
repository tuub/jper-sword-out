from octopus.lib import dataobj
from service import dao

class RepositoryStatus(dataobj.DataObj, dao.RepositoryStatusDAO):
    """
    {
        "id" : "<id of the repository account>",
        "last_updated" : "<date this record was last updated>",
        "created_date" : "<date this record was created>",

        "last_deposit_date" : "<date of analysed date of last deposited notification>",
        "status" : "<succeeding|failing>"
    }
    """
    def __init__(self, raw=None):
        struct = {
            "fields" : {
                "id" : {"coerce" : "unicode"},
                "last_updated" : {"coerce" : "utcdatetime"},
                "created_date" : {"coerce" : "utcdatetime"},
                "last_deposit_date" : {"coerce" : "utcdatetime"},
                "status" : {"coerce" : "unicode"},
            }
        }

        self._add_struct(struct)
        super(RepositoryStatus, self).__init__(raw=raw)

    @property
    def last_deposit_date(self):
        return self._get_single("last_deposit_date", coerce=dataobj.date_str())

    @last_deposit_date.setter
    def last_deposit_date(self, val):
        self._set_single("last_deposit_date", val, coerce=dataobj.date_str())

    @property
    def status(self):
        return self._get_single("status", coerce=dataobj.to_unicode())

    @status.setter
    def status(self, val):
        self._set_single("status", val, coerce=dataobj.to_unicode(), allowed_values=[u"succeeding", u"failing"])


class DepositRecord(dataobj.DataObj, dao.DepositRecordDAO):
    """
    {
        "id" : "<opaque id of the deposit - also used as the local store id for the response content>",
        "last_updated" : "<date this record was last updated>",
        "created_date" : "<date this record was created>",

        "repository" : "<account id of the repository>",
        "deposit_date" : "<date of attempted deposit>",
        "metadata_status" : "<deposited|failed>",
        "content_status" : "<deposited|none|failed>",
        "completed_status" : "<deposited|none|failed>"
    }
    """
    def __init__(self, raw=None):
        struct = {
            "fields" : {
                "id" : {"coerce" : "unicode"},
                "last_updated" : {"coerce" : "utcdatetime"},
                "created_date" : {"coerce" : "utcdatetime"},
                "repository" : {"coerce" : "unicode"},
                "deposit_date" : {"coerce" : "utcdatetime"},
                "metadata_status" : {"coerce" : "unicode"},
                "content_status" : {"coerce" : "unicode"},
                "completed_status" : {"coerce" : "unicode"},
            }
        }

        self._add_struct(struct)
        super(DepositRecord, self).__init__(raw=raw)

    @property
    def repository(self):
        return self._get_single("repository", coerce=dataobj.to_unicode())

    @repository.setter
    def repository(self, val):
        self._set_single("repository", val, coerce=dataobj.to_unicode())

    @property
    def deposit_date(self):
        return self._get_single("deposit_date", coerce=dataobj.to_unicode())

    @deposit_date.setter
    def deposit_date(self, val):
        self._set_single("deposit_date", val, coerce=dataobj.to_unicode())

    @property
    def metadata_status(self):
        return self._get_single("metadata_status", coerce=dataobj.to_unicode())

    @metadata_status.setter
    def metadata_status(self, val):
        self._set_single("metadata_status", val, coerce=dataobj.to_unicode(), allowed_values=[u"deposited", u"failed"])

    @property
    def content_status(self):
        return self._get_single("content_status", coerce=dataobj.to_unicode())

    @content_status.setter
    def content_status(self, val):
        self._set_single("content_status", val, coerce=dataobj.to_unicode(), allowed_values=[u"deposited", u"none", u"failed"])

    @property
    def completed_status(self):
        return self._get_single("completed_status", coerce=dataobj.to_unicode())

    @completed_status.setter
    def completed_status(self, val):
        self._set_single("completed_status", val, coerce=dataobj.to_unicode(), allowed_values=[u"deposited", u"none", u"failed"])
