import heapq

def solution(operations):
    heap = []
    
    for op in operations:
        command, val = op.split()
        num = int(val)
        
        if command == "I":
            heapq.heappush(heap, num)
        elif command == "D" and heap:
            if num == 1:
                # 1. 최댓값 삭제: 리스트의 최댓값을 찾아 제거 후 다시 힙 재구축
                heap.remove(max(heap))
                heapq.heapify(heap)
            elif num == -1:
                # 2. 최솟값 삭제: 최소 힙에서 가장 작은 값 삭제
                heapq.heappop(heap)
                
    if not heap:
        return [0, 0]
    
    return [max(heap), heapq.heappop(heap)]