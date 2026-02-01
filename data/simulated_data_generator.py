import pandas as pd
import numpy as np

# Simulate 30 days of hourly water usage
hours = 30 * 24
np.random.seed(42)

# Normal usage pattern
usage = np.random.normal(loc=50, scale=10, size=hours)

# Inject anomalies (simulated leaks)
anomaly_indices = np.random.choice(hours, size=10, replace=False)
usage[anomaly_indices] *= 3  # spikes represent leaks

df = pd.DataFrame({'Water_Usage': usage})
df.to_csv("sample_usage.csv", index=False)
print("Simulated dataset created: sample_usage.csv")
