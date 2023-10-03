#!/usr/bin/env python3

import ipdb
from pet import Pet

# Owner.create_table()
# frank = Owner("frank", "555-555-5555", "frank@gmail.com", "555 Somewhere St.")
# frank.save()

Pet.drop_table()
Pet.create_table()
# spot = Pet("spot", "dog", "chihuahua", "feisty")

# spot.save()
spot = Pet("spot", "dog", "chihuahua", "feisty")
snowball = Pet("snowball", "dog", "Poodle", "friendly")

ipdb.set_trace()
