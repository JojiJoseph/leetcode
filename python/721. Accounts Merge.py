from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        mail_to_id = {}
        n = len(accounts)
        graph = [[] for i in range(n)]
        for id_, account in enumerate(accounts):
            for email in account[1:]:
                if email in mail_to_id:
                    graph[id_].append(mail_to_id[email])
                    graph[mail_to_id[email]].append(id_)
                else:
                    mail_to_id[email] = id_
        
        merged_accounts = []
        
        q  = deque()
        visited = [0]*n 
        for id_ in range(n):
            if visited[id_]:
                continue
            q.append(id_)
            running_mail_ids = []
            while len(q):
                id_ = q.pop()
                visited[id_] = 1
                for next_id in graph[id_]:
                    if not visited[next_id]:
                        q.append(next_id)
                running_mail_ids.extend(accounts[id_][1:])
            merged_accounts.append([accounts[id_][0]] + sorted(set(running_mail_ids)))
        return  merged_accounts
