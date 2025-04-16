
import unittest

from ..quote_centermsg import quote_centermsg

class TestQuoteCenterMsg(unittest.TestCase):

    def test_beachvolley(self):
        self.assertEqual(
            quote_centermsg("es_delayed 2 es_centermsg [RandomSettings] HE Paradise v2 (HE hurt = 0.5s Ball Slow) [Bomb Cost 120]"),
            "es_delayed 2 es_centermsg \"[RandomSettings] HE Paradise v2 (HE hurt = 0.5s Ball Slow) [Bomb Cost 120]\""
        )
        self.assertEqual(
            quote_centermsg("es_delayed 0.1 es_centermsg [Randomsettings] Slapball | Gravity 700 [Bomb ON]"),
            "es_delayed 0.1 es_centermsg \"[Randomsettings] Slapball | Gravity 700 [Bomb ON]\""
        )

    def test_quote_centermsg(self):
        self.assertEqual(
            quote_centermsg("es_centermsg foo bar"),
            "es_centermsg \"foo bar\""
        )

    def test_quote_delayed_centermsg(self):
        self.assertEqual(
            quote_centermsg("es_delayed 0.1 es_centermsg foo bar"),
            "es_delayed 0.1 es_centermsg \"foo bar\""
        )

    def test_ignore_already_quoted_message(self):
        self.assertEqual(
            quote_centermsg("es_centermsg \"foo bar\""),
            "es_centermsg \"foo bar\""
        )

    def test_escaped_quotes(self):
        self.assertEqual(
            quote_centermsg("es_centermsg \\\"foo bar\\\""),
            "es_centermsg \"\\\"foo bar\\\"\""
        )

if __name__ == "__main__":
    unittest.main()
