import gym
import gym_duckietown
import time
import sys
import argparse
import math
import numpy as np
import gym

def launch_env(id=None):
    env = None
    if id is None:
        # Launch the environment
        from gym_duckietown.simulator import Simulator

        env = Simulator(
            seed=123,  # random seed
            map_name="small_loop",
            max_steps=500001,  # we don't want the gym to reset itself
            domain_rand=False,
            camera_width=640,
            camera_height=480,
            accept_start_angle_deg=4,  # start close to straight
            full_transparency=True,
            distortion=True,
        )
    else:
        env = gym.make(id)

    return env
