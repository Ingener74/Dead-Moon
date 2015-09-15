# encoding: utf8
from unittest import TestCase

from app.main import ExplorePath


class TestExplorePath(TestCase):
    def setUp(self):
        self.exp = ExplorePath()

    def test_go(self):
        self.assertEqual(self.exp.go('path1'), ['.', 'path1'])
        self.assertEqual(self.exp.go('path2'), ['.', 'path1', 'path2'])

    def test_up(self):
        self.assertEqual(len(self.exp.path), 1)
        self.assertEqual(self.exp.go('path1'), ['.', 'path1'])
        self.assertEqual(len(self.exp.path), 2)
        self.assertEqual(self.exp.go('path2'), ['.', 'path1', 'path2'])
        self.assertEqual(len(self.exp.path), 3)

        self.exp.up()
        self.assertEqual(len(self.exp.path), 2)

        self.exp.up()
        self.assertEqual(len(self.exp.path), 1)

        self.assertRaises(self.exp.up(), TypeError)
        self.assertEqual(len(self.exp.path), 1)

    def test_getPath(self):
        self.assertEqual(self.exp.getPath(), './')

        self.assertEqual(self.exp.go('path1'), ['.', 'path1'])
        self.assertEqual(self.exp.getPath(), './path1/')

        self.assertEqual(self.exp.go('path2'), ['.', 'path1', 'path2'])
        self.assertEqual(self.exp.getPath(), './path1/path2/')

