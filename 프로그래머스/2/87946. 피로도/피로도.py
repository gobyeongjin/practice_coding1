from itertools import permutations

def solution(k, dungeons):
    answer = 0

    # 던전의 인덱스
    indexes = range(len(dungeons))

    # 모든 던전 방문 순서 생성
    for order in permutations(indexes):
        current_k = k
        count = 0

        for i in order:
            # 현재 피로도로 던전을 갈 수 있는지 확인
            if current_k >= dungeons[i][0]:
                current_k -= dungeons[i][1]
                count += 1
            else:
                break

        answer = max(answer, count)

    return answer