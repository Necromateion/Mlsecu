def get_adversarial_points(classifier, candidates, attack, dist_function, epsilon):
    original_points = []
    altered_points = []
    adv_epsilons = []

    step = 0.01

    for candidate in candidates:
        adversarial_example, current_epsilon = attack(classifier, candidate, dist_function, step=step, epsilon=epsilon)

        if adversarial_example is not None:
            original_points.append(candidate)
            altered_points.append(adversarial_example)
            adv_epsilons.append(current_epsilon)

    return original_points, altered_points, adv_epsilons

def get_smallest_alteration(classifier, candidates, attack, dist_function):
    original_point = None
    altered_point = None
    adv_epsilon = float('inf')

    step = 0.01

    for candidate in candidates:
        adversarial_example, current_epsilon = attack(classifier, candidate, dist_function, step=step)

        if adversarial_example is not None and current_epsilon < adv_epsilon:
            original_point = candidate
            altered_point = adversarial_example
            adv_epsilon = current_epsilon

    return original_point, altered_point, adv_epsilon
