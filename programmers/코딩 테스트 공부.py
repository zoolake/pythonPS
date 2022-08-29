import sys
# DP
def solution(alp, cop, problems):
    answer = 0
    # 최대 알고력, 코딩력 찾기
    max_algo, max_coding = alp, cop
    for problem in problems:
        max_algo, max_coding = max(max_algo, problem[0]), max(max_coding, problem[1])
   
    # DP 테이블 초기화
    dp = [[sys.maxsize]*(max_coding+1) for _ in range(max_algo+1)]
    dp[alp][cop] = 0
    
    # 연산
    for algo in range(alp, max_algo+1):
        for coding in range(cop, max_coding+1):
            diff_algo = algo-alp 
            diff_coding = coding-cop
            dp[algo][coding] = min(dp[algo][coding], diff_algo + diff_coding)
            
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                # 문제를 풀 수 있다면
                if algo >= alp_req and coding >= cop_req:
                    next_algo = algo + alp_rwd if algo + alp_rwd <= max_algo else max_algo
                    next_coding = coding + cop_rwd if coding + cop_rwd <= max_coding else max_coding
                    dp[next_algo][next_coding] = min(dp[next_algo][next_coding], dp[algo][coding] + cost)
    
    return dp[max_algo][max_coding]
