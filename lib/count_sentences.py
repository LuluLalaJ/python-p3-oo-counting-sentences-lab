#!/usr/bin/env python3

class MyString:
  def __init__(self, value='') -> None:
    self._value = value

  @property
  def value(self):
    return self._value

  @value.setter
  def value(self, val):
    if isinstance(val, str):
      self._value = val
    else:
      print("The value must be a string.")

  def is_sentence(self):
    return self.value.endswith(".")

  def is_question(self):
    return self.value.endswith("?")

  def is_exclamation(self):
    return self.value.endswith("!")

  def count_sentences(self):
    self.value = self.value.replace("?", ".")
    self.value = self.value.replace("!", ".")
    lst = self.value.split(".")
    sentences = [ele for ele in lst if ele]
    return len(sentences)




# word = MyString()
# word.value = "This, well, is a sentence. This is too!! And so is this, I think? Woo..."
# print(word.value)
# print(word.count_sentences())
