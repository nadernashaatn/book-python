Socket
======


``socket``
-------------------------------------------------------------------------------
.. figure:: img/socket-flow.jpg

    Socket Flow

Protocols
---------
* IPv4 - ``socket.AF_INET``
* IPv6 - ``socket.AF_INET6``
* UDP - ``socket.SOCK_DGRAM``
* TCP - ``socket.SOCK_STREAM``
* Broadcast - ``socket.SO_BROADCAST``

API
---
* The ``bufsize`` argument of 1024 used above is the maximum amount of data to be received at once
* ``accept()``, ``connect()``, ``send()``, and ``recv()`` are blocking
* Blocking calls have to wait on system calls (I/O) to complete before they can return a value

.. csv-table:: API
    :header-rows: 1

    "Method", "Description"
    "``socket()``", ""
    "``bind()``", ""
    "``listen()``", ""
    "``accept()``", ""
    "``connect()``", ""
    "``connect_ex()``", ""
    "``send()``", ""
    "``recv()``", ""
    "``close()``", ""

TCP
---
Server:

.. literalinclude:: src/socket-tcp-server.py
    :language: python
    :caption: ``socket`` TCP Server

Client:

.. literalinclude:: src/socket-tcp-client.py
    :language: python
    :caption: ``socket`` TCP Client

UDP
---
Server:

.. literalinclude:: src/socket-udp-server.py
    :language: python
    :caption: ``socket`` UDP Server

Client:

.. literalinclude:: src/socket-udp-client.py
    :language: python
    :caption: ``socket`` UDP Client

Multicast
---------
.. literalinclude:: src/socket-multicast.py
    :language: python
    :caption: ``socket`` Multicast Client


``socketserver``
-------------------------------------------------------------------------------

TCP
---

Server:

.. literalinclude:: src/socketserver-tcp-server.py
    :language: python
    :caption: ``socketserver`` TCP Server

Client:

.. literalinclude:: src/socket-tcp-client.py
    :language: python
    :caption: ``socket`` TCP Client


Asynchronous
------------

Threaded:
    * ``socketserver.ThreadingTCPServer``
    * ``socketserver.ThreadingUDPServer``

    .. literalinclude:: src/socketserver-tcp-threaded.py
        :language: python
        :caption: ``socketserver`` TCP Threaded Client

Forking:

    * ``socketserver.ForkingTCPServer``
    * ``socketserver.ForkingUDPServer``

    .. literalinclude:: src/socketserver-tcp-forking.py
        :language: python
        :caption: ``socketserver`` TCP Forking Client


References
-------------------------------------------------------------------------------
* https://realpython.com/python-sockets/


Assignments
-------------------------------------------------------------------------------
.. todo:: Convert assignments to literalinclude

Heartbeat
^^^^^^^^^
* Assignment: Heartbeat
* Complexity: medium
* Lines of code: 20 lines
* Time: 21 min

English:
    TODO: English Translation
    X. Run doctests - all must succeed

Polish:
    1. Stwórz klienta i serwer Heart Beat
    2. Zarówno klient jak i serwer ma być uruchamiany w wątkach
    3. Serwer ma przyjmować komunikaty UDP/IPv4 na porcie 1337
    4. Komunikacja ma odbywać się za pomocą protokołu JSON
    5. Klient ma mieć informację o swoim adresie IP i PORT
    6. Klient ma co 5 sekund wysyłać informację do serwera o swoim IP i PORT
    7. Wypisz:

        a. datę UTC przyjścia pakietu,
        b. IP i PORT przesłany przez klienta.

    8. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * ``threading.Timer(frequency: int, fn: Callable).start()``
    * ``socket.socket(socket.AF_INET, socket.SOCK_DGRAM)``
    * ``socketserver.ThreadingUDPServer``

Backdoor
^^^^^^^^
* Assignment: Backdoor
* Complexity: medium
* Lines of code: 150 lines
* Time: 34 min

English:
    TODO: English Translation
    X. Run doctests - all must succeed

Polish:
    1. Stwórz uruchamiany w wątku serwer TCP
    2. Serwer ma być uruchamiany na losowym porcie z przedziału 1025-65535 (dlaczego taki zakres portów?)
    3. Wyciągnij informację o adresie IP i PORT na którym nasłuchuje serwer
    4. Serwer oczekuje na komunikaty w formacie JSON:

        a. ``date: datetime`` (UTC),
        b. ``command: str``,
        c. ``timeout: int``.

    5. Serwer wykonuje polecenie zapisane w ``command`` w systemie operacyjnym uwzględniając ``timeout``
    6. Prześlij nadawcy JSON z wynikiem wykonania polecenia, tj.:

        a. ``date: datetime`` (UTC),
        b. ``host: str``,
        c. ``port: int``,
        d. ``stdout: str``,
        e. ``stderr: str``,
        f. ``exit_code: int``

    7. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * ``random.randint()``
    * ``socket.socket(socket.AF_INET, socket.SOCK_STREAM)``
    * ``socketserver.ThreadingTCPServer``
    * ``subprocess.run(cmd: str, timeout: int, shell: bool = True)``
    * ``json.dumps(obj: Any)``
    * ``json.loads(s: str)``
