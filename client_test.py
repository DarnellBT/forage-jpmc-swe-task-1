import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      ratio = (quote['top_bid']['price'] + quote['top_ask']['price']) / 2
      data_point = (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], ratio)
      self.assertEqual(getDataPoint(quote), data_point)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      ratio = (quote['top_bid']['price'] + quote['top_ask']['price']) / 2
      data_point = (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], ratio)
      self.assertEqual(getDataPoint(quote), data_point)

  """ ------------ Add more unit tests ------------ """
  def test_getRatio_calculateRatio(self):
    price_pairs = [
      {'price_a': 121.2, 'price_b': 121.68},
      {'price_a': 120.48, 'price_b': 117.87}
    ]
    for prices in price_pairs:
      ratio = prices['price_a'] / prices['price_b']
      self.assertEqual(getRatio(*prices.values()), ratio)

  def test_getRatio_calculateRatioSecondPriceIsZero(self):
    price_pairs = [
      {'price_a': 121.2, 'price_b': 0},
      {'price_a': 120.48, 'price_b': 0}
    ]
    for prices in price_pairs:
      self.assertEqual(getRatio(*prices.values()), None)

if __name__ == '__main__':
    unittest.main()
