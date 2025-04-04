const net = require('net');

function scanPort(host, port) {
    return new Promise((resolve) => {
        const socket = new net.Socket();
        let isOpen = false;

        socket.connect(port, host, () => {
            isOpen = true;
            socket.destroy();
            resolve({ port, isOpen });
        });

        socket.on('error', () => {
            resolve({ port, isOpen });
        });

        socket.setTimeout(200, () => {
            socket.destroy();
            resolve({ port, isOpen });
        });
    });
}

async function scanPorts(host, startPort, endPort) {
    console.log(`Scanning ports ${startPort}-${endPort} on ${host}...`);
    for (let port = startPort; port <= endPort; port++) {
        const { port: scannedPort, isOpen } = await scanPort(host, port);
        if (isOpen) {
            console.log(`Port ${scannedPort} is open.`);
        }
    }
    console.log('Scan complete.');
}

// Example: Scan ports 1-1024 on localhost
scanPorts('127.0.0.1', 1, 1024);