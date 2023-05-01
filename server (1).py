import socket

dns_table = {"www.instagram.com": "190.165.1.1",
             "www.udemy.com": "190.165.1.2",
             "www.deakin.edu.in": "190.165.1.3",
             "www.amazon.com": "190.165.1.4"}

cname_record = {"www.instagram.com": "host.instagram.com",
                "www.udemy.com": "host.udemy.com",
                "www.deakin.edu.in": "host.deakin.edu.in",
                "www.amazon.com": "host.amazon.com"}
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Server is running")
clientSocket.bind(("127.0.0.1", 1234))
while True:
    data, address = clientSocket.recvfrom(1024)
    message = format(address) + " request to fetch data "
    print(message)
    data = data.decode()
    ip = dns_table.get(data, "Data not found, check for errors").encode()
    cname = cname_record.get(data, "none").encode()
    send = clientSocket.sendto(ip, address)
    send1 = clientSocket.sendto(cname, address)
