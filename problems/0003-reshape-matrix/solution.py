import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	try:
		arr = np.array(a)
		reshaped = arr.reshape(new_shape)
		reshaped_matrix = reshaped.tolist()
	except ValueError:
		reshaped_matrix = []
	
	return reshaped_matrix