__author__ = "Tony Rozzi"


from cv2 import (
    Canny,
    HoughLines,
    imshow,
    waitKey,
    destroyAllWindows,
    resize,
    COLOR_BGR2HSV,
    imread,
    cvtColor,
    inRange,
    bitwise_and,
    line,
    LINE_AA,
)

from numpy import inf, linspace, array
from colorsys import rgb_to_hsv
from math import pi, sin, cos, tan, atan, atan2, isclose
from random import choice as random_choice
import matplotlib.pyplot as plt
from matplotlib import rc


def show(name, image):
    h, w = image.shape[0], image.shape[1]
    imshow(name, resize(image, (w // 2, h // 2)))
    waitKey(0)
    destroyAllWindows()


def contains_similar_line(
    image, line_list, new_line, epsilon_angle=0.1, epsilon_shift=5
):
    # Ax + By = C
    # new_line = (A, B, C)
    # line_list = [(A, B, C), (A, B, C), (A, B, C), ...]

    # lines are considered similar IF
    # 1) The angle between them is less then epsilon_angle (in radians) AND
    # 2a) They contain an intersection point within the image OR
    # 2b) They are parallel lines, and are a distance apart < epsilon_shift

    new_line_angle = atan(-new_line[0] / new_line[1])

    for line in line_list:
        line_angle = atan(-line[0] / line[1])
        if not isclose(new_line_angle, line_angle, abs_tol=epsilon_angle):
            continue

        if lines_are_parallel(line, new_line, 0.0000001):
            if lines_are_close(image, line, new_line, epsilon_shift):
                return True

        elif image_contains_intersection_pt(image, line, new_line):
            return True

    return False


def slope(line):
    if line[1] == 0:
        return inf
    return -line[0] / line[1]


def lines_are_parallel(line1, line2, epsilon):
    angle1 = atan(-line1[0] / line1[1])
    angle2 = atan(-line2[0] / line2[1])
    return isclose(angle1, angle2, abs_tol=epsilon)


def intersection(l1, l2):
    # given lines must not be parallel, this method doesn't check for that
    b_ratio = l2[1] / l1[1]
    x_intersection = (l2[2] - b_ratio * l1[2]) / (l2[0] - b_ratio * l1[0])
    y_intersection = (l1[2] - l1[0] * x_intersection) / l1[1]  # return (C - A*x) / B;
    return x_intersection, y_intersection


def image_contains_intersection_pt(image, line1, line2):
    pt = intersection(line1, line2)
    h, w = image.shape[0], image.shape[1]
    return 0 < pt[0] < w and 0 < pt[1] < h


def line_from_point_and_slope(point, slope):
    if slope == float("inf"):
        return 1, 0, point[0]
    else:
        return slope, -1, slope * point[0] - point[1]


def lines_are_close(image, line1, line2, epsilon_shift):
    # given two parallel/near-parallel lines, return whether their distance apart is < epsilon at the image's midpoint
    height, width = image.shape[0], image.shape[1]
    perpendicular_slope = -1 / slope(line1)
    perpendicular_line = line_from_point_and_slope(
        (width / 2, height / 2), perpendicular_slope
    )

    p1 = intersection(perpendicular_line, line1)
    p2 = intersection(perpendicular_line, line2)
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return (dx * dx + dy * dy) ** 0.5 < epsilon_shift


def standard_form_from_points(p1, p2):
    # returns the A, B, C in the equation Ax + By = C given 2 points

    if abs(p1[0] - p2[0]) < 0.00000001:
        return 1, 0, p1[0]

    slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
    return slope, -1, slope * p1[0] - p1[1]


def lines_to_angles(lines):
    # converts tuples in the form (A, B, C) for the equation Ax + By = C to
    # angles between [0, 2pi)

    angles = [atan2(-line[0], line[1]) for line in lines]
    for i, angle in enumerate(angles):
        if angle < 0:
            angles[i] = 2 * pi + angle
    # puts everything in the range [0, 2pi)
    return angles


def line_angle_difference(angle1, angle2):
    # given two angles between 0 and 2*pi, find the smallest angle between them
    angle_diff1 = 2 * pi - max(angle1, angle2) + min(angle1, angle2)
    angle_diff2 = max(angle1, angle2) - min(angle1, angle2)

    angle3 = (angle1 + pi) % (2 * pi)

    angle_diff3 = 2 * pi - max(angle3, angle2) + min(angle3, angle2)
    angle_diff4 = max(angle3, angle2) - min(angle3, angle2)

    return min(angle_diff1, angle_diff2, angle_diff3, angle_diff4)


def calculate_angular_mse(axis1, axis2, angles_list):
    mse = 0.0  # mean squared error
    for rad in angles_list:
        diff1 = line_angle_difference(rad, axis1)
        diff2 = line_angle_difference(rad, axis2)
        dt_from_closest_axis = min(diff1, diff2)
        mse += dt_from_closest_axis * dt_from_closest_axis
    return mse


def fit_perpendicular_axes(angles_list, iterations=20, d_theta=pi / 6):
    current_angle = random_choice(angles_list)
    perpendicular_axis = current_angle + pi / 2

    for _ in range(iterations):
        error1 = calculate_angular_mse(
            current_angle + d_theta, perpendicular_axis + d_theta, angles_list
        )
        error2 = calculate_angular_mse(
            current_angle - d_theta, perpendicular_axis - d_theta, angles_list
        )
        if error1 < error2:
            current_angle += d_theta
        else:
            current_angle -= d_theta
        perpendicular_axis = current_angle + pi / 2
        d_theta /= 2

    return current_angle, perpendicular_axis


def plot_lines_and_axes_and_average(angles_list, fit_axes, averaged_angles):
    # plotter formatting
    fig_size = plt.rcParams["figure.figsize"]
    fig_size[0] = 30
    fig_size[1] = 16
    plt.rcParams["figure.figsize"] = fig_size

    axes = plt.gca()
    axes.set_xlim([-5, 5])
    axes.set_ylim([-5, 5])
    font = {"family": "Consolas", "weight": "normal", "size": 35}
    rc("font", **font)

    # plotting and labelling the data
    line_width = 3
    plt.plot([], [], ":r", label="Measured Angles", linewidth=line_width)
    for angle in angles_list:
        x = linspace(-5, 5, 100)
        y = tan(angle) * x
        plt.plot(x, y, ":r", linewidth=line_width)

    plt.plot([], [], "--g", label="M.S.E Fit Axis", linewidth=line_width)
    for axis in fit_axes:
        x = linspace(-5, 5, 100)
        y = tan(axis) * x
        plt.plot(x, y, "--g", linewidth=line_width)

    plt.plot([], [], "-b", label="Average of lines near axes", linewidth=line_width)
    for avg_angle in averaged_angles:
        x = linspace(-5, 5, 100)
        y = tan(avg_angle) * x
        plt.plot(x, y, "-b", linewidth=line_width)

    # setup and show plot
    plt.title("Angles Graph")
    plt.legend(loc="upper left")
    plt.grid()
    plt.show()


def cluster_lines_around_axes(lines: list, axes: list):
    d = {axis: [] for axis in axes}
    for line in lines:
        closest_axis = min(axes, key=lambda axis: line_angle_difference(line, axis))
        d[closest_axis] += [line]
    return d


def average_angles(angles: list):
    return sum(a if a < pi else a - pi for a in angles) / len(angles)


if __name__ == "__main__":
    img = imread("string.jpg")
    height, width, channels = img.shape
    hsv = cvtColor(img, COLOR_BGR2HSV)

    target_rgb = [202, 137, 139]
    hsv_unscaled = rgb_to_hsv(*target_rgb)
    target_hsv = [
        int(hsv_unscaled[0] * 255),
        int(hsv_unscaled[1] * 255),
        hsv_unscaled[2],
    ]

    thresh = 100
    lower_pink = array(
        [target_hsv[0] - thresh, target_hsv[1] - thresh, target_hsv[2] - thresh]
    )  # in HSV
    upper_pink = array(
        [target_hsv[0] + thresh, target_hsv[1] + thresh, target_hsv[2] + thresh]
    )  # in HSV

    black_and_white_image = inRange(hsv, lower_pink, upper_pink)
    base_colored_image = bitwise_and(img, img, mask=black_and_white_image)

    show("Original", img)
    show("Pink", base_colored_image)
    show("Black and White", black_and_white_image)

    edges = Canny(black_and_white_image, 50, 150)
    show("After canny", edges)
    lines = HoughLines(edges, 1, pi / 180.0, 250, array([]), 0, 0)

    a, b, c = lines.shape
    print(f"Number of Lines before filtering: {a}")
    unique_lines = []
    for i in range(a):
        rho = lines[i][0][0]
        theta = lines[i][0][1]
        a1 = cos(theta)
        b1 = sin(theta)
        x0, y0 = a1 * rho, b1 * rho
        pt1 = int(x0 - width * b1), int(y0 + height * a1)
        pt2 = int(x0 + width * b1), int(y0 - height * a1)

        line_equation = standard_form_from_points(pt1, pt2)
        if not contains_similar_line(
            img, unique_lines, line_equation, epsilon_angle=0.15, epsilon_shift=20
        ):
            unique_lines += [line_equation]
            line(img, pt1, pt2, (255, 0, 0), 3, LINE_AA)

    print(f"Number of lines after filtering={len(unique_lines)}")
    show("Unique lines transposed on image", img)

    angles = lines_to_angles(unique_lines)
    axis1, axis2 = fit_perpendicular_axes(angles)
    line_cluster = cluster_lines_around_axes(angles, [axis1, axis2])
    averaged_cluster = {
        average_angles(line_cluster[axis]): line_cluster[axis] for axis in line_cluster
    }

    print("Angles from lines:", angles)
    print("Line Cluster:", line_cluster)
    print("Axes:", [axis1, axis2])
    print("Averages Of Cluster:", *averaged_cluster.keys())

    rads_off_course = min(averaged_cluster.items(), key=lambda x: len(x[1]))[0] - pi / 2
    print(f"The ROV is {rads_off_course} radians off course counter-clockwise")

    plot_lines_and_axes_and_average(angles, [axis1, axis2], averaged_cluster.keys())
