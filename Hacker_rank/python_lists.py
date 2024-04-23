if __name__ == '__main__':
    N = int(input())
    ans = []
    for _ in range(N):
        s= str(input())
        s_list = s.split(" ")
        if s_list[0]=='insert':
            ans.insert(int(s_list[1]), int(s_list[2]))
        elif s_list[0]=='append':
            ans.append(int(s_list[1]))
        elif s_list[0]=='remove':
            ans.remove(int(s_list[1]))
        elif s_list[0]=='sort':
            ans = sorted(ans)
        elif s_list[0]=='pop':
            ans.pop()
        elif s_list[0]=='reverse':
            ans.reverse()
        else:
            print(ans)

        
