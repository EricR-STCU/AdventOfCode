with open('./day16.txt') as f:
    data = f.read().strip()

X = ''.join(str(bin(int(c, 16)))[2:].zfill(4) for c in data)

class Literal():
    def __init__(self, packet):
        self.value, self.length = literal(packet)
        self.header = packet[:6]
    
    def version(self):
        return version_num(self)

class Packet1():
    def __init__(self, packet):
        self.sub_packets = []
        self.header = packet[:6]
        subs = self.size(packet)
        packet = packet[7+11:]
        for _ in range(subs):
            p = parse(packet)
            self.sub_packets.append(p)
            packet = packet[p.length:]
        self.length = 7 + 11 + sum(p.length for p in self.sub_packets)
    
    def size(self, packet):
        return int(packet[7:7+11], 2)

    def version(self):
        return version_num(self) + sum(p.version() for p in self.sub_packets)


class Packet0():
    def __init__(self, packet):
        self.sub_packets = []
        self.header = packet[:6]
        self.length = self.size(packet) + 7 + 15
        packet = packet[7+15:self.length]
        while len(packet) > 6:
            p = parse(packet)
            self.sub_packets.append(p)
            packet = packet[p.length:]
            
    def size(self, packet):
        return int(packet[7:7+15], 2)

    def version(self):
        return version_num(self) + sum(p.version() for p in self.sub_packets)
        
def compute(packet):
    t = type_id(packet.header)
    if t == 0:
        return sum(compute(p) for p in packet.sub_packets)
    elif t == 1:
        prod = 1
        for p in packet.sub_packets:
            prod *= compute(p)
        return prod
    elif t == 2:
        return min(compute(p) for p in packet.sub_packets)
    elif t == 3:
        return max(compute(p) for p in packet.sub_packets)
    elif t == 4:
        return packet.value
    elif t == 5:
        return 1 if compute(packet.sub_packets[0]) > compute(packet.sub_packets[1]) else 0
    elif t == 6:
        return 1 if compute(packet.sub_packets[0]) < compute(packet.sub_packets[1]) else 0
    elif t == 7:
        return 1 if compute(packet.sub_packets[0]) == compute(packet.sub_packets[1]) else 0

def parse(packet):
    t = type_id(packet)
    i = I(packet)
    if t == 4:
        return Literal(packet)
    elif i == 1:
        return Packet1(packet)
    elif i == 0:
        return Packet0(packet)
    print('oops')

def version_num(packet):
    return int(packet.header[:3], 2)

def type_id(packet):
    return int(packet[3:6], 2)

def I(packet):
    return int(packet[6])

def literal(packet):
    i = 6
    bits = packet[i+1:i+5]
    while int(packet[i]):
        i += 5
        bits += packet[i+1:i+5]
    return (int(bits, 2), i + 5)

def size(i, packet):
    return int(packet[7:7+11] if i else packet[7:7+15], 2)

def part1():
    P = parse(X)
    return P.version()

def part2():
    return compute(parse(X))


print(part1())
print(part2())