def __init__():
    global point,path,dic
    point = {'A' : [[1, 'C', 0.000000, -0.000000, 0.000000, 0], [2, 'N', -0.821020, -0.006354, 0.000000, 0], [3, 'H', -1.601020, -0.006354, 0.000000, 0, 'VAL=1'], [4, 'H', -0.821020, -0.786354, 0.000000, 0, 'VAL=1'], [5, 'O', 0.779999, 0.779999, 0.000000, 0], [6, 'C', 0.779999, -0.000000, 0.000000, 0], [7, 'O', 1.559999, -0.000000, 0.000000, 0, 'HCOUNT=1'], [8, 'C', -0.000000, -0.779999, 0.000000, 0, 'HCOUNT=3'], [9, 'H', -0.003147, 0.779993, 0.000000, 0, 'VAL=1']],
            'S' : [[1, 'C', 0.000000, -0.000000, 0.000000, 0], [2, 'N', -0.821020, -0.006354, 0.000000, 0], [3, 'H', -1.601020, -0.006354, 0.000000, 0, 'VAL=1'], [4, 'H', -0.821020, -0.786354, 0.000000, 0, 'VAL=1'], [5, 'O', 0.779999, 0.779999, 0.000000, 0], [6, 'C', 0.779999, -0.000000, 0.000000, 0], [7, 'O', 1.559999, -0.000000, 0.000000, 0, 'HCOUNT=1'], [8, 'H', -0.003147, 0.779993, 0.000000, 0, 'VAL=1'], [9, 'C', -0.000000, -0.779999, 0.000000, 0, 'HCOUNT=2'], [10, 'O', 0.779999, -0.779999, 0.000000, 0, 'HCOUNT=1']],
            'L' : [[1, 'C', 0.000000, -0.000000, 0.000000, 0], [2, 'N', -0.821020, -0.006354, 0.000000, 0], [3, 'H', -1.601020, -0.006354, 0.000000, 0, 'VAL=1'], [4, 'H', -0.821020, -0.786354, 0.000000, 0, 'VAL=1'], [5, 'O', 0.779999, 0.779999, 0.000000, 0], [6, 'C', 0.779999, -0.000000, 0.000000, 0], [7, 'O', 1.559999, -0.000000, 0.000000, 0, 'HCOUNT=1'], [8, 'H', -0.003147, 0.779993, 0.000000, 0, 'VAL=1'], [9, 'C', -0.672859, -2.130937, 0.000000, 0, 'HCOUNT=3'], [10, 'C', 0.002640, -1.740937, 0.000000, 0, 'HCOUNT=1'], [11, 'C', 0.678140, -2.130937, 0.000000, 0, 'HCOUNT=3'], [12, 'C', -0.000000, -0.779999, 0.000000, 0, 'HCOUNT=2']],
            'C' : [[1, 'C', 0.000000, -0.000000, 0.000000, 0], [2, 'N', -0.821020, -0.006354, 0.000000, 0], [3, 'H', -1.601020, -0.006354, 0.000000, 0, 'VAL=1'], [4, 'H', -0.821020, -0.786354, 0.000000, 0, 'VAL=1'], [5, 'O', 0.779999, 0.779999, 0.000000, 0], [6, 'C', 0.779999, -0.000000, 0.000000, 0], [7, 'O', 1.559999, -0.000000, 0.000000, 0, 'HCOUNT=1'], [8, 'H', -0.003147, 0.779993, 0.000000, 0, 'VAL=1'], [9, 'C', -0.000000, -0.779999, 0.000000, 0, 'HCOUNT=2'], [10, 'S', 0.779999, -0.779999, 0.000000, 0, 'HCOUNT=1']],
            'D' : [[1, 'C', 0.000000, -0.000000, 0.000000, 0], [2, 'N', -0.821020, -0.006354, 0.000000, 0], [3, 'H', -1.601020, -0.006354, 0.000000, 0, 'VAL=1'], [4, 'H', -0.821020, -0.786354, 0.000000, 0, 'VAL=1'], [5, 'O', 0.779999, 0.779999, 0.000000, 0], [6, 'C', 0.779999, -0.000000, 0.000000, 0], [7, 'O', 1.559999, -0.000000, 0.000000, 0, 'HCOUNT=1'], [8, 'C', -0.000000, -0.779999, 0.000000, 0, 'HCOUNT=2'], [9, 'H', -0.003147, 0.779993, 0.000000, 0, 'VAL=1'], [10, 'O', -0.000000, -1.559999, 0.000000, 0], [11, 'C', -0.000000, -1.559999, 0.000000, 0], [12, 'O', -0.000000, -1.559999, 0.000000, 0, 'HCOUNT=1']],
            'N' : [[1, 'C', 0.000000, -0.000000, 0.000000, 0], [2, 'N', -0.821020, -0.006354, 0.000000, 0], [3, 'H', -1.601020, -0.006354, 0.000000, 0, 'VAL=1'], [4, 'H', -0.821020, -0.786354, 0.000000, 0, 'VAL=1'], [5, 'O', 0.779999, 0.779999, 0.000000, 0], [6, 'C', 0.779999, -0.000000, 0.000000, 0], [7, 'O', 1.559999, -0.000000, 0.000000, 0, 'HCOUNT=1'], [8, 'C', -0.000000, -0.779999, 0.000000, 0, 'HCOUNT=2'], [9, 'H', -0.003147, 0.779993, 0.000000, 0, 'VAL=1'], [10, 'C', -0.000000, -1.559999, 0.000000, 0], [11, 'O', -0.675499, -1.949999, 0.000000, 0], [12, 'N', 0.675653, -1.949733, 0.000000, 0, 'HCOUNT=2']],
            'I' : [[1, 'C', 0.000000, -0.000000, 0.000000, 0], [2, 'N', -0.821020, -0.006354, 0.000000, 0], [3, 'H', -1.601020, -0.006354, 0.000000, 0, 'VAL=1'], [4, 'H', -0.821020, -0.786354, 0.000000, 0, 'VAL=1'], [5, 'O', 0.779999, 0.779999, 0.000000, 0], [6, 'C', 0.779999, -0.000000, 0.000000, 0], [7, 'O', 1.559999, -0.000000, 0.000000, 0, 'HCOUNT=1'], [8, 'H', -0.003147, 0.779993, 0.000000, 0, 'VAL=1'], [9, 'C', -0.672859, -2.130937, 0.000000, 0, 'HCOUNT=2'], [10, 'C', 0.002640, -1.740937, 0.000000, 0, 'HCOUNT=1'], [11, 'C', 0.678140, -2.130937, 0.000000, 0, 'HCOUNT=3'], [12, 'C', -0.000000, -0.779999, 0.000000, 0, 'HCOUNT=2'], [13, 'C', -0.672859, -2.910937, 0.000000, 0, 'HCOUNT=3']],
            'G' : [[1, 'C', 0.000000, -0.000000, 0.000000, 0], [2, 'N', -0.821020, -0.006354, 0.000000, 0], [3, 'H', -1.601020, -0.006354, 0.000000, 0, 'VAL=1'], [4, 'H', -0.821020, -0.786354, 0.000000, 0, 'VAL=1'], [5, 'O', 0.779999, 0.779999, 0.000000, 0], [6, 'C', 0.779999, -0.000000, 0.000000, 0], [7, 'O', 1.559999, -0.000000, 0.000000, 0, 'HCOUNT=1'], [8, 'H', -0.000000, -0.779999, 0.000000, 0, 'VAL=1'], [9, 'H', -0.003147, 0.779993, 0.000000, 0, 'VAL=1]']],
            'R' : [[1, 'C', 0.000000, -0.000000, 0.000000, 0], [2, 'C', 0.779999, -0.000000, 0.000000, 0], [3, 'O', 0.779999, 0.779999, 0.000000, 0], [4, 'O', 1.559998, -0.000000, 0.000000, 0, 'HCOUNT=1'], [5, 'N', -0.821020, -0.006354, 0.000000, 0], [6, 'H', -1.601019, -0.006354, 0.000000, 0, 'VAL=1'], [7, 'H', -0.821020, -0.786354, 0.000000, 0, 'VAL=1'], [8, 'H', -0.003147, 0.779991, 0.000000, 0, 'VAL=1'], [9, 'C', 0.003351, -0.779992, 0.000000, 0, 'HCOUNT=2'], [10, 'C', 0.003351, -1.559992, 0.000000, 0, 'HCOUNT=2'], [11, 'C', 0.003351, -2.339992, 0.000000, 0, 'HCOUNT=2'], [12, 'N', 0.003351, -3.119992, 0.000000, 0, 'HCOUNT=1'], [13, 'C', 0.003351, -3.899992, 0.000000, 0], [14, 'N', -0.672148, -4.289992, 0.000000, 0, 'HCOUNT=1'], [15, 'N', 0.679004, -4.289725, 0.000000, 0, 'HCOUNT=2']],
            'H' : [[1, 'C', 0.372154, -2.792851, 0.000000, 0, 'HCOUNT=1'], [2, 'N', -0.407784, -2.783275, 0.000000, 0], [3, 'H', -0.873898, -3.408684, 0.000000, 0, 'VAL=1'], [4, 'C', -0.639692, -2.038547, 0.000000, 0, 'HCOUNT=1'], [5, 'N', 0.622280, -2.054046, 0.000000, 0], [6, 'C', 0.000000, -0.000000, 0.000000, 0], [7, 'N', -0.821020, -0.006354, 0.000000, 0],  [8, 'H', -1.601020, -0.006354, 0.000000, 0, 'VAL=1'], [9, 'H', -0.821020, -0.786354, 0.000000, 0, 'VAL=1'], [10, 'O', 0.779999, 0.779999, 0.000000, 0], [11, 'C', 0.779999, -0.000000, 0.000000, 0], [12, 'O', 1.559999, -0.000000, 0.000000, 0, 'HCOUNT=1'], [13, 'H', -0.003147, 0.779993, 0.000000, 0, 'VAL=1'], [14, 'C', -0.000000, -0.779999, 0.000000, 0, 'HCOUNT=2'], [15, 'C', -0.003076, -1.587858, 0.000000, 0]],
            'V' : [[1, 'C', 0.000000, -0.000000, 0.000000, 0], [2, 'N', -0.821020, -0.006354, 0.000000, 0], [3, 'H', -1.601020, -0.006354, 0.000000, 0, 'VAL=1'], [4, 'H', -0.821020, -0.786354, 0.000000, 0, 'VAL=1'], [5, 'O', 0.779999, 0.779999, 0.000000, 0], [6, 'C', 0.779999, -0.000000, 0.000000, 0], [7, 'O', 1.559999, -0.000000, 0.000000, 0, 'HCOUNT=1'], [8, 'C', -0.000000, -0.779999, 0.000000, 0, 'HCOUNT=1'], [9, 'H', -0.003147, 0.779993, 0.000000, 0, 'VAL=1'], [10, 'C', -0.390000, -1.455499, 0.000000, 0, 'HCOUNT=3'], [11, 'C', 0.389999, -1.455499, 0.000000, 0, 'HCOUNT=3']],
            'P' : [[1, 'C', 0.779999, -0.000000, 0.000000, 0], [2, 'O', 0.779999, 0.779999, 0.000000, 0], [3, 'O', 1.559998, -0.000000, 0.000000, 0, 'HCOUNT=1'], [4, 'C', -0.000000, 0.000000, 0.000000, 0, 'HCOUNT=1'], [5, 'N', -0.458473, -0.631033, 0.000000, 0, 'HCOUNT=1'], [6, 'C', -1.200297, -0.389999, 0.000000, 0, 'HCOUNT=2'], [7, 'C', -1.200297, 0.390000, 0.000000, 0, 'HCOUNT=2'], [8, 'C', -0.458473, 0.631033, 0.000000, 0, 'HCOUNT=2']],
            'W' : [[1, 'C', 0.000000, -0.000000, 0.000000, 0], [2, 'N', -0.821020, -0.006354, 0.000000, 0], [3, 'H', -1.601020, -0.006354, 0.000000, 0, 'VAL=1'], [4, 'H', -0.821020, -0.786354, 0.000000, 0, 'VAL=1'], [5, 'O', 0.779999, 0.779999, 0.000000, 0], [6, 'C', 0.779999, -0.000000, 0.000000, 0], [7, 'O', 1.559999, -0.000000, 0.000000, 0, 'HCOUNT=1'], [8, 'H', -0.003147, 0.779993, 0.000000, 0, 'VAL=1'], [9, 'C', -0.000000, -0.779999, 0.000000, 0, 'HCOUNT=2'], [10, 'C', -0.000000, -1.559999, 0.000000, 0], [11, 'C', -0.631033, -2.018472, 0.000000, 0, 'HCOUNT=1'], [12, 'C', 0.631033, -2.018472, 0.000000, 0], [13, 'C', 1.388429, -1.797894, 0.000000, 0, 'HCOUNT=1'], [14, 'C', 1.945017, -2.337296, 0.000000, 0, 'HCOUNT=1'], [15, 'C', 1.770667, -3.097277, 0.000000, 0, 'HCOUNT=1'], [16, 'C', 1.039729, -3.344313, 0.000000, 0, 'HCOUNT=1'], [17, 'N', -0.390000, -2.760296, 0.000000, 0], [18, 'C', 0.389999, -2.760296, 0.000000, 0], [19, 'H', -0.848399, -3.391382, 0.000000, 0, 'VAL=1']],
            'T' : [[1, 'C', 0.000000, -0.000000, 0.000000, 0], [2, 'N', -0.821020, -0.006354, 0.000000, 0], [3, 'H', -1.601020, -0.006354, 0.000000, 0, 'VAL=1'], [4, 'H', -0.821020, -0.786354, 0.000000, 0, 'VAL=1'], [5, 'O', 0.779999, 0.779999, 0.000000, 0], [6, 'C', 0.779999, -0.000000, 0.000000, 0], [7, 'O', 1.559999, -0.000000, 0.000000, 0, 'HCOUNT=1'], [8, 'H', -0.003147, 0.779993, 0.000000, 0, 'VAL=1'], [9, 'C', -0.000000, -0.779999, 0.000000, 0, 'HCOUNT=1'], [10, 'O', 0.779999, -0.779999, 0.000000, 0, 'HCOUNT=1'], [11, 'C', -0.000000, -1.559999, 0.000000, 0, 'HCOUNT=3']],
            'F' : [[1, 'C', 0.000000, -0.000000, 0.000000, 0], [2, 'N', -0.821020, -0.006354, 0.000000, 0], [3, 'H', -1.601020, -0.006354, 0.000000, 0, 'VAL=1'], [4, 'H', -0.821020, -0.786354, 0.000000, 0, 'VAL=1'], [5, 'O', 0.779999, 0.779999, 0.000000, 0], [6, 'C', 0.779999, -0.000000, 0.000000, 0], [7, 'O', 1.559999, -0.000000, 0.000000, 0, 'HCOUNT=1'], [8, 'C', -0.000000, -0.779999, 0.000000, 0, 'HCOUNT=2'], [9, 'C', -0.000000, -1.559999, 0.000000, 0], [10, 'C', 0.675499, -1.949999, 0.000000, 0, 'HCOUNT=1'], [11, 'C', 0.675499, -2.729999, 0.000000, 0, 'HCOUNT=1'], [12, 'C', -0.000000, -3.119999, 0.000000, 0, 'HCOUNT=1'], [13, 'C', -0.675499, -2.729999, 0.000000, 0, 'HCOUNT=1'], [14, 'C', -0.675499, -1.949999, 0.000000, 0, 'HCOUNT=1'], [15, 'H', -0.003147, 0.779993, 0.000000, 0, 'VAL=1']],
            'M' : [[1, 'C', 0.000000, -0.000000, 0.000000, 0], [2, 'N', -0.821020, -0.006354, 0.000000, 0], [3, 'H', -1.601020, -0.006354, 0.000000, 0, 'VAL=1'], [4, 'H', -0.821020, -0.786354, 0.000000, 0, 'VAL=1'], [5, 'O', 0.779999, 0.779999, 0.000000, 0], [6, 'C', 0.779999, -0.000000, 0.000000, 0], [7, 'O', 1.559999, -0.000000, 0.000000, 0, 'HCOUNT=1'], [8, 'H', -0.003147, 0.779993, 0.000000, 0, 'VAL=1'], [9, 'C', -0.000000, -0.779999, 0.000000, 0, 'HCOUNT=2'], [10, 'C', -0.000000, -1.559999, 0.000000, 0, 'HCOUNT=2'], [11, 'S', -0.000000, -2.339999, 0.000000, 0], [12, 'C', -0.000000, -3.119999, 0.000000, 0, 'HCOUNT=3']],
            'Q' : [[1, 'C', 0.000000, -0.000000, 0.000000, 0], [2, 'C', 0.779999, -0.000000, 0.000000, 0], [3, 'O', 0.779999, 0.779999, 0.000000, 0], [4, 'O', 1.559998, -0.000000, 0.000000, 0, 'HCOUNT=1'], [5, 'N', -0.821020, -0.006354, 0.000000, 0], [6, 'H', -1.601019, -0.006354, 0.000000, 0, 'VAL=1'], [7, 'H', -0.821020, -0.786354, 0.000000, 0, 'VAL=1'], [8, 'H', -0.003147, 0.779992, 0.000000, 0, 'VAL=1'], [9, 'C', 0.003351, -0.779992, 0.000000, 0, 'HCOUNT=2'], [10, 'C', 0.003351, -1.559992, 0.000000, 0, 'HCOUNT=2'], [11, 'O', -0.672148, -2.729992, 0.000000, 0], [12, 'C', 0.003351, -2.339992, 0.000000, 0], [13, 'N', 0.679004, -2.729725, 0.000000, 0, 'HCOUNT=2']],
            'E' : [[1, 'C', 0.000000, -0.000000, 0.000000, 0], [2, 'C', 0.779999, -0.000000, 0.000000, 0], [3, 'O', 0.779999, 0.779999, 0.000000, 0], [4, 'O', 1.559998, -0.000000, 0.000000, 0, 'HCOUNT=1'], [5, 'N', -0.821020, -0.006354, 0.000000, 0], [6, 'H', -1.601019, -0.006354, 0.000000, 0, 'VAL=1'], [7, 'H', -0.821020, -0.786354, 0.000000, 0, 'VAL=1'], [8, 'H', -0.003147, 0.779992, 0.000000, 0, 'VAL=1'], [9, 'C', 0.003351, -0.779992, 0.000000, 0, 'HCOUNT=2'], [10, 'C', 0.003351, -1.559992, 0.000000, 0, 'HCOUNT=2'], [11, 'O', -0.672148, -2.729992, 0.000000, 0], [12, 'C', 0.003351, -2.339992, 0.000000, 0], [13, 'O', 0.679004, -2.729725, 0.000000, 0, 'HCOUNT=1']],
            'K' : [[1, 'C', 0.000000, -0.000000, 0.000000, 0], [2, 'N', -0.821020, -0.006354, 0.000000, 0], [3, 'H', -1.601020, -0.006354, 0.000000, 0, 'VAL=1'], [4, 'H', -0.821020, -0.786354, 0.000000, 0, 'VAL=1'], [5, 'O', 0.779999, 0.779999, 0.000000, 0], [6, 'C', 0.779999, -0.000000, 0.000000, 0], [7, 'O', 1.559999, -0.000000, 0.000000, 0, 'HCOUNT=1'], [8, 'C', -0.000000, -0.779999, 0.000000, 0, 'HCOUNT=2'], [9, 'H', -0.003147, 0.779993, 0.000000, 0, 'VAL=1'], [10, 'C', -0.000000, -1.559999, 0.000000, 0, 'HCOUNT=2'], [11, 'C', 0.012416, -2.333645, 0.000000, 0,' HCOUNT=2'], [12, 'C', 0.012416, -3.113645, 0.000000, 0, 'HCOUNT=2'], [13, 'N', 0.012416, -3.893645, 0.000000, 0, 'HCOUNT=2']],
            'Y' : [[1, 'C', 0.000000, -0.000000, 0.000000, 0], [2, 'N', -0.821020, -0.006354, 0.000000, 0], [3, 'H', -1.601020, -0.006354, 0.000000, 0, 'VAL=1'], [4, 'H', -0.821020, -0.786354, 0.000000, 0, 'VAL=1'], [5, 'O', 0.779999, 0.779999, 0.000000, 0], [6, 'C', 0.779999, -0.000000, 0.000000, 0], [7, 'O', 1.559999, -0.000000, 0.000000, 0, 'HCOUNT=1'], [8, 'H', -0.003147, 0.779993, 0.000000, 0, 'VAL=1'], [9, 'C', -0.000000, -0.779999, 0.000000, 0, 'HCOUNT=2'], [10, 'C', -0.000000, -1.559999, 0.000000, 0], [11, 'C', 0.675499, -1.949999, 0.000000, 0, 'HCOUNT=1'], [12, 'C', 0.675499, -2.729999, 0.000000, 0, 'HCOUNT=1'], [13, 'C', -0.675499, -2.729999, 0.000000, 0, 'HCOUNT=1'], [14, 'C', -0.675499, -1.949999, 0.000000, 0, 'HCOUNT=1'], [15, 'C', -0.000000, -3.119999, 0.000000, 0], [16, 'O', 0.000307, -3.899999, 0.000000, 0, 'HCOUNT=1']]}
    path  = {'A' : [[1, 1, 1, 6], [2, 1, 1, 2], [3, 1, 2, 3], [4, 1, 2, 4], [5, 2, 6, 5], [6, 1, 6, 7], [7, 1, 1, 8], [8, 1, 1, 9]],
            'S' : [[1, 1, 1, 6], [2, 1, 1, 2], [3, 1, 2, 3], [4, 1, 2, 4], [5, 2, 6, 5], [6, 1, 6, 7], [7, 1, 1, 9], [8, 1, 1, 8], [9, 1, 9, 10]],
            'L' : [[1, 1, 1, 6], [2, 1, 1, 2], [3, 1, 2, 3], [4, 1, 2, 4], [5, 2, 6, 5], [6, 1, 6, 7], [7, 1, 1, 12], [8, 1, 1, 8], [9, 1, 9, 10], [10, 1, 10, 11], [11, 1, 10, 12]],
            'C' : [[1, 1, 1, 6], [2, 1, 1, 2], [3, 1, 2, 3], [4, 1, 2, 4], [5, 2, 6, 5], [6, 1, 6, 7], [7, 1, 1, 9], [8, 1, 1, 8], [9, 1, 9, 10]],
            'D' : [[1, 1, 1, 6], [2, 1, 1, 2], [3, 1, 2, 3], [4, 1, 2, 4], [5, 2, 6, 5], [6, 1, 6, 7], [7, 1, 1, 8], [8, 1, 1, 9], [9, 1, 8, 11], [10, 2, 11, 10], [11, 1, 11, 12]],
            'N' : [[1, 1, 1, 6], [2, 1, 1, 2], [3, 1, 2, 3], [4, 1, 2, 4], [5, 2, 6, 5], [6, 1, 6, 7], [7, 1, 1, 8], [8, 1, 1, 9], [9, 1, 8, 10], [10, 2, 10, 11], [11, 1, 10, 12]],
            'I' : [[1, 1, 1, 6], [2, 1, 1, 2], [3, 1, 2, 3], [4, 1, 2, 4], [5, 2, 6, 5], [6, 1, 6, 7], [7, 1, 1, 12], [8, 1, 1, 8], [9, 1, 9, 10], [10, 1, 10, 11], [11, 1, 10, 12], [12, 1, 9, 13]],
            'G' : [[1, 1, 1, 6], [2, 1, 1, 2], [3, 1, 2, 3], [4, 1, 2, 4], [5, 2, 6, 5], [6, 1, 6, 7], [7, 1, 1, 8], [8, 1, 1, 9]],
            'R' : [[1, 1, 1, 2], [2, 2, 2, 3], [3, 1, 2, 4], [4, 1, 1, 5], [5, 1, 5, 6], [6, 1, 5, 7], [7, 1, 1, 8], [8, 1, 1, 9], [9, 1, 9, 10], [10, 1, 10, 11], [11, 1, 11, 12], [12, 1, 12, 13], [13, 2, 13, 14], [14, 1, 13, 15]],
            'H' : [[1, 1, 1, 2], [2, 2, 5, 1], [3, 1, 2, 3], [4, 1, 2, 4], [5, 2, 4, 15], [6, 1, 15, 5], [7, 1, 6, 11], [8, 1, 6, 7], [9, 1, 7, 8], [10, 1, 7, 9], [11, 2, 11, 10], [12, 1, 11, 12], [13, 1, 6, 14], [14, 1, 6, 13], [15, 1, 14, 15]],
            'V' : [[1, 1, 1, 6], [2, 1, 1, 2], [3, 1, 2, 3], [4, 1, 2, 4], [5, 2, 6, 5], [6, 1, 6, 7], [7, 1, 1, 8], [8, 1, 1, 9], [9, 1, 8, 10], [10, 1, 8, 11]],
            'P' : [[1, 2, 1, 2], [2, 1, 1, 3], [3, 1, 1, 4], [4, 1, 4, 5], [5, 1, 5, 6], [6, 1, 6, 7], [7, 1, 7, 8], [8, 1, 8, 4]],
            'W' : [[1, 1, 1, 6], [2, 1, 1, 2], [3, 1, 2, 3], [4, 1, 2, 4], [5, 2, 6, 5], [6, 1, 6, 7], [7, 1, 1, 9], [8, 1, 1, 8], [9, 1, 9, 10], [10, 1, 10, 12], [11, 1, 17, 11], [12, 2, 11, 10], [13, 1, 12, 13], [14, 2, 13, 14], [15, 1, 14, 15], [16, 2, 15, 16], [17, 1, 16, 18], [18, 2, 18, 12], [19, 1, 17, 18], [20, 1, 17, 19]],
            'T' : [[1, 1, 1, 6], [2, 1, 1, 2], [3, 1, 2, 3], [4, 1, 2, 4], [5, 2, 6, 5], [6, 1, 6, 7], [7, 1, 1, 9], [8, 1, 1, 8], [9, 1, 9, 10], [10, 1, 9, 11]],
            'F' : [[1, 1, 1, 6], [2, 1, 1, 2], [3, 1, 2, 3], [4, 1, 2, 4], [5, 2, 6, 5], [6, 1, 6, 7], [7, 1, 1, 8], [8, 1, 8, 9], [9, 1, 9, 10], [10, 2, 10, 11], [11, 1, 11, 12], [12, 2, 12, 13], [13, 1, 13, 14], [14, 2, 14, 9], [15, 1, 1, 15]],
            'M' : [[1, 1, 1, 6], [2, 1, 1, 2], [3, 1, 2, 3], [4, 1, 2, 4], [5, 2, 6, 5], [6, 1, 6, 7], [7, 1, 1, 9], [8, 1, 1, 8], [9, 1, 9, 10], [10, 1, 10, 11], [11, 1, 11, 12]],
            'Q' : [[1, 1, 1, 2], [2, 2, 2, 3], [3, 1, 2, 4], [4, 1, 1, 5], [5, 1, 5, 6], [6, 1, 5, 7], [7, 1, 1, 8], [8, 1, 1, 9], [9, 1, 9, 10], [10, 1, 10, 12], [11, 2, 12, 11], [12, 1, 12, 13]],
            'E' : [[1, 1, 1, 2], [2, 2, 2, 3], [3, 1, 2, 4], [4, 1, 1, 5], [5, 1, 5, 6], [6, 1, 5, 7], [7, 1, 1, 8], [8, 1, 1, 9], [9, 1, 9, 10], [10, 1, 10, 12], [11, 2, 12, 11], [12, 1, 12, 13]],
            'K' : [[1, 1, 1, 6], [2, 1, 1, 2], [3, 1, 2, 3], [4, 1, 2, 4], [5, 2, 6, 5], [6, 1, 6, 7], [7, 1, 1, 8], [8, 1, 1, 9], [9, 1, 8, 10], [10, 1, 10, 11], [11, 1, 11, 12], [12, 1, 12, 13]],
            'Y' : [[1, 1, 1, 6], [2, 1, 1, 2], [3, 1, 2, 3], [4, 1, 2, 4], [5, 2, 6, 5], [6, 1, 6, 7], [7, 1, 1, 9], [8, 1, 1, 8], [9, 1, 9, 10], [10, 1, 10, 11], [11, 2, 11, 12], [12, 1, 12, 15], [13, 2, 15, 13], [14, 1, 13, 14], [15, 2, 14, 10], [16, 1, 15, 16]]}
    dic={'UUU':'F','UUC':'F','UUA':'L','UUG':'L','UCU':'S','UCC':'S','UCA':'S','UCG':'S','UAU':'Y','UAC':'Y','UAA':'.','UAG':'.','UGU':'C','UGC':'C','UGA':'.','UGG':'W',
        'CUU':'L','CUC':'L','CUA':'L','CUG':'L','CCU':'P','CCC':'P','CCA':'P','CCG':'P','CAU':'H','CAC':'H','CAA':'Q','CAG':'Q','CGU':'R','CGC':'R','CGA':'R','CGG':'R',
        'AUU':'I','AUC':'I','AUA':'I','AUG':'M','ACU':'T','ACC':'T','ACA':'T','ACG':'T','AAU':'N','AAC':'N','AAA':'K','AAG':'K','AGU':'S','AGC':'S','AGA':'R','AGG':'R',
        'GUU':'V','GUC':'V','GUA':'V','GUG':'V','GCU':'A','GCC':'A','GCA':'A','GCG':'A','GAU':'D','GAC':'D','GAA':'E','GAG':'E','GGU':'G','GGC':'G','GGA':'G','GGG':'G'}

def encoding(key):
    global point,path,dic
    ret = {}
    num = int(str(key.encode('utf-8').hex()),16)
    cd4 = ''
    while num != 0:
        cd4 = str(num%4) + cd4
        num = num // 4
    code = cd4.replace('0','U').replace('1','C').replace('2','A').replace('3','G')
    if len(code)%3 != 0:code = 'U'*(3-(len(code)%3)) + code
    code = 'AUG' + code
    out  = ''
    mrna = ''
    rna  = ''
    for i in range(len(code)//3):
        if dic[code[i*3:(i+1)*3]] != '.':piece = code[i*3:(i+1)*3]
        else:piece = code[i*3:(i+1)*3].replace('U','u').replace('A','a').replace('G','g').replace('C','c').replace('u','A').replace('a','U').replace('g','C').replace('c','G')
        out = out + dic[piece]
        mrna = mrna + piece
        rna = rna + piece.replace('U','u').replace('A','a').replace('G','g').replace('C','c').replace('u','A').replace('a','U').replace('g','C').replace('c','G')
    mrna = mrna + 'UAG'
    rna = rna + 'AUC'
    dna = [rna.replace('U','T'),mrna.replace('U','T')[::-1]]
    if len(out) < 2:raise Exception("Input is too short to translate.",key)
    ret['DeoxyriboNucleic Acid'] = dna
    ret['Messenger Ribonucleic Acid'] = mrna
    #out = 'FLSYCIMVPTAHQNKDERSG'
    chempoint = []
    chempath  = []
    connect   = []
    connected = []
    if out[0] == 'P':
        k = 0
        dy = {}
        for data in point['P']:
            if data[0] == 3:
                connect.append(str(k-1))
            else:
                k += 1
                dy[data[0]]=k
                if len(data) == 7:chempoint.append(str(k)+' '+str(data[1])+' '+str(data[2])+' '+str(data[3])+' '+str(data[4])+' '+str(data[5])+' '+data[6])
                elif len(data) == 6:chempoint.append(str(k)+' '+str(data[1])+' '+str(data[2])+' '+str(data[3])+' '+str(data[4])+' '+str(data[5]))
        k = 0
        for pth in path['P']:
            if 3 == pth[2] or 3 == pth[3]:pass
            else:
                k += 1
                p2 = dy[pth[2]]
                p3 = dy[pth[3]]
                chempath.append(str(k)+' '+str(pth[1])+' '+str(p2)+' '+str(p3))
    else:
        k = 0
        af = 7
        add = 0
        if out[0] == 'H':af = 12
        if out[0] == 'E' or out[0] == 'Q' or out[0] == 'R':
            af = 4
            add = -1
        dy = {}
        for data in point[out[0]]:
            if data[0] == af:
                connect.append(str(k+add))
            else:
                k += 1
                dy[data[0]]=k
                if len(data) == 7:chempoint.append(str(k)+' '+str(data[1])+' '+str(data[2])+' '+str(data[3])+' '+str(data[4])+' '+str(data[5])+' '+data[6])
                elif len(data) == 6:chempoint.append(str(k)+' '+str(data[1])+' '+str(data[2])+' '+str(data[3])+' '+str(data[4])+' '+str(data[5]))
        k = 0
        for pth in path[out[0]]:
            if af == pth[2] or af == pth[3]:pass
            else:
                k += 1
                p2 = dy[pth[2]]
                p3 = dy[pth[3]]
                chempath.append(str(k)+' '+str(pth[1])+' '+str(p2)+' '+str(p3))
    count = 0
    for n in out[1:-1]:
        count += 1
        basepath = len(chempath)
        basepoint = len(chempoint)
        if n == 'P':
            k = 0
            dy = {}
            for data in point['P']:
                if data[0] == 3:
                    connect.append(str(k+basepoint-1))
                elif data[0] == 5:
                    k += 1
                    dy[data[0]]=k+basepoint
                    chempoint.append(str(k+basepoint)+' '+str(data[1])+' '+str(round(data[2]+2.4*count,6))+' '+str(data[3])+' '+str(data[4])+' '+str(data[5]))
                    connected.append([connect.pop(0),k+basepoint])
                else:
                    k += 1
                    dy[data[0]]=k+basepoint
                    if len(data) == 7:chempoint.append(str(k+basepoint)+' '+str(data[1])+' '+str(round(data[2]+2.4*count,6))+' '+str(data[3])+' '+str(data[4])+' '+str(data[5])+' '+data[6])
                    elif len(data) == 6:chempoint.append(str(k+basepoint)+' '+str(data[1])+' '+str(round(data[2]+2.4*count,6))+' '+str(data[3])+' '+str(data[4])+' '+str(data[5]))
            k = 0
            for pth in path['P']:
                if 3 == pth[2] or 3 == pth[3]:pass
                else:
                    k += 1
                    p2 = dy[pth[2]]
                    p3 = dy[pth[3]]
                    chempath.append(str(k+basepath)+' '+str(pth[1])+' '+str(p2)+' '+str(p3))
        else:
            bf = 3
            af = 7
            add = 0
            if n == 'H':
                af = 12
                bf = 8
            if n == 'E' or n == 'Q' or n == 'R':
                bf = 6
                af = 4
                add = -1
            k = 0
            dy = {}
            for data in point[n]:
                if data[0] == af:
                    connect.append(str(k+basepoint+add))
                elif data[0] == bf:connected.append([connect.pop(0),k+basepoint])
                else:
                    k += 1
                    dy[data[0]]=k+basepoint
                    if len(data) == 7:chempoint.append(str(k+basepoint)+' '+str(data[1])+' '+str(round(data[2]+2.4*count,6))+' '+str(data[3])+' '+str(data[4])+' '+str(data[5])+' '+data[6])
                    elif len(data) == 6:chempoint.append(str(k+basepoint)+' '+str(data[1])+' '+str(round(data[2]+2.4*count,6))+' '+str(data[3])+' '+str(data[4])+' '+str(data[5]))
            k = 0
            for pth in path[n]:
                if af == pth[2] or af == pth[3] or bf == pth[2] or bf == pth[3]:pass
                else:
                    k += 1
                    p2 = dy[pth[2]]
                    p3 = dy[pth[3]]
                    chempath.append(str(k+basepath)+' '+str(pth[1])+' '+str(p2)+' '+str(p3))
    basepath = len(chempath)
    basepoint = len(chempoint)
    #print(basepath)
    count += 1
    if out[-1] == 'P':
        k = 0
        dy = {}
        for data in point['P']:
            if data[0] == 5:
                k += 1
                dy[data[0]]=k+basepoint
                chempoint.append(str(k+basepoint)+' '+str(data[1])+' '+str(round(data[2]+2.4*count,6))+' '+str(data[3])+' '+str(data[4])+' '+str(data[5]))
                connected.append([connect.pop(0),k+basepoint])
            else:
                k += 1
                dy[data[0]]=k+basepoint
                if len(data) == 7:chempoint.append(str(k+basepoint)+' '+str(data[1])+' '+str(round(data[2]+2.4*count,6))+' '+str(data[3])+' '+str(data[4])+' '+str(data[5])+' '+data[6])
                elif len(data) == 6:chempoint.append(str(k+basepoint)+' '+str(data[1])+' '+str(round(data[2]+2.4*count,6))+' '+str(data[3])+' '+str(data[4])+' '+str(data[5]))
        k = 0
        for pth in path['P']:
            k += 1
            p2 = dy[pth[2]]
            p3 = dy[pth[3]]
            chempath.append(str(k+basepath)+' '+str(pth[1])+' '+str(p2)+' '+str(p3))

    else:
        bf = 3
        if out[-1] == 'H':bf = 8
        if out[-1] == 'E' or out[-1] == 'Q' or out[-1] == 'R':bf = 6
        k = 0
        dy = {}
        for data in point[out[-1]]:
            if data[0] == bf:connected.append([connect.pop(0),k+basepoint])
            else:
                k += 1
                dy[data[0]]=k+basepoint
                if len(data) == 7:chempoint.append(str(k+basepoint)+' '+str(data[1])+' '+str(round(data[2]+2.4*count,6))+' '+str(data[3])+' '+str(data[4])+' '+str(data[5])+' '+data[6])
                elif len(data) == 6:chempoint.append(str(k+basepoint)+' '+str(data[1])+' '+str(round(data[2]+2.4*count,6))+' '+str(data[3])+' '+str(data[4])+' '+str(data[5]))
        k = 0
        for pth in path[out[-1]]:
            if bf == pth[2] or bf == pth[3]:pass
            else:
                k += 1
                p2 = dy[pth[2]]
                p3 = dy[pth[3]]
                chempath.append(str(k+basepath)+' '+str(pth[1])+' '+str(p2)+' '+str(p3))
    basepath = len(chempath)
    for k,num in zip(range(1,len(connected)+1,1),connected):chempath.append(str(k+basepath)+' 1 '+str(num[0])+' '+str(num[1]))

    grand = open('./'+str(key)+'_t.mol','w')
    grand.write(''' \nKingDraw2D\n\n  0  0  0     0  0              0 V3000\nM  V30 BEGIN CTAB\n''')
    grand.write('M  V30 COUNTS '+str(len(chempoint))+' '+str(len(chempath))+' 0 0 0\n')
    grand.write('M  V30 BEGIN ATOM\n')
    for d in chempoint:grand.write('M  V30 '+d+'\n')
    grand.write('M  V30 END ATOM\nM  V30 BEGIN BOND\n')
    for d in chempath:grand.write('M  V30 '+d+'\n')
    grand.write('M  V30 END BOND\nM  V30 END CTAB\nM  END\n')
    grand.close()
    counting = {'H':0,'C':0}
    for d in chempoint:
        im = d.split(' ')
        try:
            if len(im) == 7 and 'H' in im[6]:counting['H']+=int(im[6][-1:])
            counting[im[1]] += 1
        except:counting[im[1]] = 1
    chem = ''
    for kkey in counting.keys():
        chem = chem + kkey+ str(counting[kkey]) + ' '
    ret['Chemical formula'] = chem
    poly = ''
    for d in out:poly = poly + d + '-'
    ret['polypeptide'] = poly[:-1]
    grand = open('./'+str(key)+'_d.txt','w')
    for rekey in ret.keys():grand.write(rekey + (27-len(rekey))*' ' + ' : ' + str(ret[rekey]).replace("'","").replace('[','').replace(']','') + '\n')
    grand.close()
    return ret

def long_encoding(key):
    global point,path,dic
    ret = {}
    num = int(str(key.encode('utf-8').hex()),16)
    cd4 = ''
    while num != 0:
        cd4 = str(num%4) + cd4
        num = num // 4
    code = cd4.replace('0','U').replace('1','C').replace('2','A').replace('3','G')
    if len(code)%3 != 0:code = 'U'*(3-(len(code)%3)) + code
    code = 'AUG' + code
    mrna = ''
    rna  = ''
    moremrna = ''
    for i in range(len(code)//3):
        if dic[code[i*3:(i+1)*3]] == '.':
            piece = code[i*3:(i+1)*3].replace('U','u').replace('A','a').replace('G','g').replace('C','c').replace('u','A').replace('a','U').replace('g','C').replace('c','G')
            moremrna = moremrna + 'A'
        elif code[i*3:(i+1)*3] in ['AUU','AUC','ACU']:
            piece = code[i*3:(i+1)*3]
            moremrna = moremrna + 'C'
        else:piece = code[i*3:(i+1)*3]
        mrna = mrna + piece
    if len(moremrna)%3 != 0:moremrna = 'G'*(3-(len(moremrna)%3)) + moremrna
    polymrna = mrna + moremrna
    latemrna = 'UU' + polymrna[3:] + 'U'
    mrna = polymrna + latemrna
    out  = ''
    for i in range(len(mrna)//3):
        piece = mrna[i*3:(i+1)*3]
        out = out + dic[piece]
    mrna = mrna + 'UAG'
    rna = mrna.replace('U','u').replace('A','a').replace('G','g').replace('C','c').replace('u','A').replace('a','U').replace('g','C').replace('c','G')
    dna = [rna.replace('U','T'),mrna.replace('U','T')[::-1]]
    if len(out) < 2:raise Exception("Input is too short to translate.",key)
    ret['DeoxyriboNucleic Acid'] = dna
    ret['Messenger Ribonucleic Acid'] = mrna
    #out = 'FLSYCIMVPTAHQNKDERSG'
    chempoint = []
    chempath  = []
    connect   = []
    connected = []
    if out[0] == 'P':
        k = 0
        dy = {}
        for data in point['P']:
            if data[0] == 3:
                connect.append(str(k-1))
            else:
                k += 1
                dy[data[0]]=k
                if len(data) == 7:chempoint.append(str(k)+' '+str(data[1])+' '+str(data[2])+' '+str(data[3])+' '+str(data[4])+' '+str(data[5])+' '+data[6])
                elif len(data) == 6:chempoint.append(str(k)+' '+str(data[1])+' '+str(data[2])+' '+str(data[3])+' '+str(data[4])+' '+str(data[5]))
        k = 0
        for pth in path['P']:
            if 3 == pth[2] or 3 == pth[3]:pass
            else:
                k += 1
                p2 = dy[pth[2]]
                p3 = dy[pth[3]]
                chempath.append(str(k)+' '+str(pth[1])+' '+str(p2)+' '+str(p3))
    else:
        k = 0
        af = 7
        add = 0
        if out[0] == 'H':af = 12
        if out[0] == 'E' or out[0] == 'Q' or out[0] == 'R':
            af = 4
            add = -1
        dy = {}
        for data in point[out[0]]:
            if data[0] == af:
                connect.append(str(k+add))
            else:
                k += 1
                dy[data[0]]=k
                if len(data) == 7:chempoint.append(str(k)+' '+str(data[1])+' '+str(data[2])+' '+str(data[3])+' '+str(data[4])+' '+str(data[5])+' '+data[6])
                elif len(data) == 6:chempoint.append(str(k)+' '+str(data[1])+' '+str(data[2])+' '+str(data[3])+' '+str(data[4])+' '+str(data[5]))
        k = 0
        for pth in path[out[0]]:
            if af == pth[2] or af == pth[3]:pass
            else:
                k += 1
                p2 = dy[pth[2]]
                p3 = dy[pth[3]]
                chempath.append(str(k)+' '+str(pth[1])+' '+str(p2)+' '+str(p3))
    count = 0
    for n in out[1:-1]:
        count += 1
        basepath = len(chempath)
        basepoint = len(chempoint)
        if n == 'P':
            k = 0
            dy = {}
            for data in point['P']:
                if data[0] == 3:
                    connect.append(str(k+basepoint-1))
                elif data[0] == 5:
                    k += 1
                    dy[data[0]]=k+basepoint
                    chempoint.append(str(k+basepoint)+' '+str(data[1])+' '+str(round(data[2]+2.4*count,6))+' '+str(data[3])+' '+str(data[4])+' '+str(data[5]))
                    connected.append([connect.pop(0),k+basepoint])
                else:
                    k += 1
                    dy[data[0]]=k+basepoint
                    if len(data) == 7:chempoint.append(str(k+basepoint)+' '+str(data[1])+' '+str(round(data[2]+2.4*count,6))+' '+str(data[3])+' '+str(data[4])+' '+str(data[5])+' '+data[6])
                    elif len(data) == 6:chempoint.append(str(k+basepoint)+' '+str(data[1])+' '+str(round(data[2]+2.4*count,6))+' '+str(data[3])+' '+str(data[4])+' '+str(data[5]))
            k = 0
            for pth in path['P']:
                if 3 == pth[2] or 3 == pth[3]:pass
                else:
                    k += 1
                    p2 = dy[pth[2]]
                    p3 = dy[pth[3]]
                    chempath.append(str(k+basepath)+' '+str(pth[1])+' '+str(p2)+' '+str(p3))
        else:
            bf = 3
            af = 7
            add = 0
            if n == 'H':
                af = 12
                bf = 8
            if n == 'E' or n == 'Q' or n == 'R':
                bf = 6
                af = 4
                add = -1
            k = 0
            dy = {}
            for data in point[n]:
                if data[0] == af:
                    connect.append(str(k+basepoint+add))
                elif data[0] == bf:connected.append([connect.pop(0),k+basepoint])
                else:
                    k += 1
                    dy[data[0]]=k+basepoint
                    if len(data) == 7:chempoint.append(str(k+basepoint)+' '+str(data[1])+' '+str(round(data[2]+2.4*count,6))+' '+str(data[3])+' '+str(data[4])+' '+str(data[5])+' '+data[6])
                    elif len(data) == 6:chempoint.append(str(k+basepoint)+' '+str(data[1])+' '+str(round(data[2]+2.4*count,6))+' '+str(data[3])+' '+str(data[4])+' '+str(data[5]))
            k = 0
            for pth in path[n]:
                if af == pth[2] or af == pth[3] or bf == pth[2] or bf == pth[3]:pass
                else:
                    k += 1
                    p2 = dy[pth[2]]
                    p3 = dy[pth[3]]
                    chempath.append(str(k+basepath)+' '+str(pth[1])+' '+str(p2)+' '+str(p3))
    basepath = len(chempath)
    basepoint = len(chempoint)
    #print(basepath)
    count += 1
    if out[-1] == 'P':
        k = 0
        dy = {}
        for data in point['P']:
            if data[0] == 5:
                k += 1
                dy[data[0]]=k+basepoint
                chempoint.append(str(k+basepoint)+' '+str(data[1])+' '+str(round(data[2]+2.4*count,6))+' '+str(data[3])+' '+str(data[4])+' '+str(data[5]))
                connected.append([connect.pop(0),k+basepoint])
            else:
                k += 1
                dy[data[0]]=k+basepoint
                if len(data) == 7:chempoint.append(str(k+basepoint)+' '+str(data[1])+' '+str(round(data[2]+2.4*count,6))+' '+str(data[3])+' '+str(data[4])+' '+str(data[5])+' '+data[6])
                elif len(data) == 6:chempoint.append(str(k+basepoint)+' '+str(data[1])+' '+str(round(data[2]+2.4*count,6))+' '+str(data[3])+' '+str(data[4])+' '+str(data[5]))
        k = 0
        for pth in path['P']:
            k += 1
            p2 = dy[pth[2]]
            p3 = dy[pth[3]]
            chempath.append(str(k+basepath)+' '+str(pth[1])+' '+str(p2)+' '+str(p3))

    else:
        bf = 3
        if out[-1] == 'H':bf = 8
        if out[-1] == 'E' or out[-1] == 'Q' or out[-1] == 'R':bf = 6
        k = 0
        dy = {}
        for data in point[out[-1]]:
            if data[0] == bf:connected.append([connect.pop(0),k+basepoint])
            else:
                k += 1
                dy[data[0]]=k+basepoint
                if len(data) == 7:chempoint.append(str(k+basepoint)+' '+str(data[1])+' '+str(round(data[2]+2.4*count,6))+' '+str(data[3])+' '+str(data[4])+' '+str(data[5])+' '+data[6])
                elif len(data) == 6:chempoint.append(str(k+basepoint)+' '+str(data[1])+' '+str(round(data[2]+2.4*count,6))+' '+str(data[3])+' '+str(data[4])+' '+str(data[5]))
        k = 0
        for pth in path[out[-1]]:
            if bf == pth[2] or bf == pth[3]:pass
            else:
                k += 1
                p2 = dy[pth[2]]
                p3 = dy[pth[3]]
                chempath.append(str(k+basepath)+' '+str(pth[1])+' '+str(p2)+' '+str(p3))
    basepath = len(chempath)
    for k,num in zip(range(1,len(connected)+1,1),connected):chempath.append(str(k+basepath)+' 1 '+str(num[0])+' '+str(num[1]))

    grand = open('./'+str(key)+'_lt.mol','w')
    grand.write(''' \nKingDraw2D\n\n  0  0  0     0  0              0 V3000\nM  V30 BEGIN CTAB\n''')
    grand.write('M  V30 COUNTS '+str(len(chempoint))+' '+str(len(chempath))+' 0 0 0\n')
    grand.write('M  V30 BEGIN ATOM\n')
    for d in chempoint:grand.write('M  V30 '+d+'\n')
    grand.write('M  V30 END ATOM\nM  V30 BEGIN BOND\n')
    for d in chempath:grand.write('M  V30 '+d+'\n')
    grand.write('M  V30 END BOND\nM  V30 END CTAB\nM  END\n')
    grand.close()
    counting = {'H':0,'C':0}
    for d in chempoint:
        im = d.split(' ')
        try:
            if len(im) == 7 and 'H' in im[6]:counting['H']+=int(im[6][-1:])
            counting[im[1]] += 1
        except:counting[im[1]] = 1
    chem = ''
    for kkey in counting.keys():
        chem = chem + kkey+ str(counting[kkey]) + ' '
    ret['Chemical formula'] = chem
    poly = ''
    for d in out:poly = poly + d + '-'
    ret['polypeptide'] = poly[:-1]
    grand = open('./'+str(key)+'_ld.txt','w')
    for rekey in ret.keys():grand.write(rekey + (27-len(rekey))*' ' + ' : ' + str(ret[rekey]).replace("'","").replace('[','').replace(']','') + '\n')
    grand.close()
    return ret


if __name__ == '__main__':
    __init__()
    res = long_encoding(input())
    for rekey in res.keys():print(rekey,res[rekey])