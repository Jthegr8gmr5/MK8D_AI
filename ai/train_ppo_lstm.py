from stable_baselines3 import PPO
from ai_env import MK8DEnv

def main():
    env = MK8DEnv()
    model = PPO("CnnLstmPolicy", env, verbose=1)
    model.learn(total_timesteps=10000)
    model.save("ai/model/mk8d_lstm")

if __name__ == "__main__":
    main()
