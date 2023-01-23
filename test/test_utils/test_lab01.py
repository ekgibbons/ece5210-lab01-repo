import random
import time 
import unittest

import numpy as np

from ..test_utils import moving_average
import moving_average_sol

class TestDTFT(unittest.TestCase):
    def test_dtft(self):
        print("\nTesting DTFT function")
        left_bound = random.randint(-100,100)
        right_bound = random.randint(left_bound+10,1000)

        n = np.arange(left_bound, right_bound)

        x = np.random.uniform(-100,100,size=len(n))

        omega = np.linspace(-np.pi,np.pi,1000)

        X_my = moving_average.dtft(x, omega, n)
        X_sol = moving_average_sol.dtft(x, omega, n)
                  
        np.testing.assert_array_almost_equal(X_my, X_sol)

    def test_phase_correct(self):
        print("\nTesting phase correct function")

        N = random.randint(50,100)
        phase_array = np.random.uniform(-np.pi, np.pi, N)
        freq_omega_array = np.linspace(0,np.pi,N)

        phase_my = moving_average.phase_correct(
            phase_array,
            freq_omega_array)
        phase_sol = moving_average_sol.phase_correct(
            phase_array,
            freq_omega_array)

        np.testing.assert_array_almost_equal(phase_my, phase_sol)
        
        
if __name__ == "__main__":
    unittest.main()
