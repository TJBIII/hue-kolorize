from hkolorize import process_img

from os.path import join, dirname
from PIL import Image
from pytest import approx

def test_get_colors_returns_cluster_results(mocker):
    mock_cluster_centers = [ [0, 0, 255], [12, 124, 3], [0, 0, 0] ]
    mocker.patch('hkolorize.process_img.cluster', return_value=(mock_cluster_centers, mock_cluster_centers[1]))

    # Given
    img_path = join(dirname(__file__), 'img/four_lines.jpg')
    img = Image.open(img_path)

    # When
    cluster_centers, dominant_color = process_img.get_colors(img, 3)

    # Then
    assert len(cluster_centers) == 3
    assert cluster_centers == mock_cluster_centers
    assert dominant_color == [12, 124, 3]


def test_get_colors(mocker):
    # Given
    img_path = join(dirname(__file__), 'img/four_lines.jpg')
    img = Image.open(img_path)

    # When
    cluster_centers, dominant_color = process_img.get_colors(img, 3)

    # Then
    assert len(cluster_centers) == 3
    assert dominant_color == approx([236.3, 27.3, 36.3], rel=0.1)
