from bili_kits.account import *
import unittest

class TestUser(unittest.TestCase):
    def test_card_info_method(self):
        result = get_user_card_info(1)
        self.assertEqual(result['mid'],'1')
        self.assertEqual(result['name'],"bishi")  
        self.assertEqual(result['sex'],'男')
        self.assertEqual(result['face'],'http://i0.hdslb.com/bfs/face/34c5b30a990c7ce4a809626d8153fa7895ec7b63.gif')
    def test_instance(self):
        bu = BaseUser()
        self.assertEqual(bu.islogined,False)
        with self.assertRaises(UserNotLoginError):
            bu.expires
        with self.assertRaises(UserNotLoginError):
            bu.nav_info
       
if __name__ == '__main__':
    unittest.main()
 