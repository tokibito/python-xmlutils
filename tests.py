#coding: utf8
import unittest
import xmlutils

class XMLUtilsTestCase(unittest.TestCase):
    def setUp(self):
        self.dic = {'results': [
            {'result': {'rank': '1', 'user': {'_attrs': {'id': '1234'}, 'name': u'ユーザ1'}}},
            {'result': {'rank': '2', 'user': {'_attrs': {'id': '1235'}, 'name': u'ユーザ2'}}},
        ]}

    def test_render(self):
        node = xmlutils.dict_to_node(self.dic)
        self.assertEqual(
            xmlutils.XMLRenderer().render(node, indent=2),
"""<?xml version="1.0" encoding="utf-8"?>
<results>
  <result>
    <user id="1234">
      <name>ユーザ1</name>
    </user>
    <rank>1</rank>
  </result>
  <result>
    <user id="1235">
      <name>ユーザ2</name>
    </user>
    <rank>2</rank>
  </result>
</results>
"""
        )
        self.assertEqual(
            xmlutils.XMLRenderer().render(node, indent=2, unichar=True),
"""<?xml version="1.0" encoding="utf-8"?>
<results>
  <result>
    <user id="1234">
      <name>&#12518;&#12540;&#12470;&#49;</name>
    </user>
    <rank>&#49;</rank>
  </result>
  <result>
    <user id="1235">
      <name>&#12518;&#12540;&#12470;&#50;</name>
    </user>
    <rank>&#50;</rank>
  </result>
</results>
"""
        )


if __name__ == '__main__':
    unittest.main()

