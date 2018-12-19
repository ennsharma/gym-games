import gym
import numpy as np

from gym import error, spaces, utils
from gym.utils import seeding

class BlackjackEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):
    self.action_map = {
    	0 : self._hit,
    	1 : self._stand,
    	2 : self._double,
    	3 : self._split,
    	4 : self._surrender
    }
    self.card_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    self.reset()

    self.action_space = spaces.Discrete(len(self.action_map))
    self.observation_space = spaces.Discrete(len(self.card_values))
    self.seed()

  def step(self, action):
    action_func = self.action_map[action]
    obs, rew, done = action_func()
    return obs, rew, done, {}

  def reset(self):
    self.total = 0
    self._hit()
    self._hit()

  def render(self, mode='human', close=False):
    pass

  def seed(self, seed=None):
    _, seed = seeding.np_random(seed)
    return [seed]

  def _hit():
  	self.total += self.card_values[np.random.randint(0, 13)]
  	if self.total > 21:
  		return self.total, -1, True
  	return self.total, 0, True
  
  def _stand():
  	return self.total, self.total, True

  def _double():
  	pass

  def _split():
  	pass

  def _surrender():
  	pass


