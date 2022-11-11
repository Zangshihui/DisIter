# DisIter
**DisIter** is a python package to perform [the iterative displacement initial condition reconstruction](http://arxiv.org/abs/1704.06634) algorithm on particle catalogs.

## Dependences

### GCC

gcc is required to compile the cython files.

### Other python pkgs
requirement.txt has listed all required python packages. They can be installed using the setup.py. Virtual environment is recommended to avoid collisions with other existed pkgs.

## install DisIter
```
git clone https://github.com/Zangshihui/DisIter
cd ./DisIter
python setup.py build_ext
python setup.py install
```

## Tutorial
### Set the cosmology
```
from DisIter import Reconstruct
MyRec = Reconstruct(NMesh = NMesh, BoxSize = BoxSize, Omega_m0 = 0.3175, redshift = 0.5)
```
NMesh decides the mesh grid where the reconstruction is going to perform. BoxSize is the size of the simulation. Omega_m0 is the matter density at $z = 0$. 
### Read the snapshot files
```
MyRec.Readsnapshots(snapPATH = snapPATH)
```
We quote the readgadget.py and readfof.py program in [Pylians3](https://github.com/franciscovillaescusa/Pylians3). Gadget format snapshots are supported here.

### Apply RSD
```
MyRec.RSD(los = 2)
```
You can map your catalog into the redshift space.

### Perform the reconstruction
```
for i in range(8):
    # Paint the catalog on the mesh using cic
    MyRec.Paint()
    R = max(0.5**i*R_init, R_min)
    MyRec.Gaussian_Window(R)
    MyRec.Zeldovich_Approx() 
    MyRec.Shift()
```
You can set the iterative step number, initial smoothing scale and minimun smoothing scale by your self.

### Get the result
```
den = MyRec.GetRecDensity()
```