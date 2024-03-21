class Solution:
    def interpret(self, command: str) -> str:
        i = 0
        res = ""
        while i < len(command):
            if command[i] == "G":
                res+="G"
                i+=1
            elif command[i] == "(":
                if command[i+1] == "a":
                    res+="al"
                    i+=4
                else:
                    res+="o"
                    i+=2
        return res

        