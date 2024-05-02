import numpy as np

def fgsm_attack_svm_2c(classifier, orig_point, dist_function, step=None, epsilon=np.inf, max_step=200):
    data_point = orig_point.copy()
    orig_class = classifier.predict(data_point.reshape(1, -1))[0]
    new_class = orig_class
    current_epsilon = dist_function(orig_point, data_point)
    nb_steps = 0
    attack_info = (None, None)
    while orig_class == new_class:
        if current_epsilon < epsilon and nb_steps < max_step:
            nb_steps += 1
            data_point += step * classifier.coef_[0]
            new_class = classifier.predict(data_point.reshape(1, -1))[0]
            current_epsilon = dist_function(orig_point, data_point)
            attack_info = (data_point, current_epsilon)            
        else:
            return None, None
    return attack_info