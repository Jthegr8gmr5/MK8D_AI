import gymnasium as gym
from gymnasium import spaces
import numpy as np
from bot_control.usb_botbase import USBBotbase
from bot_control.controller_inputs import INPUTS

class MK8DEnv(gym.Env):
    def __init__(self):
        self.bot = USBBotbase()
        self.action_space = spaces.Discrete(len(INPUTS))
        self.observation_space = spaces.Box(0, 255, (84, 84, 4), dtype=np.uint8)

    def step(self, action):
        key = list(INPUTS.keys())[action]
        self.bot.send_input(INPUTS[key])
        obs = np.zeros((84, 84, 4), dtype=np.uint8)  # placeholder
        reward = 0.0
        done = False
        info = {}
        return obs, reward, done, info

    def reset(self):
        obs = np.zeros((84, 84, 4), dtype=np.uint8)
        return obs, {}
