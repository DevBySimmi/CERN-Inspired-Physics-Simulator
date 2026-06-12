import numpy as np
import matplotlib.pyplot as plt

plt.style.use("dark_background")

class ParticlePhysicsSimulator:

    def standard_model(self):
        particles = {
            "Electron":0.0005,
            "Muon":0.106,
            "Tau":1.77,
            "W":80.4,
            "Z":91.2,
            "Higgs":125,
            "Top":173
        }

        plt.figure(figsize=(10,5))
        plt.barh(list(particles.keys()), list(particles.values()))
        plt.xscale("log")
        plt.title("Standard Model Mass Spectrum")
        plt.xlabel("Mass (GeV)")
        plt.grid(True)
        plt.show()

    def higgs_potential(self):
        phi = np.linspace(-3,3,1000)
        V = -phi**2 + 0.25*phi**4

        plt.figure(figsize=(8,5))
        plt.plot(phi,V,linewidth=3)
        plt.title("Higgs Potential")
        plt.xlabel("Field")
        plt.ylabel("Potential")
        plt.grid(True)
        plt.show()

    def neutrino_oscillation(self):
        L = np.linspace(0,1000,1000)
        P = np.sin(0.01*L)**2

        plt.figure(figsize=(8,5))
        plt.plot(L,P,linewidth=3)
        plt.title("Neutrino Oscillation")
        plt.xlabel("Distance")
        plt.ylabel("Probability")
        plt.grid(True)
        plt.show()

    def relativity(self):
        beta = np.linspace(0,0.99,1000)
        gamma = 1/np.sqrt(1-beta**2)

        plt.figure(figsize=(8,5))
        plt.plot(beta,gamma,linewidth=3)
        plt.title("Relativistic Time Dilation")
        plt.xlabel("v/c")
        plt.ylabel("Gamma")
        plt.grid(True)
        plt.show()

    def cosmic_ray(self):
        np.random.seed(42)

        x = np.random.normal(0,5,500)
        y = np.random.normal(0,5,500)

        plt.figure(figsize=(8,8))
        plt.scatter(x,y,s=10)
        plt.title("Cosmic Ray Air Shower")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid(True)
        plt.show()

    def particle_decay(self):
        t = np.linspace(0,10,1000)

        plt.figure(figsize=(8,5))

        for tau in [0.5,1,2,3]:
            plt.plot(t,np.exp(-t/tau),label=f"τ={tau}")

        plt.yscale("log")
        plt.legend()
        plt.title("Particle Decay")
        plt.xlabel("Time")
        plt.ylabel("N/N0")
        plt.grid(True)
        plt.show()

    def run(self):
        self.particle_decay()
        self.standard_model()
        self.higgs_potential()
        self.neutrino_oscillation()
        self.relativity()
        self.cosmic_ray()

sim = ParticlePhysicsSimulator()
sim.run()