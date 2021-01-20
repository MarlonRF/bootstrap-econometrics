import numpy as np
import matplotlib.pyplot as plt

def Bootstrap(data, n=30, iteract=10000, stats=0, graph=False, serie=False):
    
    #ORIGINAL DATA
    N=len(data)
    media=np.mean(data)
    dp=np.std(data, ddof=1)
    erro_p=dp/N**0.5
        
    # BOOTSTRAP  
    boot_data = []
    for _ in range(iteract):
        boot_sample = np.random.choice(data,size=n, replace=True)
        boot_data.append(boot_sample.mean())
    b_mean=np.mean(boot_data)
    b_dp = np.std(boot_data, ddof=1)
    b_erro_p = b_dp/(n**0.5)
    
    if stats==True:
        print(
              '   Original Distibuton: \n',
              'Mean:{:5.2f}'.format(mean),'\n',
              'SD:{:5.2f}'.format(dp),'\n',
              'Standart error:{:5.2f}'.format(erro_p),'\n\n',
              '   Resampled Distribution: \n',
              'Mean - Bootstrap:{:5.2f}'.format(b_media),'\n',
              'SD - Bootstrap:{:5.2f}'.format(b_dp),'\n',
              'Standart error - Bootstrap:{:5.2f}'.format(b_erro_p),'\n'
             )
    if graph==True:
        plt.figure(figsize=(13,10), dpi= 80)
        ax1=sns.distplot(data, color="steelblue")
        ax2=sns.distplot(boot_data, color="red")
        plt.show()
        
    if serie==True:
        return boot_medias
    
