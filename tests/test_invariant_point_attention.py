import torch
import unittest
from src.models.components.invariant_point_attention import InvariantPointAttention
from src.utils.geometry import rotation_matrix, vector
from src.utils.geometry.rigid_matrix_vector import Rigid3Array


class TestInvariantPointAttention(unittest.TestCase):
    def test_shape(self):
        c_m = 13
        c_z = 17
        c_hidden = 19
        no_heads = 5
        no_qp = 7
        no_vp = 11

        batch_size = 2
        n_res = 23

        s = torch.rand((batch_size, n_res, c_m))
        z = torch.rand((batch_size, n_res, n_res, c_z))
        mask = torch.ones((batch_size, n_res))

        rot_mats = torch.rand((batch_size, n_res, 3, 3))
        rots = rotation_matrix.Rot3Array.from_array(rot_mats)
        trans_ = torch.rand((batch_size, n_res, 3))
        trans = vector.Vec3Array.from_array(trans_)
        r = Rigid3Array(rots, trans)

        ipa = InvariantPointAttention(
            c_m, c_z, c_hidden, no_heads, no_qp, no_vp
        )

        shape_before = s.shape
        s = ipa(s, z, r, mask)

        self.assertTrue(s.shape == shape_before)


if __name__ == "__main__":
    unittest.main()
