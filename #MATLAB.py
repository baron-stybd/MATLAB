import numpy as np
import matplotlib.pyplot as plt

A_exc = 0.0743  
wn = 20           
phi = 0.0488

zeta = 0.05
t = np.linspace(0, 1, 1000)
wd = wn * np.sqrt(1 - zeta**2)
x_axis = t

y_axis = A_exc * np.exp(-zeta * wn * t) * np.cos(wd * t + phi)
z_axis = A_exc * np.exp(-zeta * wn * t) * np.sin(wd * t + phi)

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x_axis, y_axis, z_axis, color='purple', linewidth=2, label='Lintasan Getaran')

ax.set_title('Visualisasi 3D Getaran Bebas Diredam (Damped Helix)', pad=20)
ax.set_xlabel('Waktu (t)', labelpad=10)
ax.set_ylabel('Amplitudo (Y)', labelpad=10)
ax.set_zlabel('Amplitudo (Z)', labelpad=10)

ax.legend()
plt.show()

print("Pengecekan koordinat 3D pada saat t = 0:")
print(f"X (Waktu) = {x_axis[0]:.4f}")
print(f"Y (Cos)   = {y_axis[0]:.4f}")
print(f"Z (Sin)   = {z_axis[0]:.4f}")
