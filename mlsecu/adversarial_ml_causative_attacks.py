import numpy as np

def move_decision_frontier(classifier, poisoning_points, target_class, point_to_hide, max_step=200):
    point_to_hide_array = np.array(point_to_hide).reshape(1, -1)

    predict_init = classifier.predict(point_to_hide_array)[0]
    predict_current = predict_init
    step = 0

    while predict_current == predict_init and step < max_step:
        step += 1

        classifier.partial_fit(poisoning_points, np.full(len(poisoning_points), target_class))

        predict_current = classifier.predict(point_to_hide_array)[0]

    if step == max_step:
        print(f'Max step achieved: {max_step}')

    return classifier


