# player_inv = {}
def display_inventory(dict):
    print('Inventory:')
    item_total = 0
    for k,v in dict.items():
        item_total += v
        print(str(v) + ' ' + str(k))
    print('Total number of items: ' + str(item_total))

def add_to_inventory(inventory, add_items):
    for i in add_items:
        if i in inventory.keys():
            inventory[i] += 1
        else:
            inventory.setdefault(i, 0)
            inventory[i] += 1
    return inventory


player_inv = {'rope':1,'torch':6,'gold coin':42,'dagger':1,'arrow':12}
dragon_loot = ['gold coin','dagger','gold coin','gold coin','ruby']
player_inv = add_to_inventory(player_inv, dragon_loot)
display_inventory(player_inv)

