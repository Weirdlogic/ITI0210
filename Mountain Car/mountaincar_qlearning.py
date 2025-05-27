import gymnasium as gym
import numpy as np
import matplotlib.pyplot as plt
import os

class MountainCarQLearning:
    def __init__(self, n_position_bins=20, n_velocity_bins=20):
        self.env = gym.make("MountainCar-v0")
        self.n_position_bins = n_position_bins
        self.n_velocity_bins = n_velocity_bins
        self.n_states = n_position_bins * n_velocity_bins
        self.n_actions = 3
        
        self.position_min = self.env.observation_space.low[0]
        self.position_max = self.env.observation_space.high[0]
        self.velocity_min = self.env.observation_space.low[1]
        self.velocity_max = self.env.observation_space.high[1]
        
        self.q_table = np.zeros((self.n_states, self.n_actions))
        
        self.alpha = 0.1
        self.gamma = 0.99
        self.epsilon = 1.0
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        
        self.episode_rewards = []
        self.episode_steps = []

    def discretize_state(self, observation):
        position, velocity = observation

        position_bin = int(np.digitize(position, np.linspace(self.position_min, self.position_max, self.n_position_bins + 1)) - 1)
        position_bin = np.clip(position_bin, 0, self.n_position_bins - 1)

        velocity_bin = int(np.digitize(velocity, np.linspace(self.velocity_min, self.velocity_max, self.n_velocity_bins + 1)) - 1)
        velocity_bin = np.clip(velocity_bin, 0, self.n_velocity_bins - 1)

        return position_bin * self.n_velocity_bins + velocity_bin

    def get_action(self, state):
        if np.random.random() < self.epsilon:
            return self.env.action_space.sample()
        return np.argmax(self.q_table[state])

    def custom_reward(self, observation, action, terminated):
        position, velocity = observation
        reward = -1
        if terminated and position >= 0.5:
            reward += 100
        if position > -0.5 and action == 2:
            reward += 0.1
        if position < -0.5 and action == 0:
            reward += 0.1
        if position > 0 and velocity > 0:
            reward += 1
        return reward

    def train(self, n_episodes=1000, use_custom_reward=True):
        print(f"Training for {n_episodes} episodes...")

        for episode in range(n_episodes):
            observation, _ = self.env.reset()
            state = self.discretize_state(observation)

            total_reward = 0
            steps = 0

            for step in range(200):
                action = self.get_action(state)
                next_observation, reward, terminated, truncated, _ = self.env.step(action)
                next_state = self.discretize_state(next_observation)

                if use_custom_reward:
                    reward = self.custom_reward(next_observation, action, terminated)

                target = reward + self.gamma * np.max(self.q_table[next_state]) if not terminated else reward
                self.q_table[state, action] += self.alpha * (target - self.q_table[state, action])

                state = next_state
                total_reward += reward
                steps = step + 1

                if terminated or truncated:
                    break

            if self.epsilon > self.epsilon_min:
                self.epsilon *= self.epsilon_decay

            self.episode_rewards.append(total_reward)
            self.episode_steps.append(steps)

            if (episode + 1) % 100 == 0:
                avg_steps = np.mean(self.episode_steps[-100:])
                avg_reward = np.mean(self.episode_rewards[-100:])
                print(f"Episode {episode + 1}: Avg Steps = {avg_steps:.1f}, Avg Reward = {avg_reward:.1f}, Epsilon = {self.epsilon:.3f}")
                if avg_steps < 200:
                    print(" Car is reaching the flag consistently.")

    def test(self, n_episodes=5, render=True):
        test_env = gym.make("MountainCar-v0", render_mode="human") if render else self.env
        print(f"\nTesting trained agent for {n_episodes} episodes...")

        old_epsilon = self.epsilon
        self.epsilon = 0
        test_steps = []

        for episode in range(n_episodes):
            observation, _ = test_env.reset()
            state = self.discretize_state(observation)

            for step in range(200):
                action = self.get_action(state)
                observation, _, terminated, truncated, _ = test_env.step(action)
                state = self.discretize_state(observation)

                if terminated or truncated:
                    break

            test_steps.append(step + 1)
            print(f"Test Episode {episode + 1}: {step + 1} steps")

        self.epsilon = old_epsilon
        if render:
            test_env.close()

        avg_test_steps = np.mean(test_steps)
        print(f"Average test steps: {avg_test_steps:.1f}")
        return test_steps

    def plot_training_progress(self):
        os.makedirs("output", exist_ok=True)
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

        window = 50
        if len(self.episode_steps) >= window:
            smoothed_steps = np.convolve(self.episode_steps, np.ones(window)/window, mode='valid')
            ax1.plot(range(window-1, len(self.episode_steps)), smoothed_steps, label='Smoothed')
        ax1.plot(self.episode_steps, alpha=0.3, label='Raw')
        ax1.set_xlabel('Episode')
        ax1.set_ylabel('Steps to Complete')
        ax1.set_title('Learning Progress (Steps per Episode)')
        ax1.grid(True)
        ax1.legend()

        if len(self.episode_rewards) >= window:
            smoothed_rewards = np.convolve(self.episode_rewards, np.ones(window)/window, mode='valid')
            ax2.plot(range(window-1, len(self.episode_rewards)), smoothed_rewards, label='Smoothed')
        ax2.plot(self.episode_rewards, alpha=0.3, label='Raw')
        ax2.set_xlabel('Episode')
        ax2.set_ylabel('Total Reward')
        ax2.set_title('Learning Progress (Reward per Episode)')
        ax2.grid(True)
        ax2.legend()

        plt.tight_layout()
        output_path = "output/training_progress.png"
        plt.savefig(output_path)
        plt.close()
        print(f"Training graph saved as {output_path}")

if __name__ == "__main__":
    agent = MountainCarQLearning(n_position_bins=20, n_velocity_bins=20)
    agent.train(n_episodes=1000, use_custom_reward=True)
    agent.plot_training_progress()
    agent.test(n_episodes=3, render=True)
    agent.env.close()
    print("\nTraining complete!")
