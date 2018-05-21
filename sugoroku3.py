import random
from time import sleep

def get_masu(): #マス数を入力
    print('マスの数を入力してください(20以上,40未満)')
    masu = int(input('>>'))
    if 20 <= masu < 40:#20以上40未満以外は値を受け取らない
        return masu
    else:
        get_masu()

def get_player_num(): #プレイヤーの数を入力
    print('プレイヤーの数を入力してください(2以上、6未満)')
    num_player = int(input(">>"))
    if  2 <= num_player < 6: #2以上、6未満以外は値を受け取らない
        return num_player
    else:
        get_player_num()


def main():
    print('これから双六を始めます。')
    masu = get_masu()
    num_player = get_player_num()
    masu_point = {} #マスにポイントを割り当てる
    print(type(masu))
    for i in range(1, masu+1):
        masu_point[i] = random.randint(1, 10)
        print("マスのポイント" + str(masu_point))
    counter = {} #プレイヤーポイントのカウンター
    location = [] #各プレイヤーの位置のリスト
    is_goal = {} #プレイヤーがゴールしたかどうか
    for i in range(1, num_player+1):
        counter[i]  = 0
        location.append(0)
        is_goal[i] = 0


    rank_num = 1
    rank = {}
    rank[0] = 0
    for turn in range(1, 1000):
        if len(rank) >= num_player:
            break
        for i in range(1, num_player+1):
            if is_goal[i] == 0:
                print( '今は' + str(turn) + 'ターンです。' )
                break
            else:
                continue
        for k, v in counter.items():
            if is_goal[k] == 1:
                continue
            if location[k-1] == masu:
                rank[rank_num] = k
                if rank[rank_num] == k:
                    counter[k] += num_player // len(rank) #ゴールした時の点数加算
                    rank_num += 1
                else:
                    break
            num_dice = random.randint(1, 8)
            print('プレイヤー' + str(k) + 'のサイコロの目は' + str(num_dice) + 'です')
            if num_dice % 2 == 0: #サイコロの目が偶数の時
                location[k-1] += num_dice
                if location[k-1] == masu:
                    is_goal[k] = 1
                    print("プレイヤー" + str(k) + 'はゴールです！\n')
                    break
                elif location[k-1] > masu:  #振出しに戻る
                    location[k-1] = 0
                    print('ゴールまであと' + str(abs(masu - location[k-1])) + 'マスです。' +"\n")

                else:
                    loc = int(location[k-1])
                    counter[k] += int(masu_point[loc])
                    print('ゴールまであと' + str(abs(masu - location[k-1])) + 'マスです。' +"\n")

            else: # サイコロの目が奇数の時
                location[k-1] -= num_dice
                if location[k-1] < 0: #スタート位置はマイナスにならない
                    location[k-1] = 0
                print('ゴールまであと' + str(abs(masu - location[k-1])) + 'マスです。' +"\n")

    for k, v in counter.items():
        print('プレイヤー' + str(k) + 'は' + str(v) + '点です')
    max_player = max(counter.items(), key=lambda x:x[1])[0]
    print('プレイヤー' + str(max_player) + 'は' + str(counter.get(max_player)) + '点で優勝です。'.format(max(counter.items())))

if __name__ == '__main__':
    main()
