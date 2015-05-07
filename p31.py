coins = [1,2,5,10,20,50,100,200]


def countways(cap,coins):
    if len(coins) == 1:
        if cap % coins[0] == 0:
            return 1
        return 0
    ways = 0
    coin = coins[-1]
    for n in range(cap/coin+1):
        ways += countways(cap-n*coin,coins[:-1])
    return ways

print countways(200,coins)



