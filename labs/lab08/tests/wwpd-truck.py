test = {
  'name': 'Car',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from car import *
          >>> deneros_car = Car('Tesla', 'Model S')
          >>> deneros_truck = MonsterTruck('Monster', 'Batmobile')
          >>> deneros_car.size # Type Error if an error occurs and Nothing if nothing is displayed
          8b1b16415e2c0ff19bfb5c4e54f6f878
          # locked
          >>> deneros_car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
          6782dfbb8a7616b3f504afa7bdbc4efe
          # locked
          >>> deneros_truck.size # Type Error if an error occurs and Nothing if nothing is displayed
          c5ace7df7c7b66fd8733af007dd50564
          # locked
          >>> deneros_truck.drive() # Type Error if an error occurs and Nothing if nothing is displayed
          543d3c4044c7b885e6bc773187315cb9
          2e96bc0878a8a5a4b77deec4ef4b3d09
          # locked
          >>> MonsterTruck.drive(deneros_truck) # Type Error if an error occurs and Nothing if nothing is displayed
          543d3c4044c7b885e6bc773187315cb9
          2e96bc0878a8a5a4b77deec4ef4b3d09
          # locked
          >>> Car.drive(deneros_truck) # Type Error if an error occurs and Nothing if nothing is displayed
          2e96bc0878a8a5a4b77deec4ef4b3d09
          # locked
          >>> deneros_truck.gas # Type Error if an error occurs and Nothing if nothing is displayed
          7c2ddff07764c87227f4781f812caaa6
          # locked
          >>> MonsterTruck.rev(deneros_truck) # Type Error if an error occurs and Nothing if nothing is displayed
          543d3c4044c7b885e6bc773187315cb9
          # locked
          >>> MonsterTruck.rev(deneros_car) # Type Error if an error occurs and Nothing if nothing is displayed
          543d3c4044c7b885e6bc773187315cb9
          # locked
          >>> Car.rev(deneros_truck) # Type Error if an error occurs and Nothing if nothing is displayed
          8a2fd4e4c3c6dcce2dc631af62ee217a
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
