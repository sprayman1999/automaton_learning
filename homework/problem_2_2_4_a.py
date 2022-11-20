#!/usr/bin/python3
import copy
import sys
import random
class DFA():
    def __init__(self,state_set,alpha_set,transfer_map,start_state,accept_set):
        self.state_set = state_set
        self.alpha_set = alpha_set
        self.transfer_map = transfer_map
        self.start_state = start_state
        self.accept_set = accept_set
    def run(self,string) -> bool:
        state_set = copy.copy(self.state_set)
        alpha_set = copy.copy(self.alpha_set)
        transfer_map = copy.copy(self.transfer_map)
        start_state = copy.copy(self.start_state)
        accept_set = copy.copy(self.accept_set)
        now_state = start_state
        for ch in string:
            if ch not in alpha_set:
                raise Exception(f"\"{ch}\" not in alpha_set. the alpha_set's value is {alpha_set}.")
            if ch not in transfer_map[now_state]:
                raise Exception(f"\"{ch}\" not in transfer_map[\'{now_state}\']. the map value is {transfer_map[now_state]}.")
            now_state = transfer_map[now_state][ch]
        if now_state not in accept_set:
            return False
        else:
            return True

dfa = DFA(
    {"S","A","B","C"},
    {"0","1"},
    {
        "S": {
            "1":"A",
            "0":"B",
        },
        "A": {
            "1":"A",
            "0":"B",
        },
        "B": {
            "1": "A",
            "0": "C",
        },
        "C": {
            "0":"C",
            "1": "A",
        }
    },
    "S",
    {"C"}
)

def test():
    for i in range(10):
        number = random.randint(0x0000ffff,0xffffffff)
        string = bin(number)[2:]
        result = dfa.run(string)
        print(f"test_data[{i}]: result is {result}. \tthe test value is \"{string}\"")

def main():
    if len(sys.argv) == 2:
        print(dfa.run(sys.argv[1]))
    elif len(sys.argv) == 1:
        test()
    else:
        print("Usage:")
        print("\tpython3 ./problem_2_2_4_a.py <string>")
        print("\tpython3 ./problem_2_2_4_a.py")

if __name__ == "__main__":
    main()
