import random
game_id = [
    'pegaxy',
    'star_sharks',
    'x_world_games',
    'second_live',
    'elfin_kingdom',
    'the_crypto_you',
    '_9d_nft',
    'binaryx',
    'cyball',
    'bomb_crypto',
    'metaverse_miner',
    'tiny_world',
    'zoo_crypto_world']

badge_des = [
    'Owned n nfts before',
    'Transfer tokens or nfts n times'
]

tier_score= [
    {1: 3},
    {2:10},
    {3: 20}
]


def build_badge_id(game_id, badge_name):
    for i in range(len(game_id)):
        id = game_id + '@' + badge_name
        return id


def build_stats_id(game_id, stat_id):
    for i in range(len(stat_id)):
        id = game_id + '@' + stat_id
        return id
    

def badge_obj_builder():
    
    tier = 3
    badge_offcial_name = [
        'Worthy',
        'Treasure Hunter'
    ]
    badge_name = [
        'worthy',
        'treasure_hunter'
    ]
    stat_ids = [
        'num_nfts_ever_owned',
        'num_transfers'
]
    list = []
    for i in range(len(game_id)):
        randoms = random.randint(0,50)     
        for j in range(len(badge_name)):
            for k in range(tier): 
                badge_id = build_badge_id(game_id[i], badge_name[j])
                stat_id = build_stats_id(game_id[i], stat_ids[j])
                badge_obj = """
            {{
                "badge_id": "{0}_{2}",
                "game_id": "{3}",
                "name": "{4}",
                "description_short": "{5}",
                "description_full": "{5}",
                "image_url": "https://public.wowarriors.io/carv/images/{3}.png",
                "image_thumbnail_url": "https://public.wowarriors.io/carv/images/{3}.png",
                "badge_tier": {2},
                "required_badges": [],
                "required_stats": [
                    {{
                        "stat_id": "{1}",
                        "stat_name": "{5}",
                        "description_short": "{5}",
                        "operator": "gte",
                        "value": {6}
                    }}
                ],
                "required_whitelist": null,
                "required_leaderboard": null,
                "badge_users_count": 1,
                "badge_score": 11,
                "game_users_count": 2,
                "obtained_percentage": {7},
                "created_time": 1645540317,
                "updated_time": 1645540317,
                "chains": [
                    {{
                        "type": "ethereum",
                        "chain_id": "137",
                        "name": "Polygon",
                        "image_url": "https://public.wowarriors.io/icon/polygon.png"
                    }}
                ],
                "open_for_mint": true,
                "num_minted": {7}

                        }}""" .format(badge_id, stat_id, k+1, game_id[i], badge_offcial_name[j], badge_des[j], tier_score[k][k+1], randoms)
                list.append(badge_obj)
        
    return list


list = badge_obj_builder()

list_strings = [str(number) for number in list]
list_strings_formatted = "[{}]".format(", ".join(list_strings))


#write this string into a file
with open('badge_objs.json', 'w') as f:
    f.write(list_strings_formatted)
