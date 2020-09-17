def changeMaker(coin_arr, amount, coin_selector=-1,coin_selected=[]):
    #print(coin_selected)
    if amount == 0 :
        return coin_selected    
    if amount < coin_arr[0]:
        return None
    while amount < coin_arr[coin_selector] and coin_selector > -1*len(coin_arr):
        coin_selector-=1
    coin_selected_new = None
    while coin_selected_new is None and coin_selector > -1*len(coin_arr):
        coin_selected_new = changeMaker(coin_arr,amount-coin_arr[coin_selector],coin_selector,coin_selected+[coin_arr[coin_selector]])
        coin_selector-=1
    return coin_selected_new

print("The coins needed are :",changeMaker([3,5,8],47))
