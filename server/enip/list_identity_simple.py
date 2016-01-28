
"""python -m cpppo.server.enip.list_identity_simple <hostname>

Returns any List Identity responses from the given hostname or IP address (default:
255.255.255.255), received before timeout (default: 1.0 second) expires.

"""

from __future__ import print_function

import sys

import cpppo
from cpppo.server import enip
from cpppo.server.enip import client

timeout			= 1.0
host			= sys.argv[1] if sys.argv[1:] else '255.255.255.255'
with client.client( host=host, udp=True, broadcast=True ) as conn:
    conn.list_identity( timeout=timeout )
    while conn.readable( timeout=timeout ):
        print( enip.enip_format( next( conn )))