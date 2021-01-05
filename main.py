from source.control import Control
from source.states.menu import MainMenu, LoseMenu, WinMenu
from source.states.game import GameState

app = Control()
state_dict = {
    'menu': MainMenu(),
    'game': GameState(),
    'lose': LoseMenu(),
    'win': WinMenu()
}
app.setup_states(state_dict, 'menu')
app.game_loop()
