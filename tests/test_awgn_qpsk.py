import numpy as np
from nr_urlcc import simulate

def qpsk_theory_ber(snr_db):
    snr_linear = 10**(snr_db/10)
    return 0.5 * (1 - np.sqrt(snr_linear / (1 + snr_linear)))

def test_awgn_qpsk_ber():
    cfg = {"seed": 0, "n_bits": 100000, "snr_db": 5}
    result = simulate.run(cfg)
    sim_ber = result["ber"]
    theory_ber = qpsk_theory_ber(cfg["snr_db"])
    sim_db = 10*np.log10(sim_ber)
    theory_db = 10*np.log10(theory_ber)
    assert abs(sim_db - theory_db) <= 0.5
