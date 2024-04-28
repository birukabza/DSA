class Solution:
    def simplifyPath(self, path: str) -> str:

        path = path.split('/')
        stack = []
        for dir in path:
            if stack and dir == "..":
                stack.pop()
            elif dir != "." and dir != "" and  dir!="..":
                stack.append(dir)

        return "/" + "/".join(stack)