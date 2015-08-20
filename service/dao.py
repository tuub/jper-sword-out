from octopus.modules.es import dao
from octopus.core import app

class RepositoryStatusDAO(dao.ESDAO):
    __type__ = "sword_repository_status"

class DepositRecordDAO(dao.ESDAO):
    __type__ = "sword_deposit_record"

    @classmethod
    def pull_by_ids(cls, notification_id, repository_id):
        q = DepositRecordQuery(notification_id, repository_id)
        obs = cls.object_query(q=q.query())
        if len(obs) > 0:
            return obs[0]

class DepositRecordQuery(object):
    def __init__(self, notification_id, repository_id):
        self.notification_id = notification_id
        self.repository_id = repository_id

    def query(self):
        return {
            "query" : {
                "bool" : {
                    "must" : [
                        {"term" : {"repository.exact" : self.repository_id}},
                        {"term" : {"notification.exact" : self.notification_id}}
                    ]
                }
            },
            "sort" : {"last_updated" : {"order" : "desc"}}
        }

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