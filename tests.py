#coding: utf8
import unittest
import xmlutils

class XMLUtilsTestCase(unittest.TestCase):
    def setUp(self):
        self.dic = {'results': [{'result': {'rank': '1', 'plan': {'_attrs': {'id': '3044'}, 'name': u'なまえ'}}}]}

    def test_render(self):
        node = xmlutils.dict_to_node(self.dic)
        self.assertEqual(
            xmlutils.XMLRenderer().render(node, indent=2),
"""<?xml version="1.0" encoding="utf-8"?>
<results>
  <result>
    <plan id="3044">
      <name>なまえ</name>
    </plan>
    <rank>1</rank>
  </result>
</results>
"""
        )

if __name__ == '__main__':
    unittest.main()

