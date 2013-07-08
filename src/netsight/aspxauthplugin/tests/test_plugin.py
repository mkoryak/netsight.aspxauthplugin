import unittest2 as unittest
import time
from netsight.aspxauthplugin.plugin import ASPXAuthPlugin

#from netsight.aspxauthplugin.testing import \
#    NETSIGHT_ASPXAUTHPLUGIN_INTEGRATION_TESTING


class TestExample(unittest.TestCase):

#    layer = NETSIGHT_ASPXAUTHPLUGIN_INTEGRATION_TESTING

    def setUp(self):
        # you'll want to use this to set up anything you need for your tests
        # below
        pass

    def test_rebuild_cookie(self):
        plugin = ASPXAuthPlugin('aspxauth')
        plugin.validation_key = """07B6387D1DED6BF193EDD726B4ADFD6B92EDA470DDF639D4B78110CA797DCED426BECF322B9FBCC5E7C3FDA2E7BA28169611B1ACD1E7F063ABF17ECDC30AD482"""
        plugin.decryption_key = """CFE45C8F9D17D68B71DAB98158E1F78E5AC05D6C5A7184BD1BF26E6E36FA5973"""

        version = 2
        start_time = int(time.time())
        end_time = int(start_time + (60 * 20) )
        username = 'matth@netsight.co.uk'

        cookie = plugin.encryptCookie(version, start_time, end_time, username)
        sig, data = plugin.decodeCookie(cookie)
        data = plugin.decryptData(data)
        import pdb; pdb.set_trace()

        self.assertEqual(plugin.unpackData(data), (version, start_time, end_time, username))


    def test_crypto_pass(self):
        plugin = ASPXAuthPlugin('aspxauth')
        plugin.validation_key = """07B6387D1DED6BF193EDD726B4ADFD6B92EDA470DDF639D4B78110CA797DCED426BECF322B9FBCC5E7C3FDA2E7BA28169611B1ACD1E7F063ABF17ECDC30AD482"""
        plugin.decryption_key = """CFE45C8F9D17D68B71DAB98158E1F78E5AC05D6C5A7184BD1BF26E6E36FA5973"""

        cookie = """31EBBD78D6F27972394A513A161AD0362E7906830460CE7D3F44E47B2F1AF63DD43E02EB22259E4AF342B232768D6701C9395AF42448E5D149FE8AE2E4D355E9F43A9B60E1A30C0282F9ED470D8037F3B9D1D965293BED7C6156672527A94B22F24039C3F7CA6ECFF6D50A0BFFB38C0E03FF9644092FB5F8FD6E6292AA7A49B5FF603456DE4EA041F785CC163A92C34937FDE017""" 
        
        self.assertEqual(plugin.authenticateCredentials({'cookie': cookie, 'plugin': plugin.getId()}), ('matth@netsight.co.uk', 'matth@netsight.co.uk'))

    def test_crypto_fail_badcookie(self):
        plugin = ASPXAuthPlugin('aspxauth')
        plugin.validation_key = """07B6387D1DED6BF193EDD726B4ADFD6B92EDA470DDF639D4B78110CA797DCED426BECF322B9FBCC5E7C3FDA2E7BA28169611B1ACD1E7F063ABF17ECDC30AD482"""
        plugin.decryption_key = """CFE45C8F9D17D68B71DAB98158E1F78E5AC05D6C5A7184BD1BF26E6E36FA5973"""

        cookie = """31EBBD78D6F27972394A513A161AD0362E7906830460CE7D3F44E47B2F1AF63DD43E02EB22259E4AF342B232768D6701C9395AF42448E5D149FE8AE2E4D355E9F43A9B60E1A30C0282F9ED470D8037F3B9D1D965293BED7C6156672527A94B22F24039C3F7CA6ECFF6D50A0BFFB38C0E03FF9644092FB5F8FD6E6292AA7A49B5FF603456DE4EA041F785CC163A92C34937FDE018""" 

        self.assertEqual(plugin.authenticateCredentials({'cookie': cookie, 'plugin': plugin.getId()}), None)

    def test_crypto_fail_validation_key(self):
        plugin = ASPXAuthPlugin('aspxauth')
        plugin.validation_key = """07B6387D1DED6BF193EDD726B4ADFD6B92EDA470DDF639D4B78110CA797DCED426BECF322B9FBCC5E7C3FDA2E7BA28169611B1ACD1E7F063ABF17ECDC30AD483"""
        plugin.decryption_key = """CFE45C8F9D17D68B71DAB98158E1F78E5AC05D6C5A7184BD1BF26E6E36FA5973"""

        cookie = """31EBBD78D6F27972394A513A161AD0362E7906830460CE7D3F44E47B2F1AF63DD43E02EB22259E4AF342B232768D6701C9395AF42448E5D149FE8AE2E4D355E9F43A9B60E1A30C0282F9ED470D8037F3B9D1D965293BED7C6156672527A94B22F24039C3F7CA6ECFF6D50A0BFFB38C0E03FF9644092FB5F8FD6E6292AA7A49B5FF603456DE4EA041F785CC163A92C34937FDE017""" 

        self.assertEqual(plugin.authenticateCredentials({'cookie': cookie, 'plugin': plugin.getId()}), None)

    def test_crypto_fail_decryption_key(self):
        plugin = ASPXAuthPlugin('aspxauth')
        plugin.validation_key = """07B6387D1DED6BF193EDD726B4ADFD6B92EDA470DDF639D4B78110CA797DCED426BECF322B9FBCC5E7C3FDA2E7BA28169611B1ACD1E7F063ABF17ECDC30AD482"""
        plugin.decryption_key = """CFE45C8F9D17D68B71DAB98158E1F78E5AC05D6C5A7184BD1BF26E6E36FA5972"""

        cookie = """31EBBD78D6F27972394A513A161AD0362E7906830460CE7D3F44E47B2F1AF63DD43E02EB22259E4AF342B232768D6701C9395AF42448E5D149FE8AE2E4D355E9F43A9B60E1A30C0282F9ED470D8037F3B9D1D965293BED7C6156672527A94B22F24039C3F7CA6ECFF6D50A0BFFB38C0E03FF9644092FB5F8FD6E6292AA7A49B5FF603456DE4EA041F785CC163A92C34937FDE017""" 

        self.assertEqual(plugin.authenticateCredentials({'cookie': cookie, 'plugin': plugin.getId()}), None)