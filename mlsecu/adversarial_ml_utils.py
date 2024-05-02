def get_astute_accuracy_from_attack_points(orig_points, orig_labels, points_with_successful_attacks, class_label):
    total_orig_class_points = sum(1 for label in orig_labels if label == class_label)
    successful_attacks = set()
    for orig_point, attack_point, label in zip(orig_points, points_with_successful_attacks, orig_labels):
        if orig_point != attack_point and label == class_label :
            successful_attacks.add(tuple(attack_point))
    astute_accuracy = (total_orig_class_points - len(successful_attacks)) / total_orig_class_points
    return astute_accuracy


def get_astute_accuracy_from_success_array(orig_labels, success_array, class_label):
    total_orig_class_points = sum(1 for label in orig_labels if label == class_label)
    successful_attacks = 0
    for success, label in zip(success_array, orig_labels):
        if success and label == class_label:
            successful_attacks += 1
    astute_accuracy = (total_orig_class_points - successful_attacks) / total_orig_class_points
    return astute_accuracy



def get_robust_accuracy_from_attack_points(orig_points, points_with_successful_attacks):
    unchanged_points = sum(1 for orig_point, attacked_point in zip(orig_points, points_with_successful_attacks)
                           if orig_point == attacked_point)

    robust_accuracy = unchanged_points / len(orig_points) if orig_points else 0
    return robust_accuracy

def get_robust_accuracy_from_success_array(success_array):
    not_attacked_points = sum(1 for success in success_array if not success)

    robust_accuracy = not_attacked_points / len(success_array) if success_array else 0
    return robust_accuracy




