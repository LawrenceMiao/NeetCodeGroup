import solution
import time
import requests, json

WEBHOOK_URL = "https://discord.com/api/webhooks/1251399417270108244/KrA_3RLwEunPAS9NGr1GV4-dDkGCM1OPiCE9fPuBsw5_TOnVaU-ePvo84P7gMoiydWV8"

ITERATIONS = 3

deltas = []
for i in range(ITERATIONS):
    start_time = time.time()

    function = solution.Solution().maxCoins

    assert function([4, 2, 3, 7]) == 5

    end_time = time.time()

    deltas.append((end_time - start_time) * 1000)

average_runtime = round(sum(deltas) / ITERATIONS)

message = f"Average runtime for *maxCoins* is: **{average_runtime}ms**"

response = requests.post(
    WEBHOOK_URL,
    data=json.dumps({"content": message}),
    headers={"Content-Type": "application/json"},
)
