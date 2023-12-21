import matplotlib.pyplot as plt

def show_rotation_graph(input_vector, rotated_vector):
    plt.figure()
    plt.quiver(0, 0, input_vector[0], input_vector[1], angles='xy', scale_units='xy', scale=1, color='b', label='Original Vector')
    plt.quiver(0, 0, rotated_vector[0], rotated_vector[1], angles='xy', scale_units='xy', scale=1, color='r', label='Rotated Vector')
    plt.xlim(-max(input_vector) - 1, max(input_vector) + 1)
    plt.ylim(-max(input_vector) - 1, max(input_vector) + 1)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.legend()
    plt.grid()
    plt.show()