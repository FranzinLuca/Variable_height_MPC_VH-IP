# Variable-height MPC using the VH-IP model
### D'Addario Giuseppe 2177530, Tranzocchi Federico 1891909, Franzin Luca 1886634, Gravili Andrea 2180997

---
# Description
This is IS-MPC, a framework for humanoid gait generation, extended to work with variable height of the CoM (VH-IP model).

The main reference is:<br />
[F. M. Smaldone, N. Scianca, L. Lanari, and G. Oriolo, “From walking to running: 3d
humanoid gait generation via mpc”](https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.876613/full), Frontiers in Robotics and AI, vol. 9, p. 876 613, 2022.

The implementation is an extension of the original code:<br />
DIAG Robotics Lab, Intrinsically Stable Model Predictive Control (IS-MPC), [GitHub](https://github.com/DIAG-Robotics-Lab/)

---
# Setup
You need a Python installation and some dependencis. If using pip, you can run the following
```
pip install dartpy casadi scipy matplotlib osqp
```
You need dartpy 0.2, if pip does not allow you to install this version on your system, you probably need to upgrade to Python 3.12 or use conda

To run the simulation
```
python simulation.py
```
then press spacebar to start it

---
# Report & presentation
The report explaining in detail the project is available [here](report.pdf). It is also available a canva presentation [here](https://canva.link/47w3jj0gx0jxxgt).