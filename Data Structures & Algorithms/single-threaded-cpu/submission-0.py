class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        d = {}
        for t in range(len(tasks)):
            d[t] = tasks[t]

    
        order_by_enqueue = sorted(d, key=lambda k: d[k][0])

        res = []
        heap = []  # (processingTime, index) — available tasks
        time = 0
        i = 0  # pointer into order_by_enqueue
        n = len(tasks)

        while len(res) < n:
        # push all tasks that have become available by current time
            while i < n and d[order_by_enqueue[i]][0] <= time:
                idx = order_by_enqueue[i]
                heapq.heappush(heap, (d[idx][1], idx))
                i += 1

            if heap:
                proc_time, idx = heapq.heappop(heap)
                time += proc_time
                res.append(idx)
            elif i < n:
            # CPU idle, jump time to the next task's enqueue time
                time = d[order_by_enqueue[i]][0]

        return res
