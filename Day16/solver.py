import os
from typing import List, Optional, Tuple
import requests
import math


AOC_SESSION = os.environ['AOC_SESSION']


class Packet:
    def __init__(self, version: int, type: int, literal: str = '', subpackets: Optional[List['Packet']] = None):
        self.version = version
        self.type = type
        self.literal = literal
        self.subpackets = subpackets or []
    
    def sum_versions(self) -> int:
        return sum([self.version, *(sub.sum_versions() for sub in self.subpackets)])
    
    def calc_sub_packets(self) -> int:
        if self.type == 0:
            return sum(sub.calc_sub_packets() for sub in self.subpackets)
        elif self.type == 1:
            return math.prod(sub.calc_sub_packets() for sub in self.subpackets)
        elif self.type == 2:
            return min(sub.calc_sub_packets() for sub in self.subpackets)
        elif self.type == 3:
            return max(sub.calc_sub_packets() for sub in self.subpackets)
        elif self.type == 4:
            return int(self.literal, 2)
        elif self.type == 5:
            return int(self.subpackets[0].calc_sub_packets() > self.subpackets[1].calc_sub_packets())
        elif self.type == 6:
            return int(self.subpackets[0].calc_sub_packets() < self.subpackets[1].calc_sub_packets())
        else:
            return int(self.subpackets[0].calc_sub_packets() == self.subpackets[1].calc_sub_packets())
    
    @staticmethod
    def parse(bits: str) -> Tuple['Packet', str]:
        version, bits = int(bits[:3], 2), bits[3:]
        type_id, bits = int(bits[:3], 2), bits[3:]
        if type_id == 4:
            literal = ''
            while bits[0] != '0':
                literal, bits = literal + bits[1:5], bits[5:]
            literal, bits = literal + bits[1:5], bits[5:]

            return Packet(version, type_id, literal, subpackets=[]), bits

        subpackets: List[Packet] = []
        length_type_id, bits = bits[0], bits[1:]
        if length_type_id == '0':
            total_length, bits = int(bits[:15], 2), bits[15:]

            orig_length = len(bits)
            while (orig_length - len(bits)) < total_length:
                subpacket, bits = Packet.parse(bits)
                subpackets.append(subpacket)

            return Packet(version, type_id, subpackets=subpackets), bits
        else:
            count, bits = int(bits[:11], 2), bits[11:]
            for _ in range(count):
                subpacket, bits = Packet.parse(bits)
                subpackets.append(subpacket)

        return Packet(version, type_id, subpackets=subpackets), bits
    

def get_data() -> str:
    data : List[str] = requests.get('https://adventofcode.com/2021/day/16/input',
        cookies={'session': AOC_SESSION}).content.decode('utf-8').split('\n')[:-1]

    packets = ''.join(bin(int(char, 16))[2:].zfill(4) for char in data[0].strip())

    return packets


def solve_q1(packets: str):
    print(Packet.parse(packets)[0].sum_versions())


def solve_q2(packets: str):
    print(Packet.parse(packets)[0].calc_sub_packets())   


if __name__ == '__main__':
    data = get_data()    
    solve_q1(data)
    solve_q2(data)
