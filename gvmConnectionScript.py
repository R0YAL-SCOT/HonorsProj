#python3 -m pip install --user python-gvm

from gvm.connections import UnixSocketConnection
from gvm.protocols.gmp import Gmp
from gvm.transforms import EtreeTransform
from gvm.xml import pretty_print


def connection(gvmUser, gvmPass):
    connection = UnixSocketConnection()
    transform = EtreeTransform()

    with Gmp(connection, transform=transform) as gmp:
        # Retrieve GMP version supported by the remote daemon
        version = gmp.get_version()

        # Prints the XML in beautiful form
        pretty_print(version)

        # Login
        gmp.authenticate(gvmUser, gvmPass)

        # Retrieve all tasks
        tasks = gmp.get_tasks()
        gmp.get_scanner( 'vuln scan', '127.0.0.1', 9390, scanner_type=2 , credential_id='up')

        # Get names of tasks
        task_names = tasks.xpath('task/name/text()')
        pretty_print(task_names)


if __name__=="__main__":
    connection()