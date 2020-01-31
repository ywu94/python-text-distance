from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import functools
import logging
logger = logging.getLogger(__name__)

class input_validator(object):
	def __init__(self, *exp_arg_types, **exp_kwarg_types):
		self.exp_arg_types = exp_arg_types
		self.exp_kwarg_types = exp_kwarg_types

	def __call__(self, fn):
		@functools.wraps(fn)
		def wrapper(*args, **kwargs):
			assert len(args) == len(self.exp_arg_types), "Expect {} arguments but get {}".format(len(self.exp_arg_types), len(args))
			for arg, exp_arg_type in zip(args, self.exp_arg_types): assert isinstance(arg, exp_arg_type), "Expect {} but get {}".format(exp_arg_type, type(arg))
			for k, v in kwargs.items(): assert isinstance(v, self.exp_kwarg_types.get(k,object)), "Expect {} for key {} but get {}".format(self.exp_kwarg_types[k], k, type(v))
			return fn(*args, **kwargs)
		return wrapper





