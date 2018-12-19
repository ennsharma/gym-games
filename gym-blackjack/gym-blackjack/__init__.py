from gym.envs.registration import register

register(
    id='BlackjackEnv-v0',
    entry_point='gym_blackjack.envs:BlackjackEnv',
)