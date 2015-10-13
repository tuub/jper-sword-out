# Controlling the SWORDv2 depositor

Repository accounts can have their sword deposit process activated and deactivated from the command line.

In the event that a repository repeatedly fails to accept a deposit, eventually their account will be disabled.  After
that point, in order to start receiving deposits again their account will need to be manually re-activated.

This can be done with:

    python service/scripts/activate.py -r [account id] -a

After that, their deposits will pick up from the last successfully deposited notification.

To deactivate an account, you can do:

    python service/scripts/activate.py -r [account id] -s
