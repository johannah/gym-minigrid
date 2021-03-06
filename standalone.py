#!/usr/bin/env python3

from __future__ import division, print_function

import sys
import numpy
import gym
import time
from optparse import OptionParser

import gym_minigrid
from gym_minigrid.envs import MiniGridEnv

def main():
    parser = OptionParser()
    parser.add_option(
        "-e",
        "--env-name",
        dest="env_name",
        help="gym environment to load",
        default='MiniGrid-Multi-Room-N6-v0'
    )
    (options, args) = parser.parse_args()

    # Load the gym environment
    env = gym.make(options.env_name)
    env.reset()

    # Create a window to render into
    renderer = env.render('human')

    def keyDownCb(keyName):
        action = 0
        if keyName == 'LEFT':
            action = MiniGridEnv.ACTION_LEFT
        elif keyName == 'RIGHT':
            action = MiniGridEnv.ACTION_RIGHT
        elif keyName == 'UP':
            action = MiniGridEnv.ACTION_FORWARD
        elif keyName == 'SPACE':
            action = MiniGridEnv.ACTION_TOGGLE
        elif keyName == 'RETURN':
            env.reset()
        elif keyName == 'ESCAPE':
            sys.exit(0)
        else:
            print("unknown key %s" % keyName)
            return

        obs, reward, done, info = env.step(action)

        print('step=%s, reward=%s' % (env.stepCount, reward))

        if done:
            print('done!')
            env.reset()

    renderer.window.setKeyDownCb(keyDownCb)

    while True:
        env.render('human')
        time.sleep(0.01)

        # If the window was closed
        if renderer.window == None:
            break

if __name__ == "__main__":
    main()
