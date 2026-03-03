1847
"""Coletar a temperatura de três dias seguidos e informar se as pessoas ficaram felizes ou tristes"""
T1, T2, T3 = map(int,input().split())
deltaT2, deltaT3 = T2 - T1, T3 - T2
if deltaT2 == 0:
    print(':)') if deltaT3 > 0 else print(':(')
elif deltaT2 > 0:
    print(':(') if deltaT3 < deltaT2 else print(':)') if deltaT3 > 0 else print(':(')
else:
    print(':)') if deltaT3 >= 0 else print(':)') if abs(deltaT2) > abs(deltaT3) else print(':(')
