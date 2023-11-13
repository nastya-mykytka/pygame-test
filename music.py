from pygame import mixer
mixer.init()

game_sound = mixer.Sound('music/we-wish-you-a-merry-christmas_60sec-174155 (1).mp3')
game_sound.set_volume(0.1)


game_over_sound = mixer.Sound('music/mixkit-fairytale-game-over-1945.wav')
game_over_sound.set_volume(0.1)

win_sound = mixer.Sound('music/TB7L64W-winning (mp3cut.net).mp3')
win_sound.set_volume(0.5)