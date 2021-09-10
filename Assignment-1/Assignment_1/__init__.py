from gym.envs.registration import register

register(
    id='RandomWalk-v0',
    entry_point='Assignment_1.Env:RandomWalk',
)
register(
    id='tenArmedGaussianBandit-v0',
    entry_point='Assignment_1.Env:ten_armed_gaussian_bandit',
)   
register(
    id='twoArmedBernoulliBandit-v0',
    entry_point='Assignment_1.Env:two_armed_bernoulli_bandit',
)   