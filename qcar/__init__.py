from gym.envs.registration import register

register(
    id='qcar-v0',
    entry_point='qcar.envs:QcarEnv',
)
