<p align="center">

  <img src="./images/logo.png">

</p>

##

<h3>Godzilla</h3>

Godzilla is basically an HTTP Denial of Service attack that affects threaded servers. It works like this:

We start making lots of HTTP requests.

1. We send headers periodically (every ~15 seconds) to keep the connections open.

2. We never close the connection unless the server does so. If the server closes a connection, we create a new one keep doing the same thing.

3. This exhausts the servers thread pool and the server can't reply to other people.

### Installation 

- Just, Clone this repository -

```

$ git clone https://github.com/Dankshiku/Godzilla

```

- Change to cloned directory and run `python Godzilla.py` 

```

$ cd Godzilla

$ bash install.sh

$ python Godzilla.py

```

### Required Tools

`slowloris`

:Slowloris is a type of denial of service attack tool which allows a single machine to take down another machine's web server with minimal bandwidth and side effects on unrelated services and ports. Slowloris tries to keep many connections to the target web server open and hold them open as long as possible. 

### Screenshot

<p>

  <img src="./images/1.png">

</p>

### Find Me on :

<p align="left">

  <a href="https://github.com/Dankshiku" target="_blank"><img src="https://img.shields.io/badge/Github-Dankshiku-green?style=for-the-badge&logo=github"></a>

  <a href="https://www.instagram.com/Dankshiku" target="_blank"><img src="https://img.shields.io/badge/IG-%40Dankshiku-red?style=for-the-badge&logo=instagram"></a>

  <a href="https://m.me/Dankshiku" target="_blank"><img src="https://img.shields.io/badge/Chat-Messenger-blue?style=for-the-badge&logo=messenger"></a>

</p>

