from octopus.modules.es import dao
from octopus.core import app

class AccountDAO(dao.ESDAO):
    __type__ = "account"

    @classmethod
    def with_sword_activated(cls):
        q = SwordAccountQuery()
        all = []
        for acc in cls.scroll(q=q.query()):
            all.append(acc)             # we need to do this because of the scroll keep-alive
        return all

class SwordAccountQuery(object):
    def __init__(self):
        pass

    def query(self):
        return {
            "query" : {
                "query_string" : {
                    "query" : "_exists_:sword_repository.collection"
                }
            }
        }