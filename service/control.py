from service import models


def activate_deposit(acc_id):
    # see if there's a repository status for this account
    rs = models.RepositoryStatus.pull(acc_id)

    # if not make one
    if rs is None:
        rs = models.RepositoryStatus()
        rs.id = acc_id
        rs.status = "succeeding"
        rs.save()
        return

    # if there is, reset it ready to go again
    rs.activate()
    rs.save()

def deactivate_deposit(acc_id):
    # see if there's a repository status for this account
    rs = models.RepositoryStatus.pull(acc_id)

    # if not, that's as good as being deactivated
    if rs is None:
        return

    # if there is, deactivate it
    rs.deactivate()
    rs.save()