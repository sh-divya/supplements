import numpy as np

def tb_P_inv(x_data, y_data, bin_size, fit_start, fit_stop):
    
    glob_avg = np.mean(y_data) 
    glob2_avg = np.mean([i**2 for i in y_data])
    den = glob2_avg - (glob_avg)**2
    P_inv = []
    tb_inv = []
    
    for interval in bin_size:
        
        n_b = 0
        sig_int_2 = 0
        start = 0
        stop = interval
        tb = x_data[stop-1] - x_data[start]
        while stop < len(x_data):
            sig_int_2 += (np.mean(y_data[start:stop]) - glob_avg)**2
            start += interval
            stop += interval
            n_b += 1
        tb_inv.append(1.0/tb)
        sig_int_2 = sig_int_2/n_b
        P_inv.append(den/(sig_int_2*tb))
        
    (m, b) = np.polyfit(tb_inv[fit_start:fit_stop], P_inv[fit_start:fit_stop], 1)
    t_c = 1.0/(b)
    error_2 = (glob2_avg-glob_avg**2)/(b*x_data[-1])

    return  (tb_inv, P_inv, t_c, error_2)
