import torch

from fid_score import calculate_fid_given_paths  # The code is downloaded from github
fid_value = calculate_fid_given_paths(['./img/real', './img/fake'],
                                                          100, 
                                                          True,
                                                          2048)

print (f'FID score: {fid_value}')
