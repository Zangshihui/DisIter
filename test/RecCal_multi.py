import sys
import time
import numpy as np
from DisIter import Reconstruct

NMesh = 512
BoxSize = 1000
R_init = 20
R_min = 2

def main():
    start = time.time()
    
    snapPATH = '/scratch/p/pen/zangsh/Quijote_Simulations/Snapshots/fiducial/0/snapdir_004/snap_004'
    MyRec = Reconstruct(NMesh = NMesh, BoxSize = BoxSize, Omega_m0 = 0.3175, redshift = 0.0)
    # Read the snapshot
    MyRec.Readsnapshots(snapPATH = snapPATH)
    # Apply the RSD
#     MyRec.RSD(los = 0)
    
    # Generate the displacement field
    # Loop to iterate
    for i in range(8):
        # Paint the catalog on the mesh using cic
        MyRec.Paint()
        R = max(0.5**i*R_init, R_min)
        MyRec.Gaussian_Window(R)
        MyRec.Zeldovich_Approx() 
        MyRec.Shift()
    
    # Generate the displacement field
    MyRec.Paint()
    den = MyRec.GetDensity()
    MyRec.Displace_Reconstruct()
    den = MyRec.GetRecDensity()
    
    end = time.time()
    print('DisIter finished, costs %f s.'%(end - start))
        
if __name__ == '__main__':
    main()