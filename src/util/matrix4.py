import numpy as np


class Matrix4:
    def __init__(self):
        self.elements = np.array([1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0])

    def premultiply(self, mat):
        return self.__multiplyMatrix(mat, self)

    def multiply(self, mat):
        return self.__multiplyMatrix(self, mat)

    def makeTranslation(self, x, y, z):
        self.elements = np.array([1.0, 0.0, 0.0, x, 0.0, 1.0, 0.0, y, 0.0, 0.0, 1, z, 0.0, 0.0, 0.0, 1.0])
        return self

    def makeRotationFromQuaternion(self, q):
        x, y, z, w = q
        self.elements = np.array(
            [
                1.0 - 2.0 * y**2 - 2.0 * z**2,
                2.0 * x * y - 2.0 * z * w,
                2.0 * x * z + 2.0 * y * w,
                0.0,
                2.0 * x * y + 2.0 * z * w,
                1.0 - 2.0 * x**2 - 2.0 * z**2,
                2.0 * y * z - 2.0 * x * w,
                0.0,
                2.0 * x * z - 2.0 * y * w,
                2.0 * y * z + 2.0 * x * w,
                1.0 - 2.0 * x**2 - 2.0 * y**2,
                0.0,
                0.0,
                0.0,
                0.0,
                1.0,
            ]
        )
        return self

    def makeScale(self, x, y, z):
        self.elements = np.array([x, 0.0, 0.0, 0.0, 0.0, y, 0.0, 0.0, 0.0, 0.0, z, 0.0, 0.0, 0.0, 0.0, 1.0])
        return self

    def tovec(self):
        return self.elements

    def tolist(self):
        return self.elements.tolist()

    def print(self, *args):
        e = self.elements
        if args:
            print("↓", args)
        # print(e[:4])
        # print(e[4:8])
        # print(e[8:12])
        # print(e[12:16])
        print("→", ", ".join([str(x) for x in e.tolist()]))

    def __multiplyMatrix(self, mat1, mat2):
        ae = mat1.elements
        be = mat2.elements
        te = self.elements

        a11, a21, a31, a41, a12, a22, a32, a42, a13, a23, a33, a43, a14, a34, a24, a44 = ae
        b11, b21, b31, b41, b12, b22, b32, b42, b13, b23, b33, b43, b14, b34, b24, b44 = be

        te[0] = a11 * b11 + a12 * b21 + a13 * b31 + a14 * b41
        te[4] = a11 * b12 + a12 * b22 + a13 * b32 + a14 * b42
        te[8] = a11 * b13 + a12 * b23 + a13 * b33 + a14 * b43
        te[12] = a11 * b14 + a12 * b24 + a13 * b34 + a14 * b44

        te[1] = a21 * b11 + a22 * b21 + a23 * b31 + a24 * b41
        te[5] = a21 * b12 + a22 * b22 + a23 * b32 + a24 * b42
        te[9] = a21 * b13 + a22 * b23 + a23 * b33 + a24 * b43
        te[13] = a21 * b14 + a22 * b24 + a23 * b34 + a24 * b44

        te[2] = a31 * b11 + a32 * b21 + a33 * b31 + a34 * b41
        te[6] = a31 * b12 + a32 * b22 + a33 * b32 + a34 * b42
        te[10] = a31 * b13 + a32 * b23 + a33 * b33 + a34 * b43
        te[14] = a31 * b14 + a32 * b24 + a33 * b34 + a34 * b44

        te[3] = a41 * b11 + a42 * b21 + a43 * b31 + a44 * b41
        te[7] = a41 * b12 + a42 * b22 + a43 * b32 + a44 * b42
        te[11] = a41 * b13 + a42 * b23 + a43 * b33 + a44 * b43
        te[15] = a41 * b14 + a42 * b24 + a43 * b34 + a44 * b44

        return self
