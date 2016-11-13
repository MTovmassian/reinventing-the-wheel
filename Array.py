# coding: utf8
# python3

class Array:

	def __init__(self, *values):

			self.array = list()
			self.length = self.set_length()
			for i in values:
				self.push(i)

	def set_length(self):

		def _set_length(counter):
			try:
				self.array[counter]
				return _set_length(counter + 1)
			except:
				return counter

		self.length = _set_length(0)

	def push(self, val):
		self.array[self.length:self.length] =  [val]
		self.set_length()

	def remove(self, val):
		
		def _remove(input_list, output_list, removed_val):
			if len(input_list) > 1:
				if  input_list[0] == val and not removed_val:
					removed_val = input_list[0]
					input_list = input_list[1:]
					return _remove(input_list, output_list, removed_val)
				else:
					output_list.append(input_list[0])
					input_list = input_list[1:]
					return _remove(input_list, output_list, removed_val)
			elif len(input_list) == 1:
				if  input_list[0] == val and not removed_val:
					self.array = output_list
				else:
					output_list.append(input_list[0])
					self.array = output_list
		
		return _remove(self.array, list(), str())

	def join(self, sep):

		def _join(input_list, output_str, sep):
			if len(input_list) > 1:
				output_str += str(input_list[0]) + sep
				return _join(input_list[1:], output_str, sep)
			elif len(input_list) == 1:
				output_str += str(input_list[0])

			return output_str

		return _join(self.array, str(), sep)

	def map(self, func):
		def _map(input_list, output_list, func):
			if len(input_list) > 0:
				val = func(input_list[0])
				output_list.push(val)
				return _map(input_list[1:], output_list, func)
			return output_list

		return _map(self.array, Array(), func)

	def __repr__(self):
		return str(self.array)

# input_list = List([1])
# input_list.append(4)
# print(input_list.join(' '))
if __name__ == '__main__':
	input_list = Array(5,6)
	print(input_list.length)
	input_list.push(4)
	print(input_list.length)
	input_list.remove(6)
	print(input_list)
	# print(input_list.map(lambda x: x+1))
	# print(input_list.map(lambda x: x+4))
