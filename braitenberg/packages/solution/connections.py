from typing import Tuple

import numpy as np

"""
def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")
    # these are random values
    res[100:150, 100:150] = 1
    res[300:, 200:] = 1
    # ---
    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")
    # these are random values
    res[100:150, 100:300] = -1
    # ---
    return res
"""

def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    H, W = shape
    res = np.zeros(shape, dtype=np.float32)
    
    near_zone = int(H * 0.5)  # Moitié inférieure = zone proche
    mid_w = W // 2            # Centre horizontal
    
    # Zone haute : avancer
    res[:near_zone, :] = 1.0
    
    # Zone basse gauche : légèrement avancer
    res[near_zone:, :mid_w] = 0.5
    
    # Zone basse droite : tourner à gauche (freiner moteur gauche)
    res[near_zone:, mid_w:] = -1.0
    
    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    H, W = shape
    res = np.zeros(shape, dtype=np.float32)
    
    near_zone = int(H * 0.5)
    mid_w = W // 2
    
    # Zone haute : avancer
    res[:near_zone, :] = 1.0
    
    # Zone basse droite : légèrement avancer
    res[near_zone:, mid_w:] = 0.5
    
    # Zone basse gauche : tourner à droite (freiner moteur droit)
    res[near_zone:, :mid_w] = -1.0
    
    return res