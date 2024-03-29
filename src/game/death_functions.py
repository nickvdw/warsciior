import tcod as libtcod

from game.render_functions import RenderOrder
from game.game_states import GameStates
from game.game_messages import Message


def kill_player(player):
    player.char = '%'
    player.color = libtcod.dark_red

    return Message('You died!', libtcod.red), GameStates.PLAYER_DEAD


def kill_monster(monster):
    death_message = '{0} is dead!'.format(monster.name.capitalize())

    monster.char = '%'
    monster.color = libtcod.dark_red
    monster.blocks = False
    monster.fighter = None
    monster.ai = None
    monster.render_order = RenderOrder.CORPSE
    death_message = Message('{0} is dead!'.format(monster.name.capitalize()), libtcod.orange)

    return death_message
