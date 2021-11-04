import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_team_toimii(self):
        list = self.statistics.team("EDM")

        self.assertAlmostEqual(list[0].name, "Semenko")

    def test_search_toimii(self):
        player = self.statistics.search("Semenko")

        self.assertEqual(player.name, "Semenko")

    def test_search_vaaralla_nimella(self):
        player = self.statistics.search("ofdgoi")

        self.assertEqual(player, None)

    def test_top_scores_toimii(self):
        result = self.statistics.top_scorers(3)

        self.assertAlmostEqual(result[0].name, "Gretzky")
