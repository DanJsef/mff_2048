from source.control import Control
from source.states.menu import Menu
from source.states.game import GameState

app = Control()
state_dict = {
    'menu': Menu(),
    'game': GameState()
}
app.setup_states(state_dict, 'menu')
app.game_loop()
