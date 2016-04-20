# coding=utf-8

import gzip
import traceback

import ultrajson as json


def main():
    start = 500000
    end = 520000
    battle_ids = range(start, end)

    with open('./battles.tsv', 'w') as out:
        out.write(get_header_line())
        out.write('\n')
        write_to(extract_fields(read_file(battle_ids)), out)


def read_file(battle_ids):
    for battle_id in battle_ids:
        with gzip.open("./data/{0}.json.gz".format(battle_id), "rt", encoding="utf-8") as f:
            try:
                raw = f.read(-1)
                if len(raw) == 0:
                    continue

                battle = json.loads(raw)
                yield battle

            except Exception as e:
                print('=========================')
                print(e)
                print(battle)
                traceback.print_exc()


def extract_fields(battles):
    valid_count = 0
    for battle in battles:
        if 'error' in battle:
            continue

        if battle['players'] is None:
            print('No player data. Skip')
            continue

        if len(battle['players']) != 8:
            print('Not full member match. Skip')
            continue

        id = battle.get('id')
        url = battle.get('url')
        rule_name, rule_mode = extract_rule_mode_name(battle)
        map_name = extract_map_name(battle)
        is_win = 1 if battle['result'] == 'win' else 0

        players = battle['players']
        friend_weapons = list(map(
            lambda p: p['weapon']['key'],
            filter(lambda p: p['team'] == 'my', players)))
        enemy_weapons = list(map(
            lambda p: p['weapon']['key'],
            filter(lambda p: p['team'] == 'his', players)))

        yield [
            str(id), url, rule_name, map_name, str(is_win),
            friend_weapons[0],
            friend_weapons[1],
            friend_weapons[2],
            friend_weapons[3],
            enemy_weapons[0],
            enemy_weapons[1],
            enemy_weapons[2],
            enemy_weapons[3]
        ]
        valid_count += 1

    print("Validated data count {0}".format(valid_count))


def write_to(records, output):
    for record in records:
        output.write('\t'.join(record))
        output.write('\n')


def get_header_line():
    return '\t'.join([
        'id', 'url', 'rule_name', 'map_name', 'is_win',
        'friend_weapon1',
        'friend_weapon2',
        'friend_weapon3',
        'friend_weapon4',
        'enemy_weapon1',
        'enemy_weapon2',
        'enemy_weapon3',
        'enemy_weapon4'
    ])


def extract_rule_mode_name(battle):
    rule = battle.get('rule')
    rule_name = ''
    rule_mode = ''
    if rule:
        rule_name = rule['key']
        mode = rule.get('rule')
        if mode:
            rule_mode = mode['key']
    return rule_name, rule_mode


def extract_map_name(battle):
    map_name = ''
    map_info = battle.get('map')
    if map_info:
        map_name = map_info['key']
    return map_name


if __name__ == "__main__":
    main()
